from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="criar_pacote_processamento",
    version="0.1",
    author="Pablo Fernandes",
    author_email="pabloafer10@hotmail.com",
    description="Bootcamp Dio",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pabloafer10/desafio_criar_pacote_processamento",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)