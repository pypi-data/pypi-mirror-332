from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="foundry_db_temp",
    version="0.1.10",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)
