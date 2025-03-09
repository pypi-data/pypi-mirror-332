from setuptools import setup

requirements : list = ["pycryptodome" , "pillow" , "aiohttp" , "websocket-client"]

setup(
    name = "RubAmin",
    version = "0.1.4",
    author = "Unique Amin",
    description = "t.me/Unique_Amin78",
    packages = ['RubAmin'],
    install_requires = requirements,
    classifiers = [],
)