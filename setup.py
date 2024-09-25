from setuptools import setup

setup(
    name="cookiecutter",
    version="0.12",
    py_modules=["cookiecutter"],
    description="Pacote para operacoes aritmeticas basicas",
    author="Britto",
    author_email="jbritto@universo.univates.br",
    url="https://github.com/jbrittoAD/teste_pip_install_operacoes/tree/main/operacoes",
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)