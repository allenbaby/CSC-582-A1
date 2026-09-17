# CSC 582 Assignment #1: Four-Bit Adder

This project will implement an object-oriented four-bit adder in Python using the required assignment structure. Implementation is being completed incrementally through meaningful Git commits.

## Python Version and Setup

Use Python 3. Create and activate a virtual environment, then install the development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Development Commands

Format the source and test directories with Black:

```bash
black source tests
```

Run the pytest suite:

```bash
pytest
```

Generate documentation for the FourBitAdder package:

```bash
PYTHONPATH=source pdoc -o doc FourBitAdder
```

Open `doc/index.html` to browse the generated documentation. Keep the generated
files under `doc/` in Git as required by the assignment.

## Current Implementation

The primitive foundation implements `AbstractDevice`, `AbstractGate`, `AND`,
`OR`, and `NAND`. All concrete gates require an integer `idNumber` when created.
Their input setters call `update()` before returning. Per the provided
construction tests, every gate starts with all pins at zero: a new NAND's output
becomes one when either zero input is set, not during construction.

`Xor2`, `HalfAdder`, `FullAdder`, and the public four-bit adder remain to be built
after the required primitive-foundation commit. The current class diagram in
`design/class_diagram.mmd` covers implemented classes only.

## Python Translation Decisions

The required `source/` directory and CamelCase filenames and method names are
preserved from the starter instead of adopting Python's usual naming conventions.
`pytest` adds `source/` to its import path through `pyproject.toml`; documentation
generation uses `PYTHONPATH=source` for the same package imports. The workspace's
Pylance settings configure editor import resolution separately.

`ABC` and `abstractmethod` require concrete subclasses to implement `update()`.
The gate setters enforce when it is called. Python has no enforced protected
visibility, so the starter's `in1`, `in2`, `out`, `id`, and `repr()` names are
preserved and intended for internal use. No no-op destructor is needed in Python.
Inputs are bits (integers 0 or 1); the starter specifies no invalid-input policy.

The test expectations use fixed truth tables and loops. This preserves the
starter's expected results without using Boolean expressions outside the three
primitive `update()` methods. Black, pytest, and pdoc are project tool choices,
not tools specifically mandated by the professor.
