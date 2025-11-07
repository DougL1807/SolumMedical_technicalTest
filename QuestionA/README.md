# Question A: Mystic Waves

## Problem Description

A mage casts `n` waves of alternating energy: `x, -x, x, -x, ...`

Calculate the total magical energy after all `n` waves.

### Input Format

```
t                    # Number of test cases (1 ≤ t ≤ 100)
x₁ n₁               # Energy value x (x ≥ 1), waves n (1 ≤ n ≤ 10)
x₂ n₂
...
```

### Output Format

```
result₁             # Total energy for each test case
result₂
...
```

### Example

**Input:**

```
4
1 4
2 5
3 6
4 7
```

**Output:**

```
0
2
0
4
```

---

## Solution Algorithm

Simple mathematical pattern:

- **Even n**: Wave pairs cancel out → result = `0`
- **Odd n**: One positive wave remains → result = `x`

**Time Complexity:** O(1) per test case  
**Space Complexity:** O(1)

---

## How to Run

### Prerequisites

- Python 3.7+
- pytest (optional, for testing)

### Quick Run

```bash
Get-Content input.txt | python mystic_waves.py
```

Expected output:

```
0
2
0
4
```

## Testing

### Quick Verification

```bash
Get-Content input.txt | python mystic_waves.py
```

### Comprehensive Testing

```bash
pytest test_mystic_waves.py -v
```

**Test Coverage:**

- ✅ Official test cases
- ✅ Boundary validation (x ≥ 1, 1 ≤ n ≤ 10, 1 ≤ t ≤ 100)
- ✅ Type checking and error handling
- ✅ Edge cases with large values

**Result:** 29/29 tests passing

---

## Code Features

### Input Validation

- Type checking (integers only)
- Range validation with clear error messages
- Comprehensive boundary checking

### Modular Design

- `calculate_total_energy(x, n)` - Core algorithm
- `solve_test_cases(test_cases)` - Batch processing
- `read_input_from_stdin()` - Input handling
- `main()` - Entry point

### Medical Software Standards

- Strict input validation
- Clear error messages
- Comprehensive test coverage
- Well-documented code

---

## Author

Jingdi Lin  
November 2025  
Solum Medical Technical Test
