use pyo3::intern;
use pyo3::prelude::*;

// Cache for the dataclasses module
pub struct DataclassMod<'py> {
    is_dataclass_fn: Bound<'py, PyAny>,
    pub asdict: Bound<'py, PyAny>,
}

impl<'py> DataclassMod<'py> {
    pub fn new(py: Python<'py>) -> PyResult<Self> {
        let module = py.import("dataclasses")?;
        let is_dataclass_fn = module.getattr(intern!(py, "is_dataclass"))?;
        let asdict = module.getattr(intern!(py, "asdict"))?;

        Ok(Self {
            is_dataclass_fn,
            asdict,
        })
    }

    pub fn is_dataclass(&self, obj: &Bound<'_, PyAny>) -> PyResult<bool> {
        let result = self.is_dataclass_fn.call1((obj,))?;
        result.extract::<bool>()
    }
}
