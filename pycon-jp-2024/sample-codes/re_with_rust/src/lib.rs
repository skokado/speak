use pyo3::prelude::*;
use regex::Regex;

// 引数で指定された正規表現を使用して、テキストを置換する関数
#[pyfunction]
fn replace_with_pattern(pattern: &str, text: &str, replacement: &str) -> String {
    let re = Regex::new(pattern).unwrap();
    re.replace_all(text, replacement).to_string()
}

/// A Python module implemented in Rust.
#[pymodule]
fn replacer(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(replace_with_pattern, m)?)?;
    Ok(())
}
