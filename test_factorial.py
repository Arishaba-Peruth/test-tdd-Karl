import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from factorial import factorial

def test_factorial():
    assert factorial(0) == 1, "Test failed: factorial(0) should be 1"

def test1_factorial():
    assert factorial(1) == 1, "Test failed: factorial(1) should be 1"

def test2_factorial():
    assert factorial(2) == 2, "Test failed: factorial(2) should be 2"

def test3_factorial():
    assert factorial(3) == 6, "Test failed: factorial(3) should be 6"

def test4_factorial():
    assert factorial(4) == 24, "Test failed: factorial(4) should be 24"

def test5_factorial():
    assert factorial(5) == 120, "Test failed: factorial(5) should be 120"
    print("All tests passed!")