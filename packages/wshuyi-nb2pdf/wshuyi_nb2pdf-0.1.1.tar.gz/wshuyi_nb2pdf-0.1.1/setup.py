#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wshuyi-nb2pdf",
    version="0.1.1",
    author="WSY",
    author_email="wsy@example.com",
    description="将Jupyter Notebook转换为优化的PDF格式，确保代码完整显示且不被截断",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/wshuyi-nb2pdf",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "jupyter",
        "nbconvert>=6.0.0",
        "playwright>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "wshuyi-nb2pdf=wshuyi_nb2pdf.cli:main",
        ],
    },
)
