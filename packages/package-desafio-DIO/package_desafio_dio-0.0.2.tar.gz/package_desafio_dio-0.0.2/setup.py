from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_desafio_DIO",
    version="0.0.2",
    author="Nelson Henrique",
    author_email="nhoblumer@hotmail.com",
    description="estudo de criação de pacotes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nhoblumer/desafio_estudo.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)