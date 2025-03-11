from setuptools import setup, find_packages

setup(
    name="nanako-utils",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib",
    ],
    python_requires=">=3.8",
    license="MIT",
)
