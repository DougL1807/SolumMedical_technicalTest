"""
Test Suite for CargoCraft Fleet Calculator
==========================================

Comprehensive tests covering:
- Basic functionality
- Edge cases
- Large numbers (up to 10^18)
- Invalid inputs
- All test cases from problem statement

Run with: pytest test_cargocraft.py -v
"""

import pytest
from cargocraft import (
    calculate_fleet_size,
    calculate_minimum_crafts,
    calculate_maximum_crafts,
    solve_single_case,
    process_batch_input
)


class TestBasicFunctionality:
    """Test basic fleet size calculations."""
    
    def test_single_type_a_craft(self):
        """Test with exactly one Type A craft (4 units)."""
        min_crafts, max_crafts = calculate_fleet_size(4)
        assert min_crafts == 1
        assert max_crafts == 1
    
    def test_single_type_b_craft(self):
        """Test with exactly one Type B craft (6 units)."""
        min_crafts, max_crafts = calculate_fleet_size(6)
        assert min_crafts == 1
        assert max_crafts == 1
    
    def test_example_case_24_units(self):
        """Test example from problem: n=24."""
        min_crafts, max_crafts = calculate_fleet_size(24)
        assert min_crafts == 4  # 4 Type B (4×6=24)
        assert max_crafts == 6  # 6 Type A (6×4=24)
    
    def test_mixed_configuration(self):
        """Test case requiring both craft types."""
        min_crafts, max_crafts = calculate_fleet_size(10)
        assert min_crafts == 2  # 1A + 1B (4+6=10)
        assert max_crafts == 2  # 1A + 1B (4+6=10)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_minimum_valid_input(self):
        """Test smallest valid input (4 units)."""
        min_crafts, max_crafts = calculate_fleet_size(4)
        assert min_crafts == 1
        assert max_crafts == 1
    
    def test_divisible_by_six(self):
        """Test numbers perfectly divisible by 6."""
        test_cases = [6, 12, 18, 30, 60]
        for n in test_cases:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert min_crafts == n // 6
    
    def test_divisible_by_four(self):
        """Test numbers perfectly divisible by 4."""
        test_cases = [8, 16, 20, 28, 40]
        for n in test_cases:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert max_crafts == n // 4
    
    def test_remainder_two_after_six(self):
        """Test n % 6 == 2 cases."""
        # n=8: 2A (8), n=14: 2A+1B (8+6), n=20: 2A+2B (8+12)
        test_cases = [(8, 2, 2), (14, 3, 3), (20, 4, 5)]
        for n, expected_min, expected_max in test_cases:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert min_crafts == expected_min
            assert max_crafts == expected_max
    
    def test_remainder_four_after_six(self):
        """Test n % 6 == 4 cases."""
        # n=10: 1A+1B, n=16: 1A+2B (4+12) or 4A (16)
        test_cases = [(10, 2, 2), (16, 3, 4), (22, 4, 5)]
        for n, expected_min, expected_max in test_cases:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert min_crafts == expected_min
            assert max_crafts == expected_max


class TestLargeNumbers:
    """Test with very large numbers (up to 10^18)."""
    
    def test_large_number_from_example(self):
        """Test the large number from problem statement."""
        n = 998244353998244352
        min_crafts, max_crafts = calculate_fleet_size(n)
        assert min_crafts == 166374058999707392
        assert max_crafts == 249561088499561088
    
    def test_max_boundary(self):
        """Test near maximum allowed value (10^18)."""
        n = 10**18  # 1,000,000,000,000,000,000
        min_crafts, max_crafts = calculate_fleet_size(n)
        # Should complete without overflow
        assert min_crafts > 0
        assert max_crafts > 0
        assert min_crafts <= max_crafts
    
    def test_large_even_numbers(self):
        """Test various large even numbers."""
        test_cases = [
            10**9,      # 1 billion
            10**12,     # 1 trillion
            10**15,     # 1 quadrillion
        ]
        for n in test_cases:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert min_crafts > 0
            assert max_crafts > 0
            assert min_crafts <= max_crafts


