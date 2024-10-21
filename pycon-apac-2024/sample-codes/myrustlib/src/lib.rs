use pyo3::prelude::*;

mod exceptions;
mod hello;
mod vec;
mod user;

use exceptions::UserGotAngryException;
use hello::hello_world;
use vec::l2norm;
use user::User;

#[pymodule]
fn myrustlib(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(l2norm, m)?)?;
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    m.add_class::<User>()?;
    m.add(
        "UserGotAngryException",
        py.get_type_bound::<UserGotAngryException>(),
    )?;
    Ok(())
}
