from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ghdemo",
    author="vgarzon8",
    description="Example module for GitHub demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    version="0.1.0",
    license="MIT",
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["ghdemo=ghdemo.cli:main"],
    },
)
