import React, { useState } from "react";
import "./App.css";

/**
 * Hardcoded valid user credentials
 * In a real application, these should be stored in a backend database
 */
const VALID_USERS = [
  { email: "doctor@solum.com", password: "Test123!" },
  { email: "admin@solum.com", password: "Admin2024#" },
  { email: "test@example.com", password: "Pass123$" },
];

function App() {
  // ===== State Management =====
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [loggedInEmail, setLoggedInEmail] = useState("");

  // ===== Validation Functions =====

  /**
   * Validate email format
   * @param {string} email - Email to validate
   * @returns {boolean} - Whether the format is valid
   */
  const isValidEmailFormat = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  /**
   * Check if email exists in valid users list
   * @param {string} email - Email to check
   * @returns {boolean} - Whether the email exists
   */
  const emailExists = (email) => {
    return VALID_USERS.some((user) => user.email === email);
  };

  /**
   * Validate password strength
   * Requirements: 8-16 characters, at least one uppercase, one lowercase, one number, one symbol
   * @param {string} password - Password to validate
   * @returns {object} - Object containing isValid and message
   */
  const validatePassword = (password) => {
    const errors = [];

    if (password.length < 8) {
      errors.push("at least 8 characters");
    }
    if (password.length > 16) {
      errors.push("no more than 16 characters");
    }
    if (!/[A-Z]/.test(password)) {
      errors.push("one uppercase letter");
    }
    if (!/[a-z]/.test(password)) {
      errors.push("one lowercase letter");
    }
    if (!/[0-9]/.test(password)) {
      errors.push("one number");
    }
    if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
      errors.push("one special character");
    }

    if (errors.length > 0) {
      return {
        isValid: false,
        message: `Password must contain ${errors.join(", ")}`,
      };
    }

    return { isValid: true, message: "" };
  };

  /**
   * Verify if credentials match
   * @param {string} email - Email address
   * @param {string} password - Password
   * @returns {boolean} - Whether credentials match
   */
  const credentialsMatch = (email, password) => {
    return VALID_USERS.some(
      (user) => user.email === email && user.password === password
    );
  };

  // ===== Event Handlers =====

  /**
   * Handle form submission
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    const newErrors = {};

    // Validate email
    if (!email.trim()) {
      newErrors.email = "Email address is required";
    } else if (!isValidEmailFormat(email)) {
      newErrors.email = "Please enter a valid email address";
    } else if (!emailExists(email)) {
      newErrors.email = "This email address is not registered in our system";
    }

    // Validate password
    if (!password) {
      newErrors.password = "Password is required";
    } else {
      const passwordValidation = validatePassword(password);
      if (!passwordValidation.isValid) {
        newErrors.password = passwordValidation.message;
      } else if (
        email &&
        emailExists(email) &&
        !credentialsMatch(email, password)
      ) {
        newErrors.password = "Incorrect password. Please try again";
      }
    }

    // If there are errors, display them and stop
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    // Simulate login process (add loading state for better UX)
    setIsLoading(true);

    // Simulate network delay
    setTimeout(() => {
      setIsLoading(false);
      setIsLoggedIn(true);
      setLoggedInEmail(email);
    }, 800);
  };

  /**
   * Handle logout
   */
  const handleLogout = () => {
    setIsLoggedIn(false);
    setLoggedInEmail("");
    setEmail("");
    setPassword("");
    setErrors({});
  };

  /**
   * Toggle password visibility
   */
  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  // ===== Render =====

  // If logged in, show welcome page
  if (isLoggedIn) {
    return (
      <div className="app">
        <div className="welcome-container">
          <div className="welcome-card">
            <div className="success-icon">✓</div>
            <h1>Welcome!</h1>
            <p className="welcome-email">{loggedInEmail}</p>
            <p className="welcome-message">
              You have successfully logged in to Solum Medical
            </p>
            <button className="logout-button" onClick={handleLogout}>
              Logout
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Login form
  return (
    <div className="app">
      <div className="login-container">
        <div className="login-card">
          <div className="login-header">
            <h1>Solum Medical</h1>
            <p>Sign in to your account</p>
          </div>

          <form onSubmit={handleSubmit} noValidate>
            {/* Email input */}
            <div className="form-group">
              <label htmlFor="email">Email Address</label>
              <input
                id="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className={errors.email ? "error" : ""}
                placeholder="Enter your email"
                disabled={isLoading}
                autoComplete="email"
              />
              {errors.email && (
                <span className="error-message">{errors.email}</span>
              )}
            </div>

            {/* Password input */}
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <div className="password-input-wrapper">
                <input
                  id="password"
                  type={showPassword ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className={errors.password ? "error" : ""}
                  placeholder="Enter your password"
                  disabled={isLoading}
                  autoComplete="current-password"
                />
                <button
                  type="button"
                  className="password-toggle"
                  onClick={togglePasswordVisibility}
                  disabled={isLoading}
                  aria-label={showPassword ? "Hide password" : "Show password"}
                >
                  {showPassword ? "👁️" : "👁️‍🗨️"}
                </button>
              </div>
              {errors.password && (
                <span className="error-message">{errors.password}</span>
              )}
            </div>

            {/* Forgot password link */}
            <div className="forgot-password">
              <a href="#forgot" onClick={(e) => e.preventDefault()}>
                Forgot password?
              </a>
            </div>

            {/* Submit button */}
            <button type="submit" className="login-button" disabled={isLoading}>
              {isLoading ? "Signing in..." : "Sign In"}
            </button>
          </form>

          {/* Test accounts hint (for demo purposes only) */}
          <div className="test-accounts">
            <p className="test-accounts-title">Test Accounts:</p>
            <ul>
              <li>doctor@solum.com / Test123!</li>
              <li>admin@solum.com / Admin2024#</li>
              <li>test@example.com / Pass123$</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
