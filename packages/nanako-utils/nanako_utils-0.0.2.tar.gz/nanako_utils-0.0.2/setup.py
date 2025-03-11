from setuptools import setup, find_packages

setup(
    name="nanako-utils",
    version="0.0.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib",
    ],
)
