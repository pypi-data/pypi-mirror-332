#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, find_namespace_packages
import os
import re

# 从__init__.py中读取版本号
with open(os.path.join('converter', '__init__.py'), 'r', encoding='utf-8') as f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        version = '1.0.0'

# 读取README.md作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 从requirements.txt读取依赖
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="tl-markdown-converter",
    version=version,
    author="TL",
    author_email="ttieli@gmail.com",
    description="A powerful and flexible Markdown converter supporting multiple output formats and templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fiction/markdown-converter",
    packages=find_namespace_packages(include=['converter*']),
    include_package_data=True,
    package_data={
        'converter.templates': [
            '*/template.html',
            '*/style.css',
            '*/script.js',
            '*/config.json',
            '*/template.json',
            '*/preview.png',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "md-converter=converter.cli:main",
        ],
    },
) 