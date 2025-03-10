from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simplemt5",
    version="0.1.0",
    author="SimpleMT5 Developer",
    author_email="your.email@example.com",
    description="Упрощенная библиотека для работы с MetaTrader 5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simplemt5",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "MetaTrader5>=5.0.0",
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
) 