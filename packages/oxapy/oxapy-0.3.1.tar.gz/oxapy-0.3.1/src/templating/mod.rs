use pyo3::{
    types::{PyModule, PyModuleMethods},
    Bound, PyResult,
};

mod minijinja;
mod tera;

pub fn templating_submodule(parent_module: &Bound<'_, PyModule>) -> PyResult<()> {
    let templating = PyModule::new(parent_module.py(), "templating")?;
    templating.add_class::<self::tera::Tera>()?;
    templating.add_class::<self::minijinja::Jinja>()?;
    parent_module.add_submodule(&templating)
}
