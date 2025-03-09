from setuptools import setup, find_packages

setup (
    name="nerimity",
    version="1.2.1",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.11.13",
        "websockets>=15.0.1",
        "requests>=2.32.3"
    ]

)