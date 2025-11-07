"""
Solum Medical Technical Test - Question A: Mystic Waves
========================================================

Problem:
A mage casts n waves of alternating energy: x, -x, x, -x, ...
Calculate the total energy after all n waves.

Mathematical Solution:
- If n is even: pairs cancel out → total = 0
- If n is odd: one unpaired positive x remains → total = x

Time Complexity: O(1)
Space Complexity: O(1)

Author: [Jingdi Lin]
Date: November 2025
"""


def calculate_total_energy(x: int, n: int) -> int:
    """
    Calculate the total magical energy after n alternating waves.
    
    The energy sequence is: x, -x, x, -x, x, -x, ...
    
    Args:
        x (int): The base energy value (1 ≤ x)
        n (int): The number of waves (1 ≤ n ≤ 10)
    
    Returns:
        int: The total energy after all n waves
        
    Examples:
        >>> calculate_total_energy(1, 4)
        0
        >>> calculate_total_energy(2, 5)
        2
        >>> calculate_total_energy(3, 6)
        0
    
    Raises:
        ValueError: If x or n is out of valid range
        TypeError: If x or n is not an integer
    """
    # Input validation
    if not isinstance(x, int) or not isinstance(n, int):
        raise TypeError(f"x and n must be integers, got x={type(x).__name__}, n={type(n).__name__}")
    
    if not (1 <= x):
        raise ValueError(f"x must be larger than 1, got {x}")
    
    if not (1 <= n <= 10):
        raise ValueError(f"n must be between 1 and 10, got {n}")
    
    # Core logic: check if n is odd or even
    if n % 2 == 0:
        # Even number of waves: all pairs cancel out
        return 0
    else:
        # Odd number of waves: one positive x remains
        return x


def solve_test_cases(test_cases: list) -> list:
    """
    Process multiple test cases and return results.
    
    Args:
        test_cases (list): List of tuples [(x1, n1), (x2, n2), ...]
    
    Returns:
        list: List of total energies for each test case
        
    Raises:
        ValueError: If test_cases is empty or contains invalid data
    """
    if not test_cases:
        raise ValueError("test_cases cannot be empty")
    
    if not isinstance(test_cases, list):
        raise TypeError(f"test_cases must be a list, got {type(test_cases).__name__}")
    
    results = []
    
    for i, case in enumerate(test_cases):
        if not isinstance(case, tuple) or len(case) != 2:
            raise ValueError(f"Test case {i+1} must be a tuple of (x, n), got {case}")
        
        x, n = case
        result = calculate_total_energy(x, n)
        results.append(result)
    
    return results


def read_input_from_stdin():
    """
    Read test cases from standard input according to problem format.
    
    Input Format:
        First line: t (number of test cases)
        Next t lines: x and n (space-separated)
    
    Returns:
        list: List of tuples [(x1, n1), (x2, n2), ...]
    """
    try:
        t = int(input().strip())
        
        if not (1 <= t <= 100):
            raise ValueError(f"Number of test cases must be between 1 and 100, got {t}")
        
        test_cases = []
        
        for i in range(t):
            line = input().strip()
            x, n = map(int, line.split())
            test_cases.append((x, n))
        
        return test_cases
    
    except ValueError as e:
        print(f"Error: Invalid input format - {e}")
        raise
    except Exception as e:
        print(f"Error: Unexpected error while reading input - {e}")
        raise


def main():
    """
    Main function to run the Mystic Waves solver.
    Reads input from stdin and prints results to stdout.
    """
    try:
        # Read test cases from standard input
        test_cases = read_input_from_stdin()
        
        # Solve all test cases
        results = solve_test_cases(test_cases)
        
        # Print results (one per line)
        for result in results:
            print(result)
    
    except Exception as e:
        print(f"Fatal error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    main()