from setuptools import setup, find_packages
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top-level
# README file and 2) it's easier to type in the README file than to put a raw string in below.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

# Utility function to load requirements from requirements.txt
def load_requirements(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        # Filter out comments and empty lines.
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="async_its_logger",
    version="0.1.0",
    author="Cristopher Serrato",
    author_email="cristopher.serrato@inmediatum.com",
    description="Asynchronous logger for high performance applications that incorporates multiple observers, logs in batches, and includes automatic retries and fallback if services are not available.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/inmediatum/asynch_its_logger.git",
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
