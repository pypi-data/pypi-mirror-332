from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Evan-Octo-Py",
    version="0.1.0",
    author="evanallen13",
    description="A Python library for managing GitHub Copilot, Rulesets, and Custom Properties",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evanallen13/octopy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "PyGithub>=1.55.0",
    ],
) 
