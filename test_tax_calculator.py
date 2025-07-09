import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tax_calculator import calculate_tax

def test_tax_for_zero_earnings():
    """
    Test case: Earnings are 0.
    Expected: Tax should be 0.
    """
    assert calculate_tax(0) == 0

def test_tax_for_earnings_below_first_bracket():
    """
    Test case: Earnings are 11999 (just below the 12000 threshold).
    Expected: Tax should be 0.
    """
    assert calculate_tax(11999) == 0

def test_tax_for_earnings_at_first_bracket_threshold():
    """
    Test case: Earnings are exactly 12000.
    Expected: Tax should be 0 (as rule is '< 12000').
    """
    assert calculate_tax(12000) == 0

def test_tax_for_earnings_just_above_first_bracket():
    """
    Test case: Earnings are 12001.
    Expected: Tax should be 20% of (12001 - 12000) = 20% of 1 = 0.20.
    """
    assert calculate_tax(12001) == 0.20

def test_tax_for_mid_range_second_bracket():
    """
    Test case: Earnings are 20000.
    Expected: Tax should be 20% of (20000 - 12000) = 20% of 8000 = 1600.
    """
    assert calculate_tax(20000) == 1600

def test_tax_for_earnings_just_below_third_bracket():
    """
    Test case: Earnings are 35999.
    Expected: Tax should be 20% of (35999 - 12000) = 20% of 23999 = 4799.80.
    """
    assert calculate_tax(35999) == 4799.80

def test_tax_for_earnings_at_second_bracket_threshold():
    """
    Test case: Earnings are exactly 36000.
    Expected: Tax should be 20% of (36000 - 12000) = 20% of 24000 = 4800.
    """
    assert calculate_tax(36000) == 4800

def test_tax_for_earnings_just_above_second_bracket():
    """
    Test case: Earnings are 36001.
    Expected:
    - Tax on (36000 - 12000) = 24000 at 20% = 4800
    - Tax on (36001 - 36000) = 1 at 40% = 0.40
    Total = 4800 + 0.40 = 4800.40
    """
    assert calculate_tax(36001) == 4800.40

def test_tax_for_high_earnings_third_bracket():
    """
    Test case: Earnings are 50000.
    Expected:
    - Tax on (36000 - 12000) = 24000 at 20% = 4800
    - Tax on (50000 - 36000) = 14000 at 40% = 5600
    Total = 4800 + 5600 = 10400
    """
    assert calculate_tax(50000) == 10400

