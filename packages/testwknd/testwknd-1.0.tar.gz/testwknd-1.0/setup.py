import setuptools
from pathlib import Path

setuptools.setup(
    name="testwknd",
    version=1.0,
    long_description="",
    packages=setuptools.find_packages(exclude=["test", "data"])
)
