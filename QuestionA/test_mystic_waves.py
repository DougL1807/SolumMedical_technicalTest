"""
Test Suite for Mystic Waves
============================

Validates boundary conditions according to actual code implementation:
- t: 1 ≤ t ≤ 100 (number of test cases)
- x: x ≥ 1 (no upper limit)
- n: 1 ≤ n ≤ 10 (number of waves)

Run: pytest test_mystic_waves.py -v
"""

import pytest
from mystic_waves import calculate_total_energy, solve_test_cases


class TestCoreAlgorithm:
    """Test the core energy calculation algorithm."""
    
    def test_official_cases(self):
        """Official test cases from problem."""
        assert calculate_total_energy(1, 4) == 0
        assert calculate_total_energy(2, 5) == 2
        assert calculate_total_energy(3, 6) == 0
        assert calculate_total_energy(4, 7) == 4
    
    def test_odd_n_returns_x(self):
        """Odd n should return x."""
        assert calculate_total_energy(5, 1) == 5
        assert calculate_total_energy(3, 3) == 3
        assert calculate_total_energy(7, 5) == 7
        assert calculate_total_energy(100, 9) == 100
    
    def test_even_n_returns_zero(self):
        """Even n should return 0."""
        assert calculate_total_energy(1, 2) == 0
        assert calculate_total_energy(5, 4) == 0
        assert calculate_total_energy(8, 6) == 0
        assert calculate_total_energy(1000, 10) == 0


class TestXBoundaries:
    """Test x boundaries: x ≥ 1 (no upper limit)."""
    
    def test_x_minimum_valid(self):
        """x = 1 is the minimum valid value."""
        assert calculate_total_energy(1, 1) == 1
        assert calculate_total_energy(1, 5) == 1
        assert calculate_total_energy(1, 10) == 0
    
    def test_x_large_values_valid(self):
        """Large x values should work (no upper limit)."""
        assert calculate_total_energy(100, 1) == 100
        assert calculate_total_energy(1000, 3) == 1000
        assert calculate_total_energy(999999, 5) == 999999
    
    def test_x_zero_invalid(self):
        """x = 0 should raise ValueError."""
        with pytest.raises(ValueError, match="x must be larger than 1"):
            calculate_total_energy(0, 5)
    
    def test_x_negative_invalid(self):
        """Negative x should raise ValueError."""
        with pytest.raises(ValueError, match="x must be larger than 1"):
            calculate_total_energy(-1, 5)
        
        with pytest.raises(ValueError, match="x must be larger than 1"):
            calculate_total_energy(-100, 5)


class TestNBoundaries:
    """Test n boundaries: 1 ≤ n ≤ 10."""
    
    def test_n_minimum_valid(self):
        """n = 1 is the minimum valid value."""
        assert calculate_total_energy(5, 1) == 5
        assert calculate_total_energy(10, 1) == 10
        assert calculate_total_energy(100, 1) == 100
    
    def test_n_maximum_valid(self):
        """n = 10 is the maximum valid value."""
        assert calculate_total_energy(5, 10) == 0
        assert calculate_total_energy(3, 10) == 0
        assert calculate_total_energy(100, 10) == 0
    
    def test_n_zero_invalid(self):
        """n = 0 should raise ValueError."""
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, 0)
    
    def test_n_negative_invalid(self):
        """Negative n should raise ValueError."""
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, -1)
        
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, -50)
    
    def test_n_above_maximum_invalid(self):
        """n > 10 should raise ValueError."""
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, 11)
        
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, 100)


class TestCombinedBoundaries:
    """Test combinations of boundary values."""
    
    def test_both_minimum(self):
        """x and n at minimum."""
        assert calculate_total_energy(1, 1) == 1
    
    def test_x_large_n_maximum(self):
        """Large x, n at maximum."""
        assert calculate_total_energy(1000, 10) == 0
    
    def test_x_large_n_minimum(self):
        """Large x, n at minimum."""
        assert calculate_total_energy(1000, 1) == 1000
    
    def test_both_invalid_low(self):
        """Both x and n below minimum."""
        with pytest.raises(ValueError):
            calculate_total_energy(0, 0)
    
    def test_x_valid_n_invalid_high(self):
        """Valid x, n too high."""
        with pytest.raises(ValueError, match="n must be between 1 and 10"):
            calculate_total_energy(5, 11)


class TestTypeValidation:
    """Test input type validation."""
    
    def test_x_must_be_integer(self):
        """x must be integer."""
        with pytest.raises(TypeError, match="x and n must be integers"):
            calculate_total_energy(5.5, 3)
        
        with pytest.raises(TypeError, match="x and n must be integers"):
            calculate_total_energy("5", 3)
    
    def test_n_must_be_integer(self):
        """n must be integer."""
        with pytest.raises(TypeError, match="x and n must be integers"):
            calculate_total_energy(5, 3.5)
        
        with pytest.raises(TypeError, match="x and n must be integers"):
            calculate_total_energy(5, "3")
    
    def test_both_must_be_integers(self):
        """Both must be integers."""
        with pytest.raises(TypeError, match="x and n must be integers"):
            calculate_total_energy(5.5, 3.5)


class TestBatchProcessing:
    """Test solve_test_cases for batch processing."""
    
    def test_single_case(self):
        """Single test case."""
        assert solve_test_cases([(1, 4)]) == [0]
    
    def test_multiple_cases(self):
        """Multiple test cases."""
        cases = [(1, 4), (2, 5), (3, 6), (4, 7)]
        assert solve_test_cases(cases) == [0, 2, 0, 4]
    
    def test_t_minimum_valid(self):
        """t = 1 (minimum)."""
        assert solve_test_cases([(5, 3)]) == [5]
    
    def test_t_maximum_valid(self):
        """t = 100 (maximum)."""
        cases = [(i % 10 + 1, i % 10 + 1) for i in range(100)]
        results = solve_test_cases(cases)
        assert len(results) == 100
    
    def test_empty_cases_invalid(self):
        """Empty test case list."""
        with pytest.raises(ValueError, match="test_cases cannot be empty"):
            solve_test_cases([])
    
    def test_invalid_format(self):
        """Invalid test case format."""
        with pytest.raises(ValueError, match="must be a tuple of"):
            solve_test_cases([(1, 2, 3)])
    
    def test_boundary_cases_in_batch(self):
        """Batch with boundary values."""
        cases = [
            (1, 1),      # x min, n min
            (1000, 10),  # x large, n max
            (1, 10),     # x min, n max
            (1000, 1),   # x large, n min
        ]
        assert solve_test_cases(cases) == [1, 0, 0, 1000]


class TestComprehensive:
    """Comprehensive real-world scenarios."""
    
    def test_all_input_txt_cases(self):
        """All 12 test cases from input.txt."""
        cases = [
            (1, 1),    # 1
            (1, 10),   # 0
            (10, 1),   # 10
            (10, 10),  # 0
            (1, 4),    # 0
            (2, 5),    # 2
            (3, 6),    # 0
            (4, 7),    # 4
            (5, 2),    # 0
            (10, 9),   # 10
            (1, 2),    # 0
            (10, 2),   # 0
        ]
        expected = [1, 0, 10, 0, 0, 2, 0, 4, 0, 10, 0, 0]
        assert solve_test_cases(cases) == expected
    
    def test_pattern_verification(self):
        """Verify alternating pattern."""
        # n=1: x
        assert calculate_total_energy(7, 1) == 7
        # n=2: x + (-x) = 0
        assert calculate_total_energy(7, 2) == 0
        # n=3: x + (-x) + x = x
        assert calculate_total_energy(7, 3) == 7
        # n=4: x + (-x) + x + (-x) = 0
        assert calculate_total_energy(7, 4) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])