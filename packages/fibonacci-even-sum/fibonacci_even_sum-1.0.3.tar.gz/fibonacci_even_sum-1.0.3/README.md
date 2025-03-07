# Fibonacci Serisi Çift Sayılar Toplamı

[![Fibonacci Even Sum Test](https://github.com/huseyinaslim/fibonacci-even-sum/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/huseyinaslim/fibonacci-even-sum/actions/workflows/main.yml)
[![Downloads](https://img.shields.io/github/downloads/huseyinaslim/fibonacci-even-sum/total)](https://github.com/huseyinaslim/fibonacci-even-sum/releases)
[![PyPI](https://img.shields.io/pypi/v/fibonacci-even-sum)](https://pypi.org/project/fibonacci-even-sum/1.0.0/)
[![License](https://img.shields.io/github/license/huseyinaslim/fibonacci-even-sum)](https://github.com/huseyinaslim/fibonacci-even-sum/blob/main/LICENSE)

*Read this in [English](README.en.md)*

Bu proje, Fibonacci serisinin belirli bir sayıya kadar olan çift sayılarının toplamını hesaplayan bir Python komut satırı uygulamasıdır.

> **Not:** Bu proje, Başkent Üniversitesi BİL458 - Bulut Çözüme Giriş dersinin ödevi için Hüseyin ASLIM tarafından kodlanmıştır.

## Gereksinimler

- Python 3.6 veya daha yüksek bir sürüm
- Herhangi bir ek kütüphane gerektirmez (sadece standart Python kütüphaneleri kullanılmaktadır)

## Fibonacci Serisi Nedir?

Fibonacci serisi, her sayının kendisinden önceki iki sayının toplamı olduğu bir sayı dizisidir. Seri genellikle 0 ve 1 ile başlar:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

Bu projede, belirli bir N sayısına kadar olan Fibonacci serisindeki çift sayıların toplamını hesaplıyoruz.

## Kurulum

### GitHub'dan Kurulum

```bash
# Repoyu klonlayın
git clone https://github.com/huseyinaslim/fibonacci-even-sum.git
cd fibonacci-even-sum

# Çalıştırma izni verin (Unix/Linux/MacOS)
chmod +x fibonacci_even_sum.py
```

### PyPI'dan Kurulum (pip ile)

```bash
# PyPI'dan kurulum
pip install fibonacci-even-sum
```

Bu komut, en son sürümü PyPI'dan indirir ve kurar. Kurulumdan sonra, `fibonacci-even-sum` komutunu doğrudan kullanabilirsiniz:

```bash
fibonacci-even-sum 100
```

### Belirli Bir Sürümü Kurma

```bash
pip install fibonacci-even-sum==1.0.0
```

### Geliştirme Sürümünü Kurma

```bash
pip install -e .
```

Bu komut, projeyi geliştirme modunda kurar, böylece kodda yaptığınız değişiklikler anında etkili olur.

## Kullanım

Programı aşağıdaki gibi çalıştırabilirsiniz:

```bash
python3 fibonacci_even_sum.py N
```

veya Unix/Linux/MacOS sistemlerinde:

```bash
./fibonacci_even_sum.py N
```

Burada `N`, Fibonacci serisinin üst sınır değeridir.

Farklı algoritmaları kullanmak için:

```bash
# Doğrudan yöntem kullanarak hesapla
python3 fibonacci_even_sum.py N --direct

# Düzeltilmiş formül kullanarak hesapla
python3 fibonacci_even_sum.py N --formula
```

Algoritmaların performans karşılaştırmasını görmek için:

```bash
python3 fibonacci_even_sum.py N --compare
```

### Örnek

```bash
python3 fibonacci_even_sum.py 100
```

Bu komut, 100'e kadar olan Fibonacci serisindeki çift sayıların toplamını hesaplayacaktır.

## Testler

Bu proje, tüm algoritmaların doğru çalıştığını doğrulamak için unit testler içermektedir. Testleri çalıştırmak için:

```bash
python3 -m unittest test_fibonacci_even_sum.py
```

veya doğrudan test dosyasını çalıştırarak:

```bash
python3 test_fibonacci_even_sum.py
```

### Test Senaryoları

Testler şu senaryoları içermektedir:

1. **Küçük Değerler Testi**: 0, 1, 2, 8, 10, 34 ve 100 gibi küçük değerler için tüm algoritmaların doğru sonuç verdiğini kontrol eder.
2. **Orta Büyüklükte Değer Testi**: 4.000.000 değeri için tüm algoritmaların doğru sonuç verdiğini kontrol eder.
3. **Büyük Değer Testi**: 10^18 (1.000.000.000.000.000.000) gibi büyük bir değer için tüm algoritmaların aynı sonucu verdiğini kontrol eder.
4. **Negatif Değer Testi**: Negatif değerler için tüm algoritmaların 0 döndürdüğünü kontrol eder.

## Algoritma Optimizasyonu

Bu projede, Fibonacci serisinin çift sayılarının toplamını hesaplamak için dört farklı algoritma kullanılmıştır:

1. **Orijinal Algoritma**: Tüm Fibonacci sayılarını hesaplar ve çift olanları toplar.
2. **Optimize Edilmiş Algoritma**: Fibonacci serisinde her 3. sayının çift olduğu gerçeğinden yararlanarak, sadece çift Fibonacci sayılarını hesaplar.
3. **Doğrudan Yöntem**: Standart Fibonacci hesaplamasını kullanır, ancak sadece çift sayıları toplar.
4. **Düzeltilmiş Formül**: İteratif bir yaklaşımla çift Fibonacci sayılarını hesaplar.

### Performans Karşılaştırması

Aşağıdaki performans karşılaştırması, belirtilen donanım ve yazılım konfigürasyonunda gerçekleştirilmiştir:

**Sistem Bilgileri:**
- **İşlemci:** Apple M1
- **Bellek:** 8 GB RAM
- **İşletim Sistemi:** macOS Darwin 24.3.0
- **Python Sürümü:** Python 3.11.0

N = 10.000.000.000.000.000.000 için performans karşılaştırması:

| Algoritma | Çalışma Süresi (saniye) | Hızlanma Oranı |
|-----------|-------------------------|----------------|
| Optimize Edilmiş Algoritma | 0.00000286 | 2.17x |
| Orijinal Algoritma | 0.00000620 | 1.00x |
| Doğrudan Yöntem | 0.00000715 | 0.87x |
| Düzeltilmiş Formül | 0.00000787 | 0.79x |

Optimize edilmiş algoritma, orijinal algoritmadan yaklaşık 2.17 kat daha hızlıdır. Doğrudan yöntem ve düzeltilmiş formül, bu test durumunda orijinal algoritmadan biraz daha yavaştır.

Tüm algoritmalar aynı sonucu vermektedir: 3.770.056.902.373.173.214

### Matematiksel İlişki ve Algoritmalar

Fibonacci serisinde çift sayılar arasında çeşitli matematiksel ilişkiler vardır. Bu projede kullanılan dört farklı algoritmanın matematiksel temelleri şöyledir:

#### 1. Orijinal Algoritma

Bu algoritma, standart Fibonacci hesaplamasını kullanır ve her adımda sayının çift olup olmadığını kontrol eder:

```python
a, b = 1, 2
total = 0

while b <= n:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
```

Zaman karmaşıklığı: O(log n), çünkü Fibonacci sayıları yaklaşık olarak φ^n hızında büyür (φ altın oran, yaklaşık 1.618).

#### 2. Optimize Edilmiş Algoritma

Fibonacci serisinde her 3. sayının çift olduğu matematiksel bir gerçektir. Ayrıca, çift Fibonacci sayıları arasında şu ilişki vardır:

```
F(n+6) = 4*F(n+3) + F(n)
```

Sadeleştirirsek:
```
F(n+3) = 4*F(n) + F(n-3)
```

Bu ilişkiyi kullanarak, sadece çift Fibonacci sayılarını hesaplayabiliriz:

```python
a, b = 0, 2  # İlk çift Fibonacci sayısı 2'dir
total = 0

while b <= n:
    total += b
    a, b = b, 4*b + a  # F(n+3) = 4*F(n) + F(n-3)
```

Zaman karmaşıklığı: O(log n / 3), çünkü sadece her 3. Fibonacci sayısını hesaplıyoruz.

#### 3. Doğrudan Yöntem

Bu yöntem, standart Fibonacci hesaplamasını kullanır, ancak üç sayıyı takip ederek her adımda bir sonraki Fibonacci sayısını hesaplar:

```python
a, b, c = 1, 1, 2  # F(1), F(2), F(3)
total = 0

while c <= n:
    if c % 2 == 0:  # Çift sayı kontrolü
        total += c
    a, b, c = b, c, b + c
```

Zaman karmaşıklığı: O(log n), orijinal algoritma ile aynıdır.

#### 4. Düzeltilmiş Formül

Bu yöntem, Fibonacci sayılarının genel formülünü kullanmak yerine, iteratif bir yaklaşımla çift Fibonacci sayılarını hesaplar:

```python
f1, f2, f3 = 1, 1, 2  # F(1), F(2), F(3)
total = 0

while f3 <= n:
    if f3 % 2 == 0:  # Çift sayı kontrolü
        total += f3
    f1, f2, f3 = f2, f3, f2 + f3
```

Zaman karmaşıklığı: O(log n), diğer iteratif yöntemlerle aynıdır.

### Binet Formülü

Fibonacci sayılarını hesaplamak için kapalı bir formül olan Binet formülü şöyledir:

```
F(n) = (φ^n - (-φ)^(-n)) / √5
```

Burada φ = (1 + √5) / 2 ≈ 1.618 (altın oran) ve n, Fibonacci sayısının indeksidir.

Bu formül, büyük Fibonacci sayılarını doğrudan hesaplamak için kullanılabilir, ancak büyük n değerleri için hassasiyet sorunları yaşanabilir.

## Örnekler

- `N = 10` için çıktı: 10 (2 + 8 = 10)
- `N = 34` için çıktı: 44 (2 + 8 + 34 = 44)
- `N = 100` için çıktı: 44 (2 + 8 + 34 = 44)
- `N = 4000000` için çıktı: 4613732 (2 + 8 + 34 + 144 + 610 + 2584 + 10946 + 46368 + 196418 + 832040 + 3524578 = 4613732)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın. 