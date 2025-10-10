# Python Binary Extension with Cython

This project demonstrates how to create a Python binary extension module using [Cython](https://cython.org), and/or compile it into binary using [PyOxidizer](https://github.com/indygreg/PyOxidizer)

---

## Prerequisites

Before building, ensure the following tools are installed:

* **Python 3.9.0** (with `pip`)
* **Cython** (`pip install cython`)

---

## Steps Performed

### 1. Execute setup.py

```bash
python setup.py build_ext --inplace
```

### 2. use the provided tester `tester.py` to execute the compiled loop
```bash
python tester.py
```

# Create executable using PyOxidizer

1. Within the project folder initialize PyOxidizer config file:
```bash
pyoxidizer init-config-file <<project-path>>
```
2. Build the project with PyOxidizer
```bash
pyoxidizer build
```

Output binary will be in the generated `build` folder

## License

MIT License
