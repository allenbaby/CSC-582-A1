# CSC 582 Assignment #1: Four-Bit Adder

This project implements an object-oriented four-bit adder in Python using the
required assignment structure. Its circuit is composed exclusively from AND, OR,
and NAND primitive objects.

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

`Xor2` contains two NANDs used as NOTs, two ANDs, and one OR. `HalfAdder` contains
one XOR and one AND. `FullAdder` contains two half-adders and one OR. The four-bit
adder contains four full-adders, with each carry-out feeding the next carry-in.
All composites inherit directly from `AbstractDevice`.

## Try the Public Adder

From the project root, start Python with `PYTHONPATH=source .venv/bin/python`, then:

```python
from FourBitAdder.FourBitAdder import FourBitAdder

adder = FourBitAdder()
adder.setA(15)
adder.setB(0)
adder.setCin(1)
print(adder.getSum(), adder.getCout())  # 0 1: binary result 10000
```

`setA` and `setB` take integers from 0 through 15; `setCin` takes 0 or 1.
`getSum` returns the lower four result bits as an integer, and `getCout` returns
the fifth bit. Each setter completes the entire update before returning.
The caller must supply inputs in these ranges; invalid-input handling is not
specified by the starter and is not added here.

For a single gate, import `AND` from `FourBitAdder.intern.LogicGates`, construct
`AND(1)`, and call `setIn1` and `setIn2` with one bit each. The constructor number
is a debugging ID, not an input or a bit position.

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

Primitive and XOR tests use fixed truth tables and loops. Adder tests use
independent integer addition for expectations, as the starter specifies;
production composites never calculate a sum arithmetically. Black, pytest, and
pdoc are project tool choices, not tools specifically mandated by the professor.

The starter leaves the smaller composites' exact accessor names open. This
translation uses `setA`, `setB`, `getA`, and `getB`; XOR has `getOut`, half-adder
has `getSum` and `getCarry`, and full-adder adds `setCin`, `getCin`, and `getCout`.
The four-bit methods preserve the provided test contract. Its bit lists store
bit zero first; binary string conversions only encode and decode pins, while
full-adder objects compute the outputs. The public module re-exports the internal
class, avoiding a duplicate wrapper class.

The base declares the shared update contract; each concrete setter enforces it
by storing its input and calling `self.update()`. Each composite's update wires
its particular components in dependency order. No generic event scheduler is
needed for this synchronous circuit. Intermediate internal outputs can change
several times during an update; outputs are settled when the public setter
returns. Composite constructors call update to settle their internal NANDs.

## Tests and Design

Run `.venv/bin/python -m pytest -v` from the project root. There are 29 test
cases, with loops inside the exhaustive tests. The four-bit suite covers all
16 × 16 × 2 = 512 additions, independent setter changes, carry propagation
through every stage, and independent adder instances. Lower-level tests cover
construction, truth tables, required component ownership, and update dispatch.

The plain-text Mermaid diagrams are:

- `design/class_diagram.mmd`: all nine production classes, inheritance, and
  component names and multiplicities.
- `design/input_update_sequence.mmd`: a single XOR input change down through
  primitive setter/update calls.
- `design/addition_sequence.mmd`: setting operands and propagating carry for
  15 + 0 + 1, from bit zero to bit three.

The sequence diagrams were explicitly authored from the implementation with
disclosed AI assistance; they were not generated by pdoc. Keep the `.mmd` files
in the submission, even if also viewing or exporting rendered diagrams.

To explain the design in class, trace `setCin(1)` from the public adder: the
four-bit update visits each full-adder; each full-adder settles two half-adders
and a carry OR; each half-adder settles an XOR and a carry AND; each XOR wires
five primitives. Only primitive update methods apply Boolean operations.

## Submission

Run Black in default mode (`black source tests`) before each commit, run the
tests, and regenerate documentation after code/docstring changes. Commit the
generated `doc/` files along with source, tests, diagrams, and the current
`AI_USAGE.md`. The assignment requires at least 15 meaningful commits across
at least four distinct days; do not fabricate, backdate, or pad the history.

Run `shasum -a 256 munger.py`. The official digest is
`5aaae171f2ee60b3e65243858cfddf727db996bb21077604eddefd9dda93a3e6`.
Never modify the bundler, including with a formatter.

From the repository root, run `python3 munger.py`, enter your actual student ID
and name, and choose `1` for take-home. Inspect the resulting
`<ID>_<Name>_takehome_bundle.txt`: check the history, source files, diagrams, and
`FILES NOT BUNDLED` section. Generated documentation is counted in the tree
rather than embedded; hidden editor settings are intentionally excluded.
Upload through the take-home form provided by the professor. The in-class bundle
uses option `2` and a separate form. A rehearsal with placeholder identity is
only a bundler check and must not be submitted.
