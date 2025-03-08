import argparse
from collections import defaultdict

NUMPY_MIN_VERSION = "2.0.1"
PANDAS_MIN_VERSION = "2.2.2"
SCIKIT_MIN_VERSION = "1.5.1"
NUMBA_MIN_VERSION = "0.60.0"
PYTEST_MIN_VERSION = "8.3.2"
SEABORN_MIN_VERSION = "0.13.2"
MATPLOTLIB_MIN_VERSION = "3.9.0"
SETUPTOOLS_MIN_VERSION = "75.1.0"
REQUESTS_MIN_VERSION = "2.32.3"

dependent_packages = {
    "numpy": (NUMPY_MIN_VERSION, "build, install"),
    "pandas": (PANDAS_MIN_VERSION, "build, install"),
    "scikit-learn": (SCIKIT_MIN_VERSION, "build, install"),
    "numba": (NUMBA_MIN_VERSION, "build, install"),
    "seaborn": (SEABORN_MIN_VERSION, "build, install"),
    "matplotlib": (MATPLOTLIB_MIN_VERSION, "build, install"),
    "setuptools": (SETUPTOOLS_MIN_VERSION, "build, install"),
    "requests": (REQUESTS_MIN_VERSION, "build, install"),
    "pytest": (PYTEST_MIN_VERSION, "tests"),
    "pytest-cov": ("2.9.0", "tests"),
}

tag_to_packages: dict = defaultdict(list)
for package, (min_version, extras) in dependent_packages.items():
    for extra in extras.split(", "):
        tag_to_packages[extra].append("{}>={}".format(package, min_version))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get min dependencies for a package")
    parser.add_argument("package", choices=dependent_packages)
    args = parser.parse_args()
    min_version = dependent_packages[args.package][0]
    print(min_version)