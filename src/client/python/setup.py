from setuptools import setup, find_packages

setup(
    name="openmcp-cardano",
    version="0.1.0",
    packages=find_packages(include=["openmcp_cardano", "openmcp_cardano.*"]),
    install_requires=[],
    python_requires=">=3.10",
) 