from setuptools import setup, find_packages

setup(
    name="ofwat-dqchecks",
    version="0.0.16",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "numpy"
    ],
)
