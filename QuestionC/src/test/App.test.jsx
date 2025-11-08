import { describe, it, expect, beforeEach } from "vitest";
import {
  render,
  screen,
  fireEvent,
  waitFor,
  cleanup,
} from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import App from "../App";

/**
 * Test Suite for Solum Medical Login Page
 *
 * This test suite covers:
 * - Email validation (format, existence, empty state)
 * - Password validation (length, complexity requirements)
 * - Login process (success and failure scenarios)
 * - Logout functionality
 * - UI interactions (password visibility toggle)
 */

describe("Solum Medical Login Page", () => {
  // ===== Helper Functions =====

  /**
   * Helper function to fill in login form
   */
  const fillLoginForm = async (email, password) => {
    const emailInput = screen.getByLabelText(/email address/i);
    const passwordInput = screen.getByLabelText(/^password$/i);

    await userEvent.clear(emailInput);
    await userEvent.clear(passwordInput);

    if (email) await userEvent.type(emailInput, email);
    if (password) await userEvent.type(passwordInput, password);
  };

  /**
   * Helper function to submit the form
   */
  const submitForm = async () => {
    const submitButton = screen.getByRole("button", { name: /sign in/i });
    await userEvent.click(submitButton);
  };

  // ===== Initial Render Tests =====

  describe("Initial Render", () => {
    it("should render login form with all required elements", () => {
      render(<App />);

      expect(screen.getByText(/solum medical/i)).toBeInTheDocument();
      expect(screen.getByLabelText(/email address/i)).toBeInTheDocument();
      expect(screen.getByLabelText(/^password$/i)).toBeInTheDocument();
      expect(
        screen.getByRole("button", { name: /sign in/i })
      ).toBeInTheDocument();
      expect(screen.getByText(/forgot password/i)).toBeInTheDocument();
    });

    it("should display test accounts information", () => {
      render(<App />);

      expect(screen.getByText(/test accounts:/i)).toBeInTheDocument();
      expect(screen.getByText(/doctor@solum.com/)).toBeInTheDocument();
      expect(screen.getByText(/admin@solum.com/)).toBeInTheDocument();
      expect(screen.getByText(/test@example.com/)).toBeInTheDocument();
    });
  });

  // ===== Email Validation Tests =====

  describe("Email Validation", () => {
    beforeEach(() => {
      render(<App />);
    });

    it("should show error when email is empty", async () => {
      await fillLoginForm("", "Test123!");
      await submitForm();

      expect(
        screen.getByText(/email address is required/i)
      ).toBeInTheDocument();
    });

    it("should show error for invalid email format", async () => {
      await fillLoginForm("invalid-email", "Test123!");
      await submitForm();

      expect(
        screen.getByText(/please enter a valid email address/i)
      ).toBeInTheDocument();
    });

    it("should show error for email not in system", async () => {
      await fillLoginForm("notfound@example.com", "Test123!");
      await submitForm();

      expect(
        screen.getByText(/this email address is not registered in our system/i)
      ).toBeInTheDocument();
    });

    it("should accept valid email format", async () => {
      await fillLoginForm("doctor@solum.com", "Test123!");
      await submitForm();

      // Should not show email format error
      expect(
        screen.queryByText(/please enter a valid email address/i)
      ).not.toBeInTheDocument();
    });
  });

  // ===== Password Validation Tests =====

  describe("Password Validation", () => {
    beforeEach(() => {
      render(<App />);
    });

    it("should show error when password is empty", async () => {
      await fillLoginForm("doctor@solum.com", "");
      await submitForm();

      expect(screen.getByText(/password is required/i)).toBeInTheDocument();
    });

    it("should show error for password shorter than 8 characters", async () => {
      await fillLoginForm("doctor@solum.com", "Test1!");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*at least 8 characters/i)
      ).toBeInTheDocument();
    });

    it("should show error for password longer than 16 characters", async () => {
      await fillLoginForm("doctor@solum.com", "Test123456789012!");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*no more than 16 characters/i)
      ).toBeInTheDocument();
    });

    it("should show error for password without uppercase letter", async () => {
      await fillLoginForm("doctor@solum.com", "test123!");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*one uppercase letter/i)
      ).toBeInTheDocument();
    });

    it("should show error for password without lowercase letter", async () => {
      await fillLoginForm("doctor@solum.com", "TEST123!");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*one lowercase letter/i)
      ).toBeInTheDocument();
    });

    it("should show error for password without number", async () => {
      await fillLoginForm("doctor@solum.com", "TestTest!");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*one number/i)
      ).toBeInTheDocument();
    });

    it("should show error for password without special character", async () => {
      await fillLoginForm("doctor@solum.com", "Test1234");
      await submitForm();

      expect(
        screen.getByText(/password must contain.*one special character/i)
      ).toBeInTheDocument();
    });

    it("should show error for incorrect password with valid email", async () => {
      await fillLoginForm("doctor@solum.com", "Wrong123!");
      await submitForm();

      expect(screen.getByText(/incorrect password/i)).toBeInTheDocument();
    });
  });

  // ===== Login Process Tests =====

  describe("Login Process", () => {
    beforeEach(() => {
      render(<App />);
    });

    it("should successfully login with valid credentials", async () => {
      await fillLoginForm("doctor@solum.com", "Test123!");
      await submitForm();

      // Wait for login to complete (simulated delay)
      await waitFor(
        () => {
          expect(screen.getByText(/welcome!/i)).toBeInTheDocument();
        },
        { timeout: 2000 }
      );

      expect(screen.getByText("doctor@solum.com")).toBeInTheDocument();
      expect(
        screen.getByText(/you have successfully logged in to solum medical/i)
      ).toBeInTheDocument();
    });

    it("should work with all three test accounts", async () => {
      const testAccounts = [
        { email: "doctor@solum.com", password: "Test123!" },
        { email: "admin@solum.com", password: "Admin2024#" },
        { email: "test@example.com", password: "Pass123$" },
      ];

      for (const account of testAccounts) {
        // Clean up before each iteration
        cleanup();
        render(<App />);

        await fillLoginForm(account.email, account.password);
        await submitForm();

        await waitFor(
          () => {
            expect(screen.getByText(/welcome!/i)).toBeInTheDocument();
          },
          { timeout: 2000 }
        );

        expect(screen.getByText(account.email)).toBeInTheDocument();
      }
    });

    it("should disable inputs and button during login", async () => {
      await fillLoginForm("doctor@solum.com", "Test123!");

      const emailInput = screen.getByLabelText(/email address/i);
      const passwordInput = screen.getByLabelText(/^password$/i);
      const submitButton = screen.getByRole("button", { name: /sign in/i });

      // Click submit
      await userEvent.click(submitButton);

      // Immediately check if elements are disabled
      expect(emailInput).toBeDisabled();
      expect(passwordInput).toBeDisabled();
      expect(submitButton).toBeDisabled();
      expect(screen.getByText(/signing in/i)).toBeInTheDocument();
    });
  });

  // ===== Logout Functionality Tests =====

  describe("Logout Functionality", () => {
    it("should logout and return to login page", async () => {
      render(<App />);

      // Login first
      await fillLoginForm("doctor@solum.com", "Test123!");
      await submitForm();

      await waitFor(
        () => {
          expect(screen.getByText(/welcome!/i)).toBeInTheDocument();
        },
        { timeout: 2000 }
      );

      // Now logout
      const logoutButton = screen.getByRole("button", { name: /logout/i });
      await userEvent.click(logoutButton);

      // Should return to login page
      expect(screen.getByText(/sign in to your account/i)).toBeInTheDocument();
      expect(screen.getByLabelText(/email address/i)).toBeInTheDocument();

      // Form should be cleared
      const emailInput = screen.getByLabelText(/email address/i);
      const passwordInput = screen.getByLabelText(/^password$/i);
      expect(emailInput).toHaveValue("");
      expect(passwordInput).toHaveValue("");
    });
  });

  // ===== UI Interaction Tests =====

  describe("UI Interactions", () => {
    it("should toggle password visibility", async () => {
      render(<App />);

      const passwordInput = screen.getByLabelText(/^password$/i);
      const toggleButton = screen.getByRole("button", {
        name: /show password/i,
      });

      // Initially password should be hidden
      expect(passwordInput).toHaveAttribute("type", "password");

      // Click to show password
      await userEvent.click(toggleButton);
      expect(passwordInput).toHaveAttribute("type", "text");

      // Click again to hide password
      await userEvent.click(toggleButton);
      expect(passwordInput).toHaveAttribute("type", "password");
    });

    it("should prevent form submission on Enter key with invalid data", async () => {
      render(<App />);

      const emailInput = screen.getByLabelText(/email address/i);
      await userEvent.type(emailInput, "invalid-email{Enter}");

      // Should show validation error
      expect(
        screen.getByText(/please enter a valid email address/i)
      ).toBeInTheDocument();

      // Should not navigate to welcome page
      expect(screen.queryByText(/welcome!/i)).not.toBeInTheDocument();
    });
  });

  // ===== Edge Cases Tests =====

  describe("Edge Cases", () => {
    beforeEach(() => {
      render(<App />);
    });

    it("should trim whitespace from email", async () => {
      await fillLoginForm("  doctor@solum.com  ", "Test123!");
      await submitForm();

      await waitFor(
        () => {
          expect(screen.getByText(/welcome!/i)).toBeInTheDocument();
        },
        { timeout: 2000 }
      );
    });

    it("should handle multiple validation errors simultaneously", async () => {
      await fillLoginForm("", "");
      await submitForm();

      expect(
        screen.getByText(/email address is required/i)
      ).toBeInTheDocument();
      expect(screen.getByText(/password is required/i)).toBeInTheDocument();
    });

    it("should clear previous errors on new submission", async () => {
      // First submission with errors
      await fillLoginForm("invalid", "short");
      await submitForm();

      expect(
        screen.getByText(/please enter a valid email address/i)
      ).toBeInTheDocument();

      // Second submission with correct data
      await fillLoginForm("doctor@solum.com", "Test123!");
      await submitForm();

      // Previous error should be gone
      expect(
        screen.queryByText(/please enter a valid email address/i)
      ).not.toBeInTheDocument();
    });
  });
});
