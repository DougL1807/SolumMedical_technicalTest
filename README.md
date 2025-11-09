# Solum Medical - Technical Assessment

Technical test submission for Web Developer position.

## Quick Start

Each question is in a separate folder with its own README:

```
A/  - Mystic Waves (algorithmic problem)
B/  - CargoCraft Fleet (optimization problem)
C/  - Login Page (React application)
```

Navigate to each folder and follow the README instructions to run the code.

## Question A: Mystic Waves

**Problem:** Calculate total energy from alternating wave sequences.

**Solution:** Mathematical pattern recognition - O(1) time complexity.

**How to run:**

```bash
cd QuestionA
python mystic_waves.py
# Or run input.txt:
python mystic_waves.py < input.txt    # Mac/Linux
Get-Content input.txt | python mystic_waves.py   # Windowss
# Or run tests:
pytest test_mystic_waves.py
```

**Key features:**

- Handles edge cases (n=1, n=2)
- Efficient algorithm (no loops needed)
- Comprehensive test coverage

## Question B: CargoCraft Fleet

**Problem:** Find min/max number of crafts given total propulsion units.

**Solution:** Linear Diophantine equation optimization for inputs up to 10^18.

**How to run:**

```bash
cd QuestionB
python cargocraft.py
# Or run input.txt:
python cargocraft.py < input.txt # Mac/Linux
Get-Content input.txt | python cargocraft.py # Windows
# Or run tests:
pytest test_cargocraft.py
```

**Key features:**

- Handles large numbers (10^18) within 1 second time limit
- Mathematical optimization (no brute force)
- Edge case handling (impossible scenarios)

## Question C: Login Page

**Problem:** Build secure login page with validation.

**Solution:** React application with comprehensive validation and testing.

**How to run:**

```bash
cd QuestionC
npm install
npm run dev
# Open http://localhost:5173

# Run tests:
npm test
```

**Test accounts:**

- doctor@solum.com / Test123!
- admin@solum.com / Admin2024#
- test@example.com / Pass123$

**Key features:**

- Email and password validation with specific error messages
- Responsive design (mobile + desktop)
- 23 unit tests with 100% pass rate
- Clean, commented code

## Technical Highlights

### Code Quality

- Clear naming conventions and file structure
- Comprehensive comments explaining logic
- Error handling for edge cases
- Input validation and sanitization

### Testing

- Question A: 29 test cases covering all scenarios
- Question B: 26 test cases including edge cases and large numbers
- Question C: 23 unit tests covering all features
- All tests passing

### Documentation

- Each question has detailed README
- Clear installation and usage instructions
- Example inputs and outputs provided
- Test account information included

## Project Structure

```
solum-technical-test/
├── README.md          # This file
├── A/
│   ├── mystic_waves.py
│   ├── test_mystic_waves.py
│   ├── input.txt
│   └── README.md
│
├── B/
│   ├── cargocraft.py
│   ├── test_cargocraft.py
│   ├── input.txt
│   └── README.md
│
└── C/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   ├── main.jsx
    │   └── test/
    │       ├── App.test.jsx
    │       └── setup.js
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── vite.config.js
    └── README.md
```

## Requirements Met

### Question A

- ✓ Accepts multiple test cases
- ✓ Handles constraints (1 ≤ x, n ≤ 10)
- ✓ Correct output format
- ✓ Clean, readable code

### Question B

- ✓ Handles inputs up to 10^18
- ✓ Runs within 1 second time limit
- ✓ Returns -1 for impossible cases
- ✓ Correct min/max calculation

### Question C

- ✓ Email validation (format + existence)
- ✓ Password validation (length + complexity)
- ✓ Login/logout functionality
- ✓ Responsive design
- ✓ Clear error messages
- ✓ Modern, professional styling

## Development Approach

All solutions prioritize:

1. **Correctness** - Handles all test cases including edge cases
2. **Efficiency** - Optimized algorithms meet performance requirements
3. **Maintainability** - Clean code with clear documentation
4. **Quality** - Comprehensive testing ensures reliability

## Notes

- All code is production-ready with error handling
- Tests can be run independently to verify functionality
- Each solution is self-contained in its folder
- No external dependencies required except those in package.json (Question C)

## Contact

Jingdi Lin
Submission Date: [09/Nov/2025]

---

Thank you for reviewing this submission.
