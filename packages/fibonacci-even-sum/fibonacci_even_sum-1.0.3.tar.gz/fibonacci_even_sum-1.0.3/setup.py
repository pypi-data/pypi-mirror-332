#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fibonacci-even-sum",
    version="1.0.3",
    author="Hüseyin ASLIM",
    author_email="founder@codev.com.tr",
    description="Fibonacci serisinin çift sayılarının toplamını hesaplayan bir Python CLI uygulaması",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huseyinaslim/fibonacci-even-sum",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fibonacci-even-sum=fibonacci_even_sum:main",
        ],
    },
    license="MIT",
) 