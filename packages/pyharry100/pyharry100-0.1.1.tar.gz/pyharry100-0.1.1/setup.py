from setuptools import setup, find_packages

setup(
    name="pyharry100",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "pyharry100=pyharry100.main:main",
        ],
    },
    author="Muhammad Zain Zameer",
    author_email="officialmuhammadzain45@gmail.com",
    description="A CLI tool designed to help beginners efficiently learn Python through the 100 Days of Code challenge by CodeWithHarry. It provides structured learning with notes, extra in-depth notes, tasks, and additional challenges. Users can also explore recommended content for deeper knowledge after each day's video.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zain-Zameer/pyharry100",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
