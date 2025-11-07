"""
CargoCraft Fleet Calculator
===========================

Solum Medical Technical Test - Task B

Problem:
    Determine the minimum and maximum number of crafts in a fleet given
    total propulsion units, where:
    - Type A crafts have 4 propulsion units
    - Type B crafts have 6 propulsion units

Mathematical Analysis:
    Given equation: 4a + 6b = n (where a = Type A, b = Type B)
    Simplified: 2a + 3b = n/2
    
    Key insights:
    1. n must be even (both 4 and 6 are even)
    2. Minimum crafts: maximize use of Type B (6 units)
    3. Maximum crafts: maximize use of Type A (4 units)

Author: Douglas
Date: November 2024
"""

from typing import Tuple, Optional


def calculate_fleet_size(n: int) -> Tuple[int, int]:
    """
    Calculate minimum and maximum possible number of crafts for given propulsion units.
    
    Args:
        n: Total number of propulsion units (must be positive integer)
        
    Returns:
        Tuple of (min_crafts, max_crafts)
        
    Raises:
        ValueError: If n is negative or if no valid combination exists
        
    Algorithm:
        1. Check if n is even (necessary condition)
        2. Calculate minimum: Use as many Type B (6) as possible
        3. Calculate maximum: Use as many Type A (4) as possible
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Input validation
    if n < 0:
        raise ValueError(f"Propulsion units cannot be negative: {n}")
    
    # Edge cases: impossible configurations
    if n == 0:
        raise ValueError("Cannot have zero propulsion units")
    
    if n % 2 != 0:
        # Odd numbers impossible (both 4 and 6 are even)
        raise ValueError(f"Cannot form {n} units (must be even)")
    
    if n == 2:
        # Too small for either craft type
        raise ValueError(f"Cannot form {n} units (minimum is 4)")
    
    # Calculate minimum crafts (maximize Type B usage)
    min_crafts = calculate_minimum_crafts(n)
    
    # Calculate maximum crafts (maximize Type A usage)
    max_crafts = calculate_maximum_crafts(n)
    
    return min_crafts, max_crafts


def calculate_minimum_crafts(n: int) -> int:
    """
    Calculate minimum number of crafts by maximizing Type B (6 units) usage.
    
    Strategy:
        - If n % 6 == 0: Use only Type B
        - If n % 6 == 2: Use 1 Type A + rest Type B (covers remainder 2 with 4)
        - If n % 6 == 4: Use 2 Type A + rest Type B (covers remainder 4 with 8)
    
    Args:
        n: Total propulsion units (guaranteed even and >= 4)
        
    Returns:
        Minimum number of crafts
    """
    remainder = n % 6
    
    if remainder == 0:
        # Perfect fit with Type B only
        # Example: n=24 → 4 Type B crafts
        return n // 6
    
    elif remainder == 2:
        # Need 1 Type A (4 units) to handle remainder 2
        # Example: n=8 → 1 Type A + 1 Type B (4+4=8, but we want 4+6=10)
        # Actually: 8 = 4+4 = 2 Type A, or impossible with B
        # Let me reconsider: 
        # n=8: 4+4=8 (2 Type A), cannot use Type B
        # n=14: 4+4+6=14 (2 Type A + 1 Type B) or 4+4+4+4=16 (no)
        # Actually 14 = 4 + 6 + 4 = 2A + 1B (total 3)
        # Or 14 % 6 = 2, so we need Type A to cover the 2
        # But we can't cover 2 with 4... 
        
        # Let me think differently:
        # n % 6 == 2 means we have 2 extra after using all possible Type B
        # We need to "exchange" some Type B for Type A to handle this
        # 1 Type B (6) → can't directly help with remainder 2
        # But 2 Type A (8) ≡ 1 Type B (6) + 2, so we replace 1 Type B with 2 Type A
        # So: (n-2)/6 Type B → (n-2-6)/6 Type B + 2 Type A = (n-8)/6 Type B + 2 Type A
        # Wait, that's not quite right either.
        
        # Let's use the standard approach:
        # 4a + 6b = n
        # If n % 6 = 2, then we can set a=2 (gives us 8), and b = (n-8)/6
        # Total crafts = 2 + (n-8)/6
        
        # But we want MINIMUM, so we should minimize total crafts
        # Actually, the key insight is:
        # n % 6 = 2 → we need exactly 2 extra units beyond multiples of 6
        # 2 Type A gives 8 = 6 + 2, so using 2 Type A covers one Type B + remainder
        
        # Actually the cleaner way:
        # n ≡ 2 (mod 6) means we can write n = 6k + 2 for some k
        # To minimize crafts, we want to use Type B as much as possible
        # But 6 doesn't divide n. We need to adjust.
        # If we use 2 Type A (8 units), we've used n-8 units with Type B
        # So: 2 Type A + (n-8)/6 Type B = 2 + (n-8)/6
        
        # But wait, we need n >= 8 for this to work
        # If n = 2, it's impossible (caught earlier)
        # If n = 8, then 2 + 0 = 2 crafts
        
        type_a_needed = 2
        remaining = n - (type_a_needed * 4)
        type_b_possible = remaining // 6
        return type_a_needed + type_b_possible
    
    else:  # remainder == 4
        # Need 1 Type A (4 units) to handle remainder 4
        # Example: n=10 → 1 Type A + 1 Type B (4+6=10)
        type_a_needed = 1
        remaining = n - (type_a_needed * 4)
        type_b_possible = remaining // 6
        return type_a_needed + type_b_possible


def calculate_maximum_crafts(n: int) -> int:
    """
    Calculate maximum number of crafts by maximizing Type A (4 units) usage.
    
    Strategy:
        - If n % 4 == 0: Use only Type A
        - If n % 4 == 2: Use 1 Type B + rest Type A (covers remainder 2 with 6)
    
    Args:
        n: Total propulsion units (guaranteed even and >= 4)
        
    Returns:
        Maximum number of crafts
    """
    remainder = n % 4
    
    if remainder == 0:
        # Perfect fit with Type A only
        # Example: n=24 → 6 Type A crafts
        return n // 4
    
    else:  # remainder == 2 (since n is even, remainder can only be 0 or 2)
        # Need 1 Type B (6 units) to handle remainder 2
        # Example: n=10 → 1 Type B + 1 Type A (6+4=10)
        type_b_needed = 1
        remaining = n - (type_b_needed * 6)
        type_a_possible = remaining // 4
        return type_b_needed + type_a_possible


def solve_single_case(n: int) -> str:
    """
    Solve a single test case and return formatted result.
    
    Args:
        n: Total propulsion units
        
    Returns:
        Formatted string: "min max" or "-1" if impossible
    """
    try:
        min_crafts, max_crafts = calculate_fleet_size(n)
        return f"{min_crafts} {max_crafts}"
    except ValueError:
        return "-1"


def process_batch_input(input_data: str) -> str:
    """
    Process multiple test cases from formatted input string.
    
    Input format:
        First line: number of test cases t
        Next t lines: each contains one integer n
        
    Args:
        input_data: Multi-line string containing test cases
        
    Returns:
        Multi-line string with results
        
    Raises:
        ValueError: If input format is invalid
    """
    lines = input_data.strip().split('\n')
    
    if not lines or not lines[0]:
        raise ValueError("Empty input")
    
    try:
        t = int(lines[0])
    except (ValueError, IndexError) as e:
        raise ValueError(f"Invalid number of test cases: {e}")
    
    if t < 1 or t > 1000:
        raise ValueError(f"Number of test cases must be between 1 and 1000, got {t}")
    
    if len(lines) < t + 1:
        raise ValueError(f"Expected {t} test cases, but got {len(lines)-1}")
    
    results = []
    for i in range(1, t + 1):
        try:
            n = int(lines[i])
            if n < 1 or n > 10**18:
                raise ValueError(f"n must be between 1 and 10^18, got {n}")
            result = solve_single_case(n)
            results.append(result)
        except (ValueError, IndexError) as e:
            raise ValueError(f"Error processing test case {i}: {e}")
    
    return '\n'.join(results)


def main():
    """
    Main function to handle user input and output.
    
    Supports two modes:
    1. Interactive: Prompts user for input
    2. File: Reads from stdin (for automated testing)
    """
    print("=" * 50)
    print("CargoCraft Fleet Calculator")
    print("Solum Medical Technical Test - Task B")
    print("=" * 50)
    print()
    print("Fleet Configuration:")
    print("  Type A: 4 propulsion units")
    print("  Type B: 6 propulsion units")
    print()
    print("Enter input (or press Ctrl+D when done):")
    print()
    
    try:
        # Read all input
        input_lines = []
        while True:
            try:
                line = input()
                input_lines.append(line)
            except EOFError:
                break
        
        if not input_lines:
            print("\nNo input provided. Exiting.")
            return
        
        input_data = '\n'.join(input_lines)
        
        # Process input
        result = process_batch_input(input_data)
        
        # Output results
        print("\n" + "=" * 50)
        print("RESULTS:")
        print("=" * 50)
        print(result)
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())