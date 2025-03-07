# setup.py

from setuptools import setup, find_packages

setup(
    name="errorcode-sdk",
    version="0.1.0",
    description="A simple SDK for retrieving error codes",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
