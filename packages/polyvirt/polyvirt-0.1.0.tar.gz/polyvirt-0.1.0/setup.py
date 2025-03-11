# setup.py
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="polyvirt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colored",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "polyvirt=polyvirt.main:main",
        ],
    },
    author="Dayton Jones",
    description="A CLI tool to manage Python virtual environments across multiple managers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)

