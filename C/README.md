# Login Page - Question C

A secure login page with comprehensive validation for Solum Medical technical assessment.

## Quick Start

### Installation

```bash
cd C
npm install
npm run dev
```

The application will open at `http://localhost:5173`

### Running Tests

```bash
npm test              # Run all tests
npm run test:ui       # Open test UI
```

## Test Accounts

Use these credentials to test the login:

```
doctor@solum.com / Test123!
admin@solum.com / Admin2024#
test@example.com / Pass123$
```

## Features

### Email Validation

- Required field
- Must be valid format (user@domain.com)
- Must exist in the system
- Shows specific error messages

### Password Validation

Password must meet all requirements:

- 8-16 characters in length
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one number (0-9)
- At least one special character (!@#$%^&\* etc.)

### Security Features

- Password visibility toggle
- Form disabled during submission to prevent duplicate requests
- Input sanitization and validation
- Clear error messages without exposing sensitive information

### User Experience

- Responsive design for mobile and desktop
- Loading state during login
- Smooth transitions and animations
- High contrast for readability
- Accessible form controls with proper labels

## Validation Rules

### Email

1. Cannot be empty
2. Must contain @ and domain
3. Must be registered in the system

### Password

1. Length between 8-16 characters
2. Must include:
   - Uppercase letter
   - Lowercase letter
   - Number
   - Special character

If any requirement is missing, a specific error message will explain what's needed.

## Technical Details

### Tech Stack

- React 18.3.1
- Vite 5.3.1
- Pure CSS (no UI libraries)
- Vitest + React Testing Library for testing

### Project Structure

```
C/
├── src/
│   ├── App.jsx          # Main component
│   ├── App.css          # Styles
│   ├── main.jsx         # Entry point
│   └── test/
│       ├── setup.js     # Test configuration
│       └── App.test.jsx # Test suite (23 tests)
├── index.html           # HTML template
├── package.json         # Dependencies
├── package-lock.json    # Lockfile
├── .gitignore           # Git ignored files
├── vite.config.js       # Vite configuration
└── README.md            # This file
```

### Test Coverage

The application includes 23 unit tests covering:

- Email validation (format, existence, empty state)
- Password validation (length, complexity requirements)
- Login process (success and failure)
- Logout functionality
- UI interactions (password toggle, form submission)
- Edge cases (whitespace, multiple errors, error clearing)

## How It Works

### Login Flow

1. User enters email and password
2. Form validates on submit
3. If invalid: shows specific error messages
4. If valid: simulates login with loading state
5. On success: displays welcome page with user email
6. User can logout to return to login page

### Validation Logic

- Email checked against predefined list of valid users
- Password validated against complexity requirements
- Credentials matched only if both email exists and password is correct
- All validation happens on frontend (no backend required)

## Error Messages

The system provides clear, actionable error messages:

**Email errors:**

- "Email address is required"
- "Please enter a valid email address"
- "This email address is not registered in our system"

**Password errors:**

- "Password is required"
- "Password must contain [specific requirements]"
- "Incorrect password. Please try again"

## Development

### Build for Production

```bash
npm run build
```

Output will be in the `dist/` directory.

### Linting

```bash
npm run lint
```

## Browser Support

Tested and working on:

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

### Port already in use

Vite will automatically use the next available port. Or specify a port:

```bash
npm run dev -- --port 3000
```

### Dependencies won't install

```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Tests failing

Make sure all dependencies are installed:

```bash
npm install
npm test
```

## Notes

- All validation happens client-side for this demo
- User credentials are hardcoded in App.jsx
- In production, authentication should use a secure backend API
- No data is stored or transmitted
