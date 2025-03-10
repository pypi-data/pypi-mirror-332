from setuptools import setup, find_packages

setup(
    name="PrivyDNS",
    version="0.1.0",
    description="A Python library for secure DNS resolution (DoH, DoT, mTLS) with sync & async support.",
    author="Nicholas Adamou",
    author_email="nicholas.adamou@outlook.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
    ],
)
