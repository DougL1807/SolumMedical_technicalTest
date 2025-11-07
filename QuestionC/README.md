# Solum Medical - Login Page

A professional login page implementation for Solum Medical's technical assessment (Question C).

## Project Description

This is a frontend-only login page built with React that demonstrates:

- Secure email and password validation
- User-friendly error messages
- Responsive design for desktop and mobile
- Professional UI/UX suitable for healthcare software
- Clean, maintainable code with comprehensive comments

## Tech Stack

- **Framework**: React 18.3.1
- **Build Tool**: Vite 5.3.1
- **Language**: JavaScript (ES6+)
- **Styling**: Pure CSS3
- **No external UI libraries** - All components are custom-built

## Installation & Setup

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn package manager

### Steps

1. **Navigate to the project directory**

   ```bash
   cd C
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start development server**

   ```bash
   npm run dev
   ```

4. **Open in browser**
   - The app will run at `http://localhost:5173`
   - Open this URL in your web browser

## Test Accounts

Use any of these credentials to test the login functionality:

| Email              | Password     |
| ------------------ | ------------ |
| `doctor@solum.com` | `Test123!`   |
| `admin@solum.com`  | `Admin2024#` |
| `test@example.com` | `Pass123$`   |

## Features

### ✅ Email Validation

- Cannot be empty
- Must follow valid email format (contains @ and domain)
- Must exist in the system (hardcoded valid emails)
- Clear error message if email not found

### ✅ Password Validation

- Length: 8-16 characters
- Must contain:
  - At least one **uppercase letter** (A-Z)
  - At least one **lowercase letter** (a-z)
  - At least one **number** (0-9)
  - At least one **special character** (!@#$%^&\*()\_+-=[]{}|;:'",.<>?/)
- Shows specific requirements if validation fails
- Password visibility toggle button

### ✅ Login Process

- Form validation on submit
- Loading state during login (prevents double-click)
- Disabled inputs during processing
- Credential matching verification

### ✅ Post-Login Experience

- Welcome message with user's email
- Clean logout functionality
- Returns to login page on logout

### ✅ User Experience

- Responsive design (mobile, tablet, desktop)
- Clear, specific error messages
- Smooth animations and transitions
- High contrast for readability
- Accessible form controls
- "Forgot password?" link (placeholder)

## Validation Rules Summary

### Email Rules:

1. Required field (cannot be empty)
2. Valid format: `example@domain.com`
3. Must exist in system's user list

### Password Rules:

1. Length: 8-16 characters
2. Complexity requirements:
   - Uppercase: ✓
   - Lowercase: ✓
   - Number: ✓
   - Special character: ✓

## 🎨 Design Principles

This login page follows healthcare software best practices:

- **Clarity**: Error messages are specific and actionable
- **Simplicity**: Clean interface with minimal distractions
- **Safety**: Prevents common user errors (double submission, invalid input)
- **Accessibility**: Proper labels, ARIA attributes, high contrast
- **Professionalism**: Modern, trustworthy design suitable for medical context

## 🔧 Build for Production

```bash
npm run build
```

This creates an optimized production build in the `dist/` folder.

## 📝 Notes

- All validation happens on the frontend (no backend required)
- User credentials are hardcoded in `App.jsx` for demonstration purposes
- In a production environment, authentication should be handled by a secure backend API
- No actual data is stored or transmitted

## 🐛 Troubleshooting

**Port already in use?**

```bash
# Vite will automatically try the next available port
# Or specify a different port:
npm run dev -- --port 3000
```

**Dependencies not installing?**

```bash
# Clear npm cache and reinstall
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

## 📞 Contact

For questions about this implementation, please refer to the technical assessment instructions.

---

**Developed for Solum Medical Technical Assessment**  
_Question C - Frontend Test: Login Page_
