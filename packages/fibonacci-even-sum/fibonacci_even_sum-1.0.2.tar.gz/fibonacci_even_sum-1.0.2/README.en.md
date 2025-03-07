# Even Sum of Fibonacci Series

[![Tests](https://img.shields.io/github/workflow/status/huseyinaslim/fibonacci-even-sum/tests?label=tests)](https://github.com/huseyinaslim/fibonacci-even-sum/actions)
[![Downloads](https://img.shields.io/github/downloads/huseyinaslim/fibonacci-even-sum/total)](https://github.com/huseyinaslim/fibonacci-even-sum/releases)
[![PyPI](https://img.shields.io/pypi/v/fibonacci-even-sum)](https://pypi.org/project/fibonacci-even-sum/1.0.0/)
[![License](https://img.shields.io/github/license/huseyinaslim/fibonacci-even-sum)](https://github.com/huseyinaslim/fibonacci-even-sum/blob/main/LICENSE)

*Bu belgeyi [Türkçe](README.md) olarak oku*

This project is a Python command-line application that calculates the sum of even numbers in the Fibonacci series up to a given number.

> **Note:** This project was coded by Hüseyin ASLIM for the assignment of Başkent University BİL458 - Introduction to Cloud Solutions course.

## Requirements

- Python 3.6 or higher
- No additional libraries required (only standard Python libraries are used)

## What is the Fibonacci Series?

The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones. The series typically starts with 0 and 1:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

In this project, we calculate the sum of even numbers in the Fibonacci series up to a given number N.

## Installation

### Installation from GitHub

```bash
# Clone the repository
git clone https://github.com/huseyinaslim/fibonacci-even-sum.git
cd fibonacci-even-sum

# Give execution permission (Unix/Linux/MacOS)
chmod +x fibonacci_even_sum.py
```

### Installation from PyPI (with pip)

```bash
# Installation from PyPI
pip install fibonacci-even-sum
```

This command downloads and installs the latest version from PyPI. After installation, you can use the `fibonacci-even-sum` command directly:

```bash
fibonacci-even-sum 100
```

### Installing a Specific Version

```bash
pip install fibonacci-even-sum==1.0.0
```

### Installing in Development Mode

```bash
pip install -e .
```

This command installs the project in development mode, so changes you make to the code take effect immediately.

## Usage

You can run the program as follows:

```bash
python3 fibonacci_even_sum.py N
```

or on Unix/Linux/MacOS systems:

```bash
./fibonacci_even_sum.py N
```

Here, `N` is the upper limit of the Fibonacci series.

To use different algorithms:

```bash
# Calculate using direct method
python3 fibonacci_even_sum.py N --direct

# Calculate using corrected formula
python3 fibonacci_even_sum.py N --formula
```

To see a performance comparison of the algorithms:

```bash
python3 fibonacci_even_sum.py N --compare
```

### Example

```bash
python3 fibonacci_even_sum.py 100
```

This command will calculate the sum of even numbers in the Fibonacci series up to 100.

## Tests

This project includes unit tests to verify that all algorithms work correctly. To run the tests:

```bash
python3 -m unittest test_fibonacci_even_sum.py
```

or by directly running the test file:

```bash
python3 test_fibonacci_even_sum.py
```

### Test Scenarios

The tests include the following scenarios:

1. **Small Values Test**: Checks that all algorithms return the correct result for small values such as 0, 1, 2, 8, 10, 34, and 100.
2. **Medium Value Test**: Checks that all algorithms return the correct result for the medium-sized value of 4,000,000.
3. **Large Value Test**: Checks that all algorithms return the same result for a large value like 10^18 (1,000,000,000,000,000,000).
4. **Negative Value Test**: Checks that all algorithms return 0 for negative values.

## Algorithm Optimization

This project uses four different algorithms to calculate the sum of even numbers in the Fibonacci series:

1. **Original Algorithm**: Calculates all Fibonacci numbers and sums the even ones.
2. **Optimized Algorithm**: Takes advantage of the fact that every 3rd number in the Fibonacci series is even, and only calculates the even Fibonacci numbers.
3. **Direct Method**: Uses standard Fibonacci calculation but only sums the even numbers.
4. **Corrected Formula**: Calculates even Fibonacci numbers using an iterative approach.

### Performance Comparison

The following performance comparison was conducted on the specified hardware and software configuration:

**System Information:**
- **Processor:** Apple M1
- **Memory:** 8 GB RAM
- **Operating System:** macOS Darwin 24.3.0
- **Python Version:** Python 3.11.0

Performance comparison for N = 10,000,000,000,000,000,000:

| Algorithm | Execution Time (seconds) | Speed-up Ratio |
|-----------|--------------------------|----------------|
| Optimized Algorithm | 0.00000286 | 2.17x |
| Original Algorithm | 0.00000620 | 1.00x |
| Direct Method | 0.00000715 | 0.87x |
| Corrected Formula | 0.00000787 | 0.79x |

The optimized algorithm is approximately 2.17 times faster than the original algorithm. The direct method and corrected formula are slightly slower than the original algorithm in this test case.

All algorithms produce the same result: 3,770,056,902,373,173,214

### Mathematical Relationships and Algorithms

There are various mathematical relationships between even numbers in the Fibonacci series. The mathematical foundations of the four different algorithms used in this project are as follows:

#### 1. Original Algorithm

This algorithm uses the standard Fibonacci calculation and checks if each number is even at each step:

```python
a, b = 1, 2
total = 0

while b <= n:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
```

Time complexity: O(log n), because Fibonacci numbers grow at a rate of approximately φ^n (φ is the golden ratio, approximately 1.618).

#### 2. Optimized Algorithm

It is a mathematical fact that every 3rd number in the Fibonacci series is even. Additionally, there is the following relationship between even Fibonacci numbers:

```
F(n+6) = 4*F(n+3) + F(n)
```

Simplified:
```
F(n+3) = 4*F(n) + F(n-3)
```

Using this relationship, we can calculate only the even Fibonacci numbers:

```python
a, b = 0, 2  # First even Fibonacci number is 2
total = 0

while b <= n:
    total += b
    a, b = b, 4*b + a  # F(n+3) = 4*F(n) + F(n-3)
```

Time complexity: O(log n / 3), because we only calculate every 3rd Fibonacci number.

#### 3. Direct Method

This method uses the standard Fibonacci calculation but tracks three numbers to calculate the next Fibonacci number at each step:

```python
a, b, c = 1, 1, 2  # F(1), F(2), F(3)
total = 0

while c <= n:
    if c % 2 == 0:  # Check if even
        total += c
    a, b, c = b, c, b + c
```

Time complexity: O(log n), same as the original algorithm.

#### 4. Corrected Formula

This method calculates even Fibonacci numbers using an iterative approach rather than using the general formula for Fibonacci numbers:

```python
f1, f2, f3 = 1, 1, 2  # F(1), F(2), F(3)
total = 0

while f3 <= n:
    if f3 % 2 == 0:  # Check if even
        total += f3
    f1, f2, f3 = f2, f3, f2 + f3
```

Time complexity: O(log n), same as other iterative methods.

### Binet's Formula

Binet's formula is a closed-form expression for calculating Fibonacci numbers:

```
F(n) = (φ^n - (-φ)^(-n)) / √5
```

Where φ = (1 + √5) / 2 ≈ 1.618 (golden ratio) and n is the index of the Fibonacci number.

This formula can be used to directly calculate large Fibonacci numbers, but precision issues may occur for large values of n.

## Examples

- Output for `N = 10`: 10 (2 + 8 = 10)
- Output for `N = 34`: 44 (2 + 8 + 34 = 44)
- Output for `N = 100`: 44 (2 + 8 + 34 = 44)
- Output for `N = 4000000`: 4613732 (2 + 8 + 34 + 144 + 610 + 2584 + 10946 + 46368 + 196418 + 832040 + 3524578 = 4613732)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.