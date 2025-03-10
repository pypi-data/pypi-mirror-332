from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="if_etl_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[req for req in requirements if not req.startswith("git+")],
    dependency_links=[req for req in requirements if req.startswith("git+")],
)
