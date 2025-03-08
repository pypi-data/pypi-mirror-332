from setuptools import setup, find_packages

setup(
    name="G-BAYSED",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "astropy",
        "matplotlib",
        "emcee",
        "corner",
    ],  # Directly specifying dependencies
    author="Golshan Ejlali",
    description="A package for SED modeling using Bayesian MCMC",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gejlali/G-BAYSED",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
    ],
)
