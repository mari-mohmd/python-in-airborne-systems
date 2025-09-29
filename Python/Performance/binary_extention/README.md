# Python Binary Extension with Maturin

This project demonstrates how to create a Python binary extension module using [Maturin](https://github.com/PyO3/maturin).
The module is written in Rust, compiled into a Python wheel, and can be imported directly in Python after installation.

---

## Prerequisites

Before building, ensure the following tools are installed:

* **Rust toolchain** (via [rustup](https://rustup.rs/))
* **Python 3.8+** (with `pip`)
* **Maturin** (`pip install maturin`)

---

## Steps Performed

### 1. Create a new Rust/extension project

```bash
mkdir one_billion_loop
cd one_billion_loop
maturin init
```

### 2. Add dependencies in `Cargo.toml`

```toml
[package]
name = "one_billion_loop"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
[lib]
name = "one_billion_loop"
crate-type = ["cdylib"]

[dependencies]
pyo3 = "0.20.0"
```

### 3. Implement a Python function in Rust (`src/lib.rs`)

```rust
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn compiled_function() -> PyResult<String> {
    let mut x: usize = 0;
    for i in 0..1000000000 {
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
```

### 4. Build the Python wheel using Maturin

```bash
maturin build
```

This will produce a `.whl` file in the `target/wheels/` directory.

### 5. Install the wheel into Python

```bash
pip install target/wheels/one_billion_loop-0.1.0-cp312-cp312-macosx_11_0_arm64.whl
```

### 6. Use the extension in Python `compiled_loop.py`

```python
import time
import one_billion_loop # Importing the binary module created by maturin

start_time= time.time()
print ( " Finished x is : " , one_billion_loop.compiled_function() , 
       " ..... Duration : " , time.time() - start_time , " seconds " )
```

---


## License

MIT License
