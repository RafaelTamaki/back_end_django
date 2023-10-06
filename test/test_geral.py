import math
from typing import assert_type 
import pytest

def raiz (n):
    return math.sqrt(n)

def test_raiz():
    assert raiz(9) ==3
    assert raiz(81) == 9
    assert raiz(144) == 12
    assert raiz(400) == 20
    assert raiz(196) == 14 

def greet(name):
    return f"Hello: {name}"

def test_greet():
    assert greet("World") == "Hello: World"

class Calculator:
    
    def add(self, x, y):
        return x + y
    
    def test_calculator():
        calc =  Calculator
        
        assert calc.add(1, 2) == 3
        assert calc.add(-4, 7) == 2

def eh_palindromo(s):
    return s == s[::-1]

@pytest.mark.parametrize("input, expected",[
    ("radar", True),
    ("refer", True),
    ("python", False),
    ("", True),  # Empty string is considered a palindrome
])

def test_eh_palindromo(input, expected):
    assert eh_palindromo(input) == expected

import unittest

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

class TestFatorial(unittest.TestCase):
    def test_fatorial_de_0(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_de_1(self):
        self.assertEqual(fatorial(1), 1)

    def test_fatorial_de_5(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_de_10(self):
        self.assertEqual(fatorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
