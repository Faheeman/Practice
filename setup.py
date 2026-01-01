from setuptools import setup, find_packages
from typing import List


def get_requirements(path: str) -> List[str]:
    """
    Reads requirements.txt and filters out editable installs like '-e .'
    """
    requirements = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line and line != "-e .":
                requirements.append(line)
    return requirements


setup(
    name="practice",
    version="0.1.0",
    author="Fahim Hasan",
    author_email="hasanfahim0101@gmail.com",
    packages=find_packages(exclude=("tests",)),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
