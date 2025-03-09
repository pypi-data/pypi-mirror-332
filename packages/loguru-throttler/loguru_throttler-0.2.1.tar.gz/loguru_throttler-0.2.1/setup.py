"""
Setup script for loguru-throttler package.
"""

from setuptools import find_packages, setup

# Read the contents of README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="loguru-throttler",
    version="0.2.1",
    description="A package for throttling duplicate log messages in loguru",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Author",
    author_email="author@example.com",
    url="https://github.com/yourusername/loguru-throttler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "loguru>=0.6.0",
    ],
)
