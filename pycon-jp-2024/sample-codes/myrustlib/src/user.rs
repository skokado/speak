use crate::exceptions::UserGotAngryException;
use pyo3::prelude::*;

#[pyclass]
pub struct User {
    name: String,
    age: u32,
}

#[pymethods]
impl User {
    #[new]
    pub fn new(name: String, age: u32) -> Self {
        Self { name, age }
    }

    pub fn greet(&self) -> PyResult<()> {
        println!("Hi I'm {}!", self.name);
        Ok(())
    }

    pub fn get_age(&self) -> u32 {
        self.age
    }

    pub fn get_angry(&self) -> PyResult<()> {
        let msg = format!("User {} got angry🙄", self.name);
        Err(UserGotAngryException::new_err(msg))
    }
}
