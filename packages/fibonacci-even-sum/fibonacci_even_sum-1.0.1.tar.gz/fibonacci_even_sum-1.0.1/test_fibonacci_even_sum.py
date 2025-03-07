#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fibonacci serisinin çift sayılarının toplamını hesaplayan programın
unit testleri.
"""

import unittest
from fibonacci_even_sum import (
    fibonacci_even_sum,
    fibonacci_even_sum_original,
    fibonacci_even_sum_direct,
    fibonacci_even_sum_formula
)


class TestFibonacciEvenSum(unittest.TestCase):
    """Fibonacci çift sayılar toplamı için test sınıfı."""

    def test_small_values(self):
        """Küçük değerler için testler."""
        test_cases = [
            (0, 0),
            (1, 0),
            (2, 2),
            (8, 10),
            (10, 10),
            (34, 44),
            (100, 44),
        ]

        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci_even_sum(n), expected)
                self.assertEqual(fibonacci_even_sum_original(n), expected)
                self.assertEqual(fibonacci_even_sum_direct(n), expected)
                self.assertEqual(fibonacci_even_sum_formula(n), expected)

    def test_medium_value(self):
        """Orta büyüklükte değer için test."""
        n = 4000000
        expected = 4613732

        self.assertEqual(fibonacci_even_sum(n), expected)
        self.assertEqual(fibonacci_even_sum_original(n), expected)
        self.assertEqual(fibonacci_even_sum_direct(n), expected)
        self.assertEqual(fibonacci_even_sum_formula(n), expected)

    def test_large_value(self):
        """Büyük değer için test."""
        n = 10**18  # 1.000.000.000.000.000.000

        # Tüm algoritmaların aynı sonucu verdiğini kontrol et
        result1 = fibonacci_even_sum(n)
        result2 = fibonacci_even_sum_original(n)
        result3 = fibonacci_even_sum_direct(n)
        result4 = fibonacci_even_sum_formula(n)

        self.assertEqual(result1, result2)
        self.assertEqual(result1, result3)
        self.assertEqual(result1, result4)

    def test_negative_value(self):
        """Negatif değer için test."""
        n = -10
        expected = 0

        self.assertEqual(fibonacci_even_sum(n), expected)
        self.assertEqual(fibonacci_even_sum_original(n), expected)
        self.assertEqual(fibonacci_even_sum_direct(n), expected)
        self.assertEqual(fibonacci_even_sum_formula(n), expected)


if __name__ == "__main__":
    unittest.main()
