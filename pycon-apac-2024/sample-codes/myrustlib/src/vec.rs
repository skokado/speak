use pyo3::prelude::*;

#[pyfunction]
pub fn l2norm(x: Vec<f64>) -> PyResult<f64> {
    let mut total: f64 = 0.0;
    for i in 0..x.len() {
        total += x[i] * x[i];
    }
    Ok(total.sqrt())
}
