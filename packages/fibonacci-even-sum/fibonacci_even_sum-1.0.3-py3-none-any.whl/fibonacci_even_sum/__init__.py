#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fibonacci serisinin belirli bir sayıya kadar olan çift sayılarının
toplamını hesaplayan paket.
"""

__version__ = "1.0.3"
__author__ = "Hüseyin ASLIM"

# Dışa aktarılan fonksiyonlar - noqa ile uyarıları bastırıyoruz
# çünkü bu importlar paket API'sinin bir parçası
from .fibonacci_even_sum import (  # noqa
    fibonacci_even_sum,
    fibonacci_even_sum_original,
    fibonacci_even_sum_direct,
    fibonacci_even_sum_formula,
    main
)
