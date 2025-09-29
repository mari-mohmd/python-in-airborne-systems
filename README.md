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
Python is a widely adopted programming language celebrated for its ease of use, dynamic typing, and strong community support. Despite these advantages, Python presents challenges when considered for safety-critical applications, notably those in airborne systems. Concerns arise from performance limitations, limited compile-time checking, and dynamic features that may impact reliability in environments where failures can have severe consequences. Airborne systems, with their stringent safety requirements, provide a context in which these challenges can be critically examined. This study evaluates Python’s alignment with the objectives defined in DO-178C (Software Considerations in Airborne Systems and Equipment Certification). By analyzing Python’s core characteristics
against these rigorous standards, we highlight potential compliance gaps and practical challenges that may hinder its use in safety-critical contexts.
In addition, we perform a comparative analysis between Python and Rust—a modern systems programming language noted for its safety guarantees and performance. Rust was selected not as a replacement for established baselines such as Ada, C, and C++, but as a complementary point of comparison illustrating how a newer, safety-oriented compiled language contrasts with Python’s interpreted model. Our findings indicate that Python lacks compile-time error checking, exhibits delayed signal handling,
and has limited optimization capabilities, which together may affect its performance and reliability. Potential enhancements such as Just-In-Time (JIT) compilation, advanced static analysis, and robust type-checking tools are recommended to mitigate these issues. Overall, our study emphasizes both the
strengths and limitations of Python and suggests pathways to improve its viability for safety-critical use.

---

## Repository Structure
```plaintext

├── Python/
│   ├── Performance/
│   |   ├── bounded_latency/                   
│   |   │   ├── bounded_latency_single_thread.py
│   |   │   ├── bounded_latency_multi_thread.py
│   |   │   └── bounded_latency_multi_process.py
│   |   │
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
│   |   ├── signle_handle_re_test.py
|
├── Rust/
│   └── performance/
│       └── bounded_latency/                   
│           ├── bounded_latency_single_thread.rs
│           └── bounded_latency_multi_thread.rs
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
- **Python Version:** 3.12 
- **Key Libraries:**  
  - `multiprocessing` (standard library)  
  - `threading` (standard library)  
  - `numba` for JIT compilation experiments  

### Rust Experiments
- **Rust Version:** 1.77 (`rustc --version`)  
- **Notes:** Rust experiments can be compiled with no optimization for raw timing analysis:
```bash
rustc -C opt-level=0 <filename>.rs
