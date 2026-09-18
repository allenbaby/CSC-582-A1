# CSC 582 Assignment #1: Four-Bit Adder

A four-bit binary adder implemented in Python using object composition. The
circuit uses AND, OR, and NAND primitives to build XOR gates, half-adders,
full-adders, and a four-stage ripple-carry adder.

## Setup

Run these commands from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

Start a Python session with the source directory on the import path:

```bash
PYTHONPATH=source .venv/bin/python
```

```python
from FourBitAdder.FourBitAdder import FourBitAdder

adder = FourBitAdder()
adder.setA(15)
adder.setB(0)
adder.setCin(1)
print(adder.getSum(), adder.getCout())  # 0 1: binary result 10000
```

- `setA(value)` and `setB(value)` accept integers from 0 through 15.
- `setCin(value)` accepts a carry-in bit of 0 or 1.
- `getSum()` returns the lower four result bits as an integer.
- `getCout()` returns the carry-out bit.

Each input setter recomputes the outputs before returning. Inputs must be within
these ranges; input validation is not implemented.

Individual gates accept one bit per input through `setIn1` and `setIn2`.
For example, `AND(1)` creates an AND gate with debugging ID `1AND`. The ID does
not specify an input value or bit position.

## Architecture

| Class | Responsibility |
| --- | --- |
| `AbstractDevice` | Declares the abstract `update()` contract. |
| `AbstractGate` | Stores two inputs and one output; input setters call `update()`. |
| `AND`, `OR`, `NAND` | Implement the primitive Boolean operations. |
| `Xor2` | Contains two NAND inverters, two AND gates, and one OR gate. |
| `HalfAdder` | Contains one XOR for sum and one AND for carry. |
| `FullAdder` | Contains two half-adders and one OR to combine their carries. |
| `FourBitAdder` | Contains four full-adders connected in ripple-carry order. |

The primitives inherit from `AbstractGate`. All composites inherit directly from
`AbstractDevice`. Each composite passes inputs through its components in
dependency order and reads their outputs. Only the three primitive `update()`
methods implement Boolean operations.

All primitive pins start at zero, matching the starter construction contract.
A new NAND's output becomes one after either zero-valued input is set.
Composite constructors call `update()` to settle their internal components.
During an update, internal outputs may change several times; the public outputs
are settled when the setter returns.

The four-bit adder stores its bit lists least-significant-bit first. Binary
string conversions encode and decode pin values; full-adder objects perform the
addition. The public module re-exports the implementation from `intern/`.

## Project Layout and Python Conventions

- `source/FourBitAdder/FourBitAdder.py`: public entry point.
- `source/FourBitAdder/intern/`: implementation classes.
- `tests/pytest/`: automated tests.
- `design/`: plain-text Mermaid diagrams.
- `doc/`: generated API documentation.
- `AI_USAGE.md`: AI assistance disclosure.

The project preserves the assignment's `source/` layout and the starter's
CamelCase filenames and method names instead of Python's usual naming
conventions. `pytest` configures its import path through `pyproject.toml`;
manual sessions and documentation generation use `PYTHONPATH=source`.
Pylance uses the workspace settings for editor import resolution.

`ABC` and `abstractmethod` require concrete devices to implement `update()`;
the input setters enforce when it runs. Python does not enforce protected
visibility. Pin fields and component objects are intended for internal use;
callers should use setters and getters. No no-op destructor is needed.

The smaller composites use `setA`, `setB`, `getA`, and `getB`. XOR exposes
`getOut`; the half-adder exposes `getSum` and `getCarry`; the full-adder also
provides `setCin`, `getCin`, and `getCout`. These names are Python implementation
choices where the starter leaves the API open. The four-bit adder preserves
the provided test contract.

## Tests and Formatting

Run the complete test suite:

```bash
pytest -v
```

Tests cover construction, truth tables, component ownership, and immediate
updates after input changes. The four-bit suite checks all 512 combinations
of two four-bit operands and carry-in, carry propagation, and instance isolation.
Primitive and XOR expectations use fixed truth tables. Adder expectations use
independent integer addition in tests.

Format all source and test files before committing:

```bash
black source tests
```

Black, pytest, and pdoc are the selected Python development tools.

## Documentation and Diagrams

Generate the API documentation:

```bash
PYTHONPATH=source pdoc -o doc FourBitAdder
```

Open it on macOS:

```bash
open doc/index.html
```

Commit the generated files under `doc/`. Regenerate them after changing code or
docstrings.

The Mermaid diagrams describe the implementation:

- `design/class_diagram.mmd`: all nine production classes, inheritance, and
  composition relationships with component names and multiplicities.
- `design/input_update_sequence.mmd`: an XOR input change and the resulting
  primitive setter and update calls.
- `design/addition_sequence.mmd`: a complete 15 + 0 + 1 addition, including carry
  propagation from bit zero through bit three.

Keep the `.mmd` sources in the submission alongside any rendered exports.
AI assistance with code and documentation is recorded in `AI_USAGE.md`.

## Submission

The assignment requires at least 15 meaningful commits across four distinct
days, formatting before each commit, generated documentation, and a current
AI disclosure log.

Verify the official bundler before use:

```bash
shasum -a 256 munger.py
```

Expected SHA-256:

```text
5aaae171f2ee60b3e65243858cfddf727db996bb21077604eddefd9dda93a3e6
```

Keep `munger.py` unmodified and exclude it from formatting commands.

Generate the submission from the repository root:

```bash
python3 munger.py
```

Enter the student ID and name, then select `1` for the take-home bundle or `2`
for the in-class bundle. Inspect the generated file's history, source contents,
diagrams, and `FILES NOT BUNDLED` section before uploading to the corresponding
submission form. Generated documentation is counted in the tree rather than
embedded in the bundle. Hidden editor settings are excluded.
