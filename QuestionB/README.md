# CargoCraft Fleet Calculator

Solum Medical Technical Test - Question B

## Requirements

- Python 3.7 or higher
- pytest (optional, for running tests)

---

## Installation

No installation required. The program is self-contained.

To run tests:

```bash
pip install pytest
```

---

## Usage

### Method 1: Quick Test (Single Number)

Run the program and enter just one number:

```bash
python cargocraft.py
```

Then enter:

```
1
24
```

Press ENTER then Ctrl+Z then Enter (Windows) or Ctrl+D (Mac/Linux).

Output:

```
4 6
```

### Method 2: Batch Testing (Multiple Test Cases)

Run the program and enter multiple test cases:

```bash
python cargocraft.py
```

Then enter:

```
4
4
7
24
998244353998244352
```

First line (4) indicates the number of test cases.
Press ENTER then Ctrl+Z then Enter (Windows) or Ctrl+D (Mac/Linux).

Output:

```
1 1
-1
4 6
166374058999707392 249561088499561088
```

### Method 3: Using Input File

Created a file named `input.txt`:

```
4
4
7
24
998244353998244352
```

Run:

```bash
# Windows PowerShell
Get-Content input.txt | python cargocraft.py

# Mac/Linux/Unix
python3 cargocraft.py < input.txt
```

### Method 4: Import as Module

Use the functions in your own code:

```python
from cargocraft import calculate_fleet_size

min_crafts, max_crafts = calculate_fleet_size(24)
print(f"Minimum: {min_crafts}, Maximum: {max_crafts}")
```

---

## Running Tests

Run all tests:

```bash
pytest test_cargocraft.py -v
```

Run specific test class:

```bash
pytest test_cargocraft.py::TestBasicFunctionality -v
```

Expected result: 26 tests pass

---

## Algorithm

### Mathematical Approach

Given equation: 4a + 6b = n (where a = Type A crafts, b = Type B crafts)

Key insight: n must be even (both 4 and 6 are even numbers)

### Calculating Minimum Crafts

Strategy: Maximize Type B usage (6 units per craft)

```
If n % 6 == 0: Use only Type B crafts
               Result: n / 6 crafts

If n % 6 == 2: Use 2 Type A crafts (8 units) + remaining Type B
               Result: 2 + (n - 8) / 6 crafts

If n % 6 == 4: Use 1 Type A craft (4 units) + remaining Type B
               Result: 1 + (n - 4) / 6 crafts
```

### Calculating Maximum Crafts

Strategy: Maximize Type A usage (4 units per craft)

```
If n % 4 == 0: Use only Type A crafts
               Result: n / 4 crafts

If n % 4 == 2: Use 1 Type B craft (6 units) + remaining Type A
               Result: 1 + (n - 6) / 4 crafts
```

### Performance

- Time Complexity: O(1) - direct mathematical calculation
- Space Complexity: O(1) - uses only a few integer variables
- Handles inputs up to 10^18 instantly

---

## Input Validation

### Valid Inputs

- Positive integers
- Even numbers only
- Minimum value: 4
- Maximum value: 10^18

### Invalid Inputs (Returns -1)

- Odd numbers (e.g., 7, 13, 99)
- Numbers less than 4 (e.g., 0, 2)
- Negative numbers

---

## Test Cases

| Input              | Output                                | Explanation                      |
| ------------------ | ------------------------------------- | -------------------------------- |
| 4                  | 1 1                                   | One Type A craft (4 × 1 = 4)     |
| 6                  | 1 1                                   | One Type B craft (6 × 1 = 6)     |
| 7                  | -1                                    | Odd number, impossible           |
| 10                 | 2 2                                   | 1 Type A + 1 Type B (4 + 6 = 10) |
| 24                 | 4 6                                   | Min: 4 Type B, Max: 6 Type A     |
| 998244353998244352 | 166374058999707392 249561088499561088 | Large number test                |

---

## File Structure

```
QuestionB/
├── cargocraft.py          # Main solution (approximately 300 lines)
├── test_cargocraft.py     # Test suite (approximately 200 lines)
├── README.md              # This file
└── input.txt              # Optional: sample input for testing
```

---

## Code Structure

The solution is organized into modular functions:

**Core Functions:**

- `calculate_fleet_size(n)` - Main function that returns (min, max) tuple
- `calculate_minimum_crafts(n)` - Computes minimum number of crafts
- `calculate_maximum_crafts(n)` - Computes maximum number of crafts

**Helper Functions:**

- `solve_single_case(n)` - Handles single test case, returns formatted string
- `process_batch_input(input_data)` - Processes multiple test cases
- `main()` - Command-line interface

---

## Error Handling

The program validates all inputs and provides clear error messages:

```
Invalid: Odd number
Error: "Cannot form 7 units (must be even)"

Invalid: Negative number
Error: "Propulsion units cannot be negative: -5"

Invalid: Too small
Error: "Cannot form 2 units (minimum is 4)"

Invalid: Zero
Error: "Cannot have zero propulsion units"
```

---

## Design Principles

### 1. Input Validation

Every input is validated before processing. The program checks for:

- Positive numbers
- Even numbers
- Valid range (1 to 10^18)
- Proper format

### 2. Mathematical Optimization

Uses direct calculation instead of iteration. This ensures:

- Constant time complexity
- Handles extremely large numbers
- Meets 1-second time limit requirement

### 3. Clear Error Messages

Error messages specify exactly what went wrong and why:

- Not just "Invalid input"
- Explains the requirement (e.g., "must be even")
- Helps users understand the problem

### 4. Modular Code

Each function has a single responsibility:

- Easy to test
- Easy to maintain
- Easy to reuse

### 5. Comprehensive Testing

Test suite covers:

- Basic functionality
- Edge cases (boundary values)
- Large numbers (up to 10^18)
- Invalid inputs
- All problem examples

---

## Performance Specifications

### Time Requirements

- Problem constraint: 1 second per test
- Actual performance: < 1 millisecond per test
- Test suite: 1000 cases in < 10 milliseconds

### Memory Requirements

- Problem constraint: 256 megabytes
- Actual usage: < 1 kilobyte per calculation
- Integer storage (10^18): approximately 36 bytes

---

## Troubleshooting

**Problem: "Python was not found"**

Windows: Use `python` instead of `python3`

```bash
python cargocraft.py
```

Mac/Linux: Use `python3`

```bash
python3 cargocraft.py
```

**Problem: "Expected N test cases, but got M"**

Solution: In batch mode, first line must be the count of test cases.

Correct format:

```
3        ← Number of test cases
4        ← Test case 1
10       ← Test case 2
24       ← Test case 3
```

**Problem: "No module named pytest"**

Solution: Install pytest

```bash
pip install pytest
```

**Problem: Import errors when using as module**

Solution: Ensure both files are in the same directory or add directory to Python path.

---

## Constraints

As specified in the problem statement:

- Time limit: 1 second per test
- Memory limit: 256 megabytes
- Input range: 1 ≤ n ≤ 10^18
- Test cases: 1 ≤ t ≤ 1000

All constraints are met by this implementation.
