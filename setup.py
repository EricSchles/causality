import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="causality",
    version="0.0.1",
    description="Yet another causal inference library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EricSchles/causality",
    author="Eric Schles",
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=[
        "causality",
        "causality.rct",
        "causality.hypothesis_tests.categorical_tests",
        "causality.hypothesis_tests.continuous_tests"
    ],
    include_package_data=True,
    install_requires=[
        "pandas", "numpy", "seaborn", "matplotlib",
        "scikit-learn",
    ],
)
