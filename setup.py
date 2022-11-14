# O arquivo setup deve ficar na raiz no projeto. Não dentro
# do programa principal (dundie).

# Ferramentas de configurar setup:
# - setuptools
# - pyproject
import os
from importlib.metadata import entry_points
from setuptools import find_packages, setup

def read(*paths): #função criada para autoimatizar a leitura dos arquivos de  requirements
    """Read the coontents of a text file safely.
    >>>read("dundie", "VERSION")
    '0.1.0'
    >>>read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__) # é uma forma de pegar o caminho do arquivo atual "setup.py"
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()

def read_requirements(path):#função criada para autoimatizar a leitura dos arquivos de  requirements
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startwith(("#", "git+", '"',))
    ] #listcomprehesion

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Edmar Almeida",
    packages=find_packages(), #Esse argumento serve para especificar quais módulos do
    # projeto serão empacotados. No nosso caso, podemos colocar somente o ["dundie"].
    # Outra opção é colocar a função find_packages() como argumento. Nesse caso, 
    # a função adiciona todos os pacotes que tem o __init__. 
    # Por isso a importância de colocar __init__ dentro dos módulos.,
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
            ]
    },
     # metadado de configuração para criar comando CIL (linha de comando).

    # O controle de dependências também é feito no arquivo setup.py
    install_requires=read_requirements("requirements.txt"), #utilização da func para facilitar a leitura 
    # dos requirements - toda vez que precisarmos acrescentar dependências novas ao projeto,
    # não precisa editar o setup.py, basta ir no arquivo requirements.txt e incluir
    extras_require={
        "test": read_requirements("requirements.tes.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    }
)
