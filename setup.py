from setuptools import setup, find_packages


setup(
    name="TextExploration",
    version="0.1",
    author="Matthijs Brouwer",
    packages=find_packages(),
    license="LICENSE.txt",
    long_description=open("README.txt").read(),
    install_requires=[
        "requests >= 2.21.0",
        "pandas",
    ],
)

