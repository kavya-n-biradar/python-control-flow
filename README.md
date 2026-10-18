# Python Control Flow: Conditional Statements and Loops

Python conditionals and loops practice for the CodeMore Python Programming Internship (Week 1, Task 1). The project uses `if / elif / else` and `for` / `while` loops to solve basic logic problems, with a written report and terminal screenshots.

## Project Structure

```
python-control-flow/
├── README.md
├── .gitignore
├── src/
│   ├── number_checks.py
│   └── loop_operations.py
└── docs/
    ├── control_flow_report.pdf
    └── screenshots/
```

## Requirements

- Python 3.8 or newer. Check your version with `python --version`.
- No external libraries are needed.

## Setup and How to Run

1. Clone the repository:
```bash
   git clone https://github.com/kavya-n-biradar/python-control-flow.git
   cd python-control-flow
```
2. Run the number classification script:
```bash
   python src/number_checks.py
```
3. Run the loop operations script:
```bash
   python src/loop_operations.py
```

On macOS or Linux, use `python3` instead of `python` if needed.

## What Each Script Does

### `src/number_checks.py`
Takes an integer from the user and prints whether it is **even or odd**, and whether it is **positive, negative or zero**. Invalid input such as text is handled with `try / except`, so the program does not crash.

### `src/loop_operations.py`
Runs three parts in order:
1. **Multiplication table** of a number from 1 to 10 (`for` loop).
2. **Sum of the first N natural numbers** (`while` loop).
3. **Right-angled triangle** of asterisks with a user-chosen number of rows (`for` loop).

Zero or negative values for N and the number of rows print an explanatory message.

## Example Output

```
Enter an integer: -5
The number is odd.
The number is negative.
```

```
Enter the number of rows: 4
*
**
***
****
```

## Documentation

The full report is in [`docs/control_flow_report.pdf`](docs/control_flow_report.pdf). It explains the logic of each script, compares `for` and `while` loops, and lists the edge cases tested. Terminal screenshots are in [`docs/screenshots/`](docs/screenshots/).

## What I Learned

- How `if / elif / else` lets a program choose between several paths.
- When to use a `for` loop (known number of repeats) and a `while` loop (repeat until a condition changes).
- Why `range()` stops one before its end value.
- How to handle edge cases such as zero, negative numbers and invalid input.
- How to organise a project and make small, clear Git commits.

## Author

Kavya Biradar