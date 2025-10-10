# Assessing Python’s Suitability for Airborne Safety-Critical Systems under DO-178C Guidelines

This repository contains experimental code and demonstrations associated with the research paper **“Assessing Python’s Suitability for Airborne Safety-Critical Systems.”**  
The experiments focus on Python’s behavior with respect to two main quality attributes: performance and reliability.

---

## Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Environment](#environment)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)
- [Authors](#authors)

---

## Overview

This project evaluates Python’s suitability for safety-critical applications, particularly in the context of DO-178C certification for airborne systems. While Python is widely adopted for its ease of use and flexibility, limitations such as lack of compile-time checks, delayed signal handling, and limited optimization raise concerns for reliability in high-assurance environments.
We compare Python against Rust, a modern language designed with safety and performance in mind. Rust is not presented as a replacement for traditional safety-critical languages (Ada, C, C++), but as a useful benchmark to highlight how a safety-oriented compiled language contrasts with Python’s interpreted model.

---

## Repository Structure
```plaintext

├── Python/
│   ├── Performance/
│   |   ├── bounded_latency/                   
│   |   │   ├── bounded_latency_single_thread.py
│   |   │   ├── bounded_latency_multi_thread.py
│   |   │   └── bounded_latency_multi_process.py
|   |   |
│   |   ├── binary_extension/
|   |   |   ├── maturin/                   
|   │   |   │   ├── compiled_loop.py
|   │   |   │   ├── README.md
|   │   |   │   └── one_billion_loop
|   |   |   |       ├── src/
|   |   |   |       |   └── lib.rs
|   |   |   |       ├── Cargo.toml
|   |   |   |       ├── Cargo.lco
|   |   |   |       └── pyproject.toml 
|   |   |   └── cython_pyoxidizer/
|   │   |        ├── one_billion_loop.pyx
|   │   |        ├── pyoxidizer.toml
|   │   |        ├── setup.py
|   │   |        ├── tester.py
|   │   |        └── README.md
|   |   |    
|   |   ├── just_in_time_compilation/
|   |   |   ├── jit.py
|   |   |   └── no_jit.py
|   |   |
│   |   ├── global_local_scopes/               
│   |   |   ├── execution_global_scope.py
│   |   |   └── execution_local_scope.py
|   |   |
|   |   └── peephole_optimization.py
|   |
|   ├── Python_Characteristics/
│   |   ├── code_processing/                   
│   |   │   ├── ast_demo.py
│   |   │   ├── compile_demo.py
│   |   │   └── tokenization_demo.py
│   |   │
|   |   └── error_detection/
|   |       ├── indentation_error.py
|   |       ├── syntax_error.py
|   |       └── tab_error.py    
|   |
|   ├── Reliability/
│   |   ├── recursion_depth.py
│   |   ├── deferred_error_detection.py
|   |   ├── signal_handle_re_test.py
|   |   ├── signal_handle_regex_test.py
|   |   └── signal_handle_tester.py 
|   |
│   └── tester.py 
│
├── Rust/
│   ├── performance/
│   |   └── bounded_latency/                   
│   |       ├── bounded_latency_single_thread.rs
│   |       └── bounded_latency_multi_thread.rs
│   ├── Reliability/
│   |    └── signal_handling                   
│   |        ├── src/main.rs
│   |        ├── src/signal_handle_tester.py
│   |        └── Cargo.toml
│   └── one-billion-loop.rs
|
├── README.md                                 
├── LICENSE                                   
└── requirements.txt 
```

## Environment

The experiments in this repository were conducted under the following environment:

### Operating System and Hardware
- **Operating System:** macOS 15.6.1 (Sequoia) 
- **CPU:** Apple M1 Pro, 10-core CPU  
- **RAM:** 16 GB  
- **Notes:** Multi-core CPU allows comparison between single-threaded, multi-threaded, and multiprocessing experiments. Timing results may vary on different hardware.

### Python Experiments
- **Python Version:** 3.9.0 
- **Key Libraries:**  
  - `multiprocessing` (standard library)  
  - `threading` (standard library)  
  - `numba` for JIT compilation experiments  
  - `regex` used as an alternative to `re` in our experiments.

### Rust Experiments
- **Rust Version:** 1.77 (`rustc --version`) 
- **Key Libraries:**  
  - `regex`  
  - `ctrlc` 
- **Notes:** Rust experiments can be compiled with no optimization for raw timing analysis:
```bash
rustc -C opt-level=0 <filename>.rs
```

## Requirements

This project requires Python 3.9.0
All dependencies are listed in the `requirements.txt` file.

To install them, run:

```bash
pip install -r requirements.txt
```

## Usage
Each experiment is self-contained within its own directory.
You may find a README.md file inside a directory that explains how to run the corresponding experiment.
If a directory does not contain a README, check the top of the experiment script — each file includes a header with usage instructions and details on how to execute it.

## License

MIT License

## Authors
* Mohammad Mari - <mohammad.mari@griffithuni.edu.au>
* Lian Wen - <l.wen@griffith.edu.au>
