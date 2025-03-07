# hello_world/
# └── hello_world/
# ├   ├── __init__.py
# ├   └── main.py
# ├── setup.py
# └── README.md

from setuptools import setup, find_packages

setup(
    name= "vannyy_nyoba_pypi",
    version = "0.1",
    packages = find_packages(),
    install_requires=[
        #add dependecies here kyk 'numpy>=1.11'
    ],
)