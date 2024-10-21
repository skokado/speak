use pyo3::prelude::*;

#[pyfunction]
pub fn eratosthenes(limit: usize) -> PyResult<Vec<usize>> {
    let mut prime_flags: Vec<bool> = vec![true; limit];

    let mut p: usize = 2;
    while (p * p) <= limit {
        if prime_flags[p] {
            for i in ((p * p)..limit).step_by(p) {
                prime_flags[i] = false
            }
        }
        p += 1;
    }

    let mut primes: Vec<usize> = vec![];
    for (i, _) in prime_flags.iter().enumerate().take(limit).skip(2) {
        if prime_flags[i] {
            primes.push(i)
        }
    }

    Ok(primes)
}

#[pyfunction]
pub fn get_primes(max: u32) -> PyResult<Vec<u32>> {
    let mut primes: Vec<u32> = vec![2];

    for n in (3..=max).step_by(2) {
        let mut i: u32 = 3;
        let mut is_prime = true;
        while i * i <= n {
            if n % i == 0 {
                is_prime = false;
                break;
            }
            i += 2;
        }
        if is_prime {
            primes.push(n);
        }
    }
    Ok(primes)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_lib(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(eratosthenes, m)?)?;
    m.add_function(wrap_pyfunction!(get_primes, m)?)?;
    Ok(())
}
