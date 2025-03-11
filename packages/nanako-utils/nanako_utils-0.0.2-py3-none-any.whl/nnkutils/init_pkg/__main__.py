from pathlib import Path

setup_py = """from setuptools import setup, find_packages

setup(
    name="{pypi_name}",
    version="0.1.0",
    packages=find_packages("src"),
    package_dir={{"": "src"}},
    install_requires=[],
)
"""

pyproject_toml = """[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
"""

init_py = """print("Congratulations! The package has been imported.")
"""


def main():
    print("This tool will create a new directory and init the project in it.")
    pypi_name = input("Enter the package name shown on PyPI: ")
    import_name = input("Enter the package name used for import: ")
    project_root = Path(pypi_name)
    project_root.mkdir(parents=True, exist_ok=True)
    src_dir = project_root / "src" / import_name
    src_dir.mkdir(parents=True, exist_ok=True)
    (src_dir / "__init__.py").write_text(init_py)
    (project_root / "setup.py").write_text(setup_py.format(pypi_name=pypi_name))
    (project_root / "pyproject.toml").write_text(pyproject_toml)
    print("Project initialized.")
    print("You can run the following commands to test:")
    print(f"$ cd {project_root}")
    print("$ pip install -e .")
    print(f"$ python -c 'import {import_name}'")
    print("$ pip uninstall -y {pypi_name}".format(pypi_name=pypi_name))


if __name__ == "__main__":
    main()
