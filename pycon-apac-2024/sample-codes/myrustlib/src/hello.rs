use pyo3::prelude::*;

#[pyfunction]
pub fn hello_world() -> PyResult<()> {
    println!("Hello from Rust!");
    Ok(())
}
