from setuptools import setup, find_packages

setup(
    name="solnir",
    version="0.1.8",
    packages=find_packages(),
    install_requires=[
        "pika",
    ],
)
