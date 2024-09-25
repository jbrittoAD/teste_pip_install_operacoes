from setuptools import setup, find_packages

setup(
    name="cookiecutter",
    version="0.12",
    packages=find_packages(),  # Isso encontra automaticamente o pacote `cookiecutter`
    description="Pacote para operacoes aritmeticas basicas",
    author="Britto",
    author_email="jbritto@universo.univates.br",
    url="https://github.com/jbrittoAD/teste_pip_install_operacoes",  # Certifique-se de que a URL está correta
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
