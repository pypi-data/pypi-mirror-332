# setup.py
from setuptools import setup, find_packages

setup(
    name="neuroslides",  # Your package name (must be unique on PyPI)
    version="0.1.0",
    description="A python package to generate slides for neuroslides presentations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Saboor Islam",
    author_email="muhammadsaboor119@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)