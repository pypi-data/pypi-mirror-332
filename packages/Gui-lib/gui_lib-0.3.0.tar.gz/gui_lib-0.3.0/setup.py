# setup.py
from setuptools import setup, find_packages

setup(
    name="Gui_lib",
    version="0.3.0",
    packages=find_packages(),
    description="A simple GUI library similar to tkinter",
    author="OUBStudios",
    author_email="oubdocs.main@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
