from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="TurboCLI",
    version="0.2.1",
    packages=find_packages(),
    author="Juho Jokisalo",
    author_email="xboxj2012@gmail.com",
    description="A simple Python package for CLI tools",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specifies markdown format
    url="https://github.com/TheDoubleMix/cli", 
    classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
],
    python_requires=">=3.7",
)
