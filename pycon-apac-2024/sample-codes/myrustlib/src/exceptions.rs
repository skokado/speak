use pyo3::exceptions::PyException;

use pyo3::create_exception;

// See also: https://pyo3.rs/v0.22.2/exception
create_exception!(myrustlib, UserGotAngryException, PyException);
