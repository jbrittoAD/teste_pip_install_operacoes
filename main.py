import os

# Definindo o nome do projeto e os arquivos que serão criados
project_name = "operacoes"
files = {
    "operacoes.py": '''class Operacoes:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def soma(self, valor):
        return self.valor + valor

    def subtracao(self, valor):
        return self.valor - valor
''',
    "setup.py": '''from setuptools import setup

setup(
    name="operacoes",
    version="0.1",
    py_modules=["operacoes"],
    description="Pacote para operações aritméticas básicas",
    author="Seu Nome",
    author_email="seuemail@example.com",
    url="https://github.com/seuusuario/operacoes",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
''',
    "README.md": "# Operações\n\nPacote para operações aritméticas básicas.",
    "__init__.py": ""  # Arquivo vazio para marcar o pacote como módulo
}

# Criando a estrutura de diretórios
if not os.path.exists(project_name):
    os.mkdir(project_name)

# Criando os arquivos com o conteúdo especificado
for filename, content in files.items():
    with open(os.path.join(project_name, filename), "w") as f:
        f.write(content)

"Projeto e arquivos criados com sucesso."
