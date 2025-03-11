from setuptools import setup, find_packages


setup(
    name="ccxt-mexc_futures",
    version="0.1.6",
    packages=find_packages(),
    description="CCXT module for MEXC Futures API",
    author="",
    author_email="",
    url="",
    install_requires=[
        "ccxt",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 