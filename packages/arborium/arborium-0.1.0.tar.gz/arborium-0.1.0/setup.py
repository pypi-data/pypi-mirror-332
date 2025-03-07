from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arborium",
    version="0.1.0",
    author="Rishabh Mandayam",
    author_email="your.email@example.com",
    description="A tree visualization and analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/arborium",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires=">=3.6",
) 