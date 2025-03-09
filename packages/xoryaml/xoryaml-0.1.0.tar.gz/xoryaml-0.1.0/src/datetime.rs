use pyo3::exceptions::PyValueError;
use pyo3::intern;
use pyo3::prelude::*;
use speedate::{Date, DateTime, Duration, Time};

pub fn pytimedelta_as_duration(py_timedelta: &Bound<'_, PyAny>) -> PyResult<Duration> {
    let total_seconds: f64 = py_timedelta
        .call_method0(intern!(py_timedelta.py(), "total_seconds"))?
        .extract()?;
    if total_seconds.is_nan() {
        return Err(PyValueError::new_err("NaN values not permitted"));
    }
    let positive = total_seconds >= 0_f64;
    let total_seconds = total_seconds.abs();
    let microsecond = total_seconds.fract() * 1_000_000.0;
    let days = (total_seconds / 86400f64) as u32;
    let seconds = total_seconds as u64 % 86400;
    Duration::new(positive, days, seconds as u32, microsecond.round() as u32)
        .map_err(|err| PyValueError::new_err(err.to_string()))
}

pub fn pydate_as_date(py_date: &Bound<'_, PyAny>) -> PyResult<Date> {
    let py = py_date.py();
    let date = Date {
        year: py_date.getattr(intern!(py, "year"))?.extract()?,
        month: py_date.getattr(intern!(py, "month"))?.extract()?,
        day: py_date.getattr(intern!(py, "day"))?.extract()?,
    };
    Ok(date)
}

pub fn pytime_as_time(
    py_time: &Bound<'_, PyAny>,
    py_dt: Option<&Bound<'_, PyAny>>,
) -> PyResult<Time> {
    let py = py_time.py();

    let tzinfo = py_time.getattr(intern!(py, "tzinfo"))?;
    let tz_offset: Option<i32> = if PyAnyMethods::is_none(&tzinfo) {
        None
    } else {
        let offset_delta = tzinfo.call_method1(intern!(py, "utcoffset"), (py_dt,))?;
        // as per the docs, utcoffset() can return None
        if PyAnyMethods::is_none(&offset_delta) {
            None
        } else {
            let offset_seconds: f64 = offset_delta
                .call_method0(intern!(py, "total_seconds"))?
                .extract()?;
            Some(offset_seconds.round() as i32)
        }
    };

    Ok(Time {
        hour: py_time.getattr(intern!(py, "hour"))?.extract()?,
        minute: py_time.getattr(intern!(py, "minute"))?.extract()?,
        second: py_time.getattr(intern!(py, "second"))?.extract()?,
        microsecond: py_time.getattr(intern!(py, "microsecond"))?.extract()?,
        tz_offset,
    })
}

pub fn pydatetime_as_datetime(py_dt: &Bound<'_, PyAny>) -> PyResult<DateTime> {
    Ok(DateTime {
        date: pydate_as_date(py_dt)?,
        time: pytime_as_time(py_dt, Some(py_dt))?,
    })
}
