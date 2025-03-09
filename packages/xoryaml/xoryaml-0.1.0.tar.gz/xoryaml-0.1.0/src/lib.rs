use pyo3::create_exception;
use pyo3::prelude::*;
use pyo3::types::{PyDate, PyDateTime, PyDelta, PyDict, PyList, PyTime};
use pyo3::wrap_pyfunction;
use pyo3::Python;
use pyo3::{exceptions::PyTypeError, exceptions::PyValueError};
use std::collections::HashSet;
use yaml_rust2::{Yaml, YamlEmitter, YamlLoader};

mod datetime;

create_exception!(xoryaml, YAMLDecodeError, PyValueError);
create_exception!(xoryaml, YAMLEncodeError, PyTypeError);

fn deserialize_all_yaml(str: &str) -> PyResult<Vec<Yaml>> {
    match YamlLoader::load_from_str(str) {
        Ok(docs) => Ok(docs),
        Err(err) => Err(YAMLDecodeError::new_err(err.to_string())),
    }
}

fn serialize_yaml(yaml: &Yaml) -> PyResult<String> {
    let mut out_str = String::new();
    let mut emitter = YamlEmitter::new(&mut out_str);
    match emitter.dump(yaml) {
        Ok(_) => Ok(out_str),
        Err(err) => Err(YAMLEncodeError::new_err(err.to_string())),
    }
}

fn yaml_to_pyobject_inner(py: Python, yaml: &Yaml) -> PyResult<PyObject> {
    match yaml {
        Yaml::Real(s) => {
            if let Ok(f) = s.parse::<f64>() {
                Ok(f.into_py(py))
            } else {
                Ok(s.into_py(py))
            }
        }
        Yaml::Integer(i) => Ok(i.into_py(py)),
        Yaml::String(s) => Ok(s.into_py(py)),
        Yaml::Boolean(b) => Ok(b.into_py(py)),
        Yaml::Array(arr) => {
            let list = PyList::empty(py);
            for item in arr {
                list.append(yaml_to_pyobject_inner(py, item)?)?;
            }
            Ok(list.into())
        }
        Yaml::Hash(hash) => {
            let dict = PyDict::new(py);
            for (k, v) in hash {
                let py_key = yaml_to_pyobject_inner(py, k)?;
                let py_value = yaml_to_pyobject_inner(py, v)?;
                dict.set_item(py_key, py_value)?;
            }
            Ok(dict.into())
        }
        Yaml::Null => Ok(py.None()),
        Yaml::BadValue => Err(YAMLDecodeError::new_err("Invalid YAML value")),
        Yaml::Alias(_) => Err(YAMLDecodeError::new_err("YAML aliases not supported")),
    }
}

fn yaml_to_pyobject(py: Python, yaml: &Yaml) -> PyResult<PyObject> {
    yaml_to_pyobject_inner(py, yaml).map_err(|e| {
        YAMLDecodeError::new_err(format!("Error converting YAML to Python object: {}", e))
    })
}

fn pyobject_to_yaml_inner(
    obj: &Bound<'_, PyAny>,
    visited: &mut HashSet<*mut PyAny>,
) -> PyResult<Yaml> {
    let ptr = obj.as_ptr() as *mut PyAny;

    if !visited.insert(ptr) {
        return Err(YAMLEncodeError::new_err("Circular reference detected"));
    }

    let result = if obj.is_none() {
        Ok(Yaml::Null)
    } else if let Ok(s) = obj.extract::<String>() {
        Ok(Yaml::String(s))
    } else if let Ok(b) = obj.extract::<bool>() {
        Ok(Yaml::Boolean(b))
    } else if let Ok(i) = obj.extract::<i64>() {
        Ok(Yaml::Integer(i))
    } else if let Ok(f) = obj.extract::<f64>() {
        Ok(Yaml::Real(f.to_string()))
    } else if obj.is_instance_of::<PyDateTime>() {
        let datetime = datetime::pydatetime_as_datetime(obj)?;
        Ok(Yaml::String(datetime.to_string()))
    } else if obj.is_instance_of::<PyDate>() {
        let date = datetime::pydate_as_date(obj)?;
        Ok(Yaml::String(date.to_string()))
    } else if obj.is_instance_of::<PyTime>() {
        let time = datetime::pytime_as_time(obj, None)?;
        Ok(Yaml::String(time.to_string()))
    } else if obj.is_instance_of::<PyDelta>() {
        let delta = datetime::pytimedelta_as_duration(obj)?;
        Ok(Yaml::String(delta.to_string()))
    } else if let Ok(list) = obj.downcast::<PyList>() {
        let mut yaml_array = Vec::new();
        for item in list.iter() {
            yaml_array.push(pyobject_to_yaml_inner(&item, visited)?);
        }
        Ok(Yaml::Array(yaml_array))
    } else if let Ok(dict) = obj.downcast::<PyDict>() {
        let mut yaml_hash = yaml_rust2::yaml::Hash::new();
        for (k, v) in dict.iter() {
            yaml_hash.insert(
                pyobject_to_yaml_inner(&k, visited)?,
                pyobject_to_yaml_inner(&v, visited)?,
            );
        }
        Ok(Yaml::Hash(yaml_hash))
    } else {
        Err(YAMLEncodeError::new_err(format!(
            "Unsupported Python type: {}",
            obj.get_type().name()?
        )))
    };

    visited.remove(&ptr);
    result
}

// Wrapper function to initialize the visited set
pub fn pyobject_to_yaml(obj: &Bound<'_, PyAny>) -> PyResult<Yaml> {
    let mut visited = HashSet::new();
    pyobject_to_yaml_inner(obj, &mut visited)
}

#[pyfunction]
fn loads_all(py: Python, str: &str) -> PyResult<PyObject> {
    if str.is_empty() {
        Ok(Python::None(py))
    } else {
        let documents = deserialize_all_yaml(str)?;
        let mut pydocs = vec![];
        for doc in documents {
            pydocs.push(yaml_to_pyobject(py, &doc)?);
        }
        Ok(PyList::new_bound(py, pydocs).to_object(py))
    }
}

#[pyfunction]
fn dumps(obj: &Bound<'_, PyAny>) -> PyResult<String> {
    let yaml = pyobject_to_yaml(obj)?;
    serialize_yaml(&yaml)
}

#[pymodule]
fn xoryaml(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("YAMLDecodeError", m.py().get_type::<YAMLDecodeError>())?;
    m.add("YAMLEncodeError", m.py().get_type::<YAMLEncodeError>())?;
    m.add_function(wrap_pyfunction!(loads_all, m)?)?;
    m.add_function(wrap_pyfunction!(dumps, m)?)?;

    Ok(())
}