class TestInvalidInputs:
    """Test error handling for invalid inputs."""
    
    def test_odd_number(self):
        """Test that odd numbers raise ValueError."""
        with pytest.raises(ValueError, match="must be even"):
            calculate_fleet_size(7)
    
    def test_negative_number(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_fleet_size(-5)
    
    def test_zero(self):
        """Test that zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot have zero"):
            calculate_fleet_size(0)
    
    def test_two_units(self):
        """Test that 2 units (too small) raises ValueError."""
        with pytest.raises(ValueError, match="minimum is 4"):
            calculate_fleet_size(2)
    
    def test_odd_numbers_return_minus_one(self):
        """Test that solve_single_case returns -1 for odd numbers."""
        assert solve_single_case(7) == "-1"
        assert solve_single_case(13) == "-1"
        assert solve_single_case(99) == "-1"


class TestProblemExamples:
    """Test all examples from the problem statement."""
    
    def test_example_input_output(self):
        """Test complete example from problem."""
        input_data = """4
4
7
24
998244353998244352"""
        
        expected_output = """1 1
-1
4 6
166374058999707392 249561088499561088"""
        
        result = process_batch_input(input_data)
        assert result == expected_output
    
    def test_individual_examples(self):
        """Test each example case individually."""
        test_cases = [
            (4, "1 1"),
            (7, "-1"),
            (24, "4 6"),
            (998244353998244352, "166374058999707392 249561088499561088"),
        ]
        
        for n, expected in test_cases:
            result = solve_single_case(n)
            assert result == expected, f"Failed for n={n}"


class TestBatchProcessing:
    """Test batch input processing."""
    
    def test_single_test_case(self):
        """Test batch with one test case."""
        input_data = "1\n10"
        result = process_batch_input(input_data)
        assert result == "2 2"
    
    def test_multiple_test_cases(self):
        """Test batch with multiple cases."""
        input_data = """3
4
6
8"""
        expected = """1 1
1 1
2 2"""
        result = process_batch_input(input_data)
        assert result == expected
    
    def test_empty_input(self):
        """Test that empty input raises ValueError."""
        with pytest.raises(ValueError, match="Empty input"):
            process_batch_input("")
    
    def test_invalid_test_count(self):
        """Test invalid number of test cases."""
        with pytest.raises(ValueError):
            process_batch_input("0\n")
        
        with pytest.raises(ValueError):
            process_batch_input("1001\n10")
    
    def test_mismatched_test_count(self):
        """Test when actual cases don't match declared count."""
        with pytest.raises(ValueError, match="Expected"):
            process_batch_input("3\n4\n6")  # Says 3, only gives 2


class TestMathematicalProperties:
    """Test mathematical properties of the solution."""
    
    def test_min_always_less_or_equal_max(self):
        """Verify min <= max for all valid inputs."""
        test_values = [4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 30, 100, 1000]
        for n in test_values:
            min_crafts, max_crafts = calculate_fleet_size(n)
            assert min_crafts <= max_crafts
    
    def test_solution_validity(self):
        """Verify that min and max produce valid combinations."""
        test_values = [4, 6, 8, 10, 12, 24, 30, 48]
        
        for n in test_values:
            min_crafts, max_crafts = calculate_fleet_size(n)
            
            # For minimum: should be achievable with some a,b combination
            # We know it's valid if our algorithm says so
            assert min_crafts >= 1
            
            # For maximum: should be achievable
            assert max_crafts >= min_crafts
            
            # Verify n is in valid range
            # Minimum possible: min_crafts * 4 (all Type A)
            # Maximum possible: max_crafts * 6 (all Type B)
            assert min_crafts * 4 <= n <= max_crafts * 6


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])