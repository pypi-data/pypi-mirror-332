#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fibonacci serisinin belirli bir sayıya kadar olan çift sayılarının toplamını hesaplayan program.
Süper optimize edilmiş versiyon.
"""

import argparse
import sys
import time
import math


def fibonacci_even_sum_formula(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını
    kapalı formül kullanarak hesaplar.
    
    Args:
        n (int): Üst sınır değeri
        
    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0
    
    # Fibonacci serisinde çift sayılar F(3), F(6), F(9), ... şeklindedir
    # Yani F(3k) şeklinde ifade edilebilir (k=1,2,3,...)
    
    # Doğrudan iteratif yöntem kullanarak çift Fibonacci sayılarını hesaplayalım
    # ve n'den küçük veya eşit olan son çift Fibonacci sayısını bulalım
    
    # İlk üç Fibonacci sayısı
    f1, f2, f3 = 1, 1, 2  # F(1), F(2), F(3)
    
    # İlk çift Fibonacci sayısı F(3) = 2
    total = 0
    
    while f3 <= n:
        if f3 % 2 == 0:  # Çift sayı kontrolü (aslında her F(3k) çifttir)
            total += f3
        
        # Bir sonraki Fibonacci sayısını hesapla
        f1, f2, f3 = f2, f3, f2 + f3
    
    return total


def fibonacci_even_sum_direct(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını
    doğrudan çift Fibonacci sayılarını hesaplayarak bulur.
    
    Args:
        n (int): Üst sınır değeri
        
    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0
    
    # Fibonacci serisinde çift sayılar F(3), F(6), F(9), ... şeklindedir
    # Yani her 3. sayı çifttir
    
    # İlk çift Fibonacci sayısı 2'dir
    a, b, c = 1, 1, 2
    total = 0
    
    while c <= n:
        if c % 2 == 0:  # Çift sayı kontrolü
            total += c
        
        # Bir sonraki Fibonacci sayısını hesapla
        a, b, c = b, c, b + c
    
    return total


def fibonacci_even_sum(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını hesaplar.
    Optimize edilmiş iteratif yöntem.
    
    Args:
        n (int): Üst sınır değeri
        
    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0
    
    # Fibonacci serisinde her 3. sayı çifttir
    # F(3k) = 4*F(3k-3) + F(3k-6)
    # Bu özelliği kullanarak sadece çift Fibonacci sayılarını hesaplayabiliriz
    a, b = 0, 2  # İlk çift Fibonacci sayısı 2'dir
    total = 0
    
    while b <= n:
        total += b
        # Bir sonraki çift Fibonacci sayısını hesapla
        # F(n+3) = 4*F(n) + F(n-3)
        a, b = b, 4*b + a
        
    return total


def fibonacci_even_sum_original(n):
    """
    Orijinal yöntem - karşılaştırma için.
    """
    if n < 2:
        return 0
    
    a, b = 1, 2
    total = 0
    
    while b <= n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
        
    return total


def main():
    """Ana program fonksiyonu."""
    parser = argparse.ArgumentParser(
        description="Fibonacci serisinin belirli bir sayıya kadar olan çift sayılarının toplamını hesaplar."
    )
    parser.add_argument(
        "number", 
        type=int, 
        help="Fibonacci serisinin üst sınır değeri"
    )
    parser.add_argument(
        "--compare", 
        action="store_true",
        help="Tüm algoritmaları karşılaştır"
    )
    parser.add_argument(
        "--formula", 
        action="store_true",
        help="Kapalı formül kullanarak hesapla"
    )
    parser.add_argument(
        "--direct", 
        action="store_true",
        help="Doğrudan yöntem kullanarak hesapla"
    )
    
    args = parser.parse_args()
    
    if args.number < 0:
        print("Lütfen pozitif bir sayı giriniz.")
        sys.exit(1)
    
    if args.formula:
        # Kapalı formül kullanarak hesapla
        result = fibonacci_even_sum_formula(args.number)
        print(f"Fibonacci serisinin {args.number} sayısına kadar olan çift sayılarının toplamı: {result}")
        return
    
    if args.direct:
        # Doğrudan yöntem kullanarak hesapla
        result = fibonacci_even_sum_direct(args.number)
        print(f"Fibonacci serisinin {args.number} sayısına kadar olan çift sayılarının toplamı: {result}")
        return
    
    if args.compare:
        # Performans karşılaştırması
        print(f"N = {args.number} için performans karşılaştırması:")
        
        # Düzeltilmiş formül
        start_time = time.time()
        result_formula = fibonacci_even_sum_formula(args.number)
        end_time = time.time()
        time_formula = end_time - start_time
        
        # Doğrudan yöntem
        start_time = time.time()
        result_direct = fibonacci_even_sum_direct(args.number)
        end_time = time.time()
        time_direct = end_time - start_time
        
        # Optimize edilmiş algoritma
        start_time = time.time()
        result1 = fibonacci_even_sum(args.number)
        end_time = time.time()
        time1 = end_time - start_time
        
        # Orijinal algoritma
        start_time = time.time()
        result2 = fibonacci_even_sum_original(args.number)
        end_time = time.time()
        time2 = end_time - start_time
        
        print(f"Düzeltilmiş formül: {time_formula:.8f} saniye")
        print(f"Doğrudan yöntem: {time_direct:.8f} saniye")
        print(f"Optimize edilmiş algoritma: {time1:.8f} saniye")
        print(f"Orijinal algoritma: {time2:.8f} saniye")
        
        print(f"\nHızlanma oranları:")
        print(f"Düzeltilmiş formül / Orijinal: {time2/time_formula:.2f}x")
        print(f"Doğrudan yöntem / Orijinal: {time2/time_direct:.2f}x")
        print(f"Optimize edilmiş / Orijinal: {time2/time1:.2f}x")
        
        print(f"\nSonuçlar:")
        print(f"Düzeltilmiş formül = {result_formula}")
        print(f"Doğrudan yöntem = {result_direct}")
        print(f"Optimize edilmiş = {result1}")
        print(f"Orijinal = {result2}")
        
        print(f"\nSonuçlar eşit mi: {result_formula == result_direct == result1 == result2}")
    else:
        # Normal çalıştırma
        result = fibonacci_even_sum(args.number)
        print(f"Fibonacci serisinin {args.number} sayısına kadar olan çift sayılarının toplamı: {result}")


if __name__ == "__main__":
    main() 