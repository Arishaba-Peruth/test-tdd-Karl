import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fibonacci import fibonacci # Import the fibonacci function from the fibonacci module

def test_fibonacci():
    assert fibonacci(0) == 0

def test_fibonacci1():
    assert fibonacci(1) == 1

def test_fibonacci2():
    assert fibonacci(2) == 1

def test_fibonacci3():
    assert fibonacci(3) == 2

def test_fibonacci4():
    assert fibonacci(4) == 3

def test_fibonacci4():
    assert fibonacci(5) == 5

def test_fibonacci5():
    assert fibonacci(6) == 8
  