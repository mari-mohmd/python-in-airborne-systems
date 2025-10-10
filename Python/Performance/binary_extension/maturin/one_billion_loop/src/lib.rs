/*
===============================================================================
 Project    : Assessing Python’s Suitability for Airborne Safety-Critical
                       Systems under DO-178C Guidelines
 File       : lib.rs
 Author(s)  : Mohammad Mari, Lian Wen
 Affiliation: School of ICT, Griffith University
 Contact    : mohammad.mari@griffithuni.edu.au
 Created    : 2025
 License    : MIT License (see LICENSE file for details)
 Description: Core experiment code to demonstrate building binary ext. for Python
 Usage      : maturin build
===============================================================================
*/

// This file is built using maturin, which produces a Python wheel package.
// The generated wheel can be installed with pip, making the module available
// for use in Python.


use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn compiled_function() -> PyResult<String> {
    let mut x: usize = 0;
    for i in 0..1_000_000_000 {
        x += 1;
    }
    Ok((x).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn one_billion_loop(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compiled_function, m)?)?;
    Ok(())
}