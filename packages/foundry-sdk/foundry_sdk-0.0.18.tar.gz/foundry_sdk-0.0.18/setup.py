import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="foundry-sdk",
    version="0.0.18",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
