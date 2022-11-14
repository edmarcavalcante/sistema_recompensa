# O arquivo setup deve ficar na raiz no projeto. Não dentro
# do programa principal (dundie).

# Ferramentas de configurar setup:
# - setuptools
# - pyproject

from importlib.metadata import entry_points
from setuptools import find_packages, setup

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
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
    }
     # metadado de configuração para criar comando CIL (linha de comando).

    install_requires=[] # O controle de dependências também é feito no arquivo setup.py
    extras_require={
        "test": [
            "pytest"
        ],
        "dev": [
            "ipdb",
            "ipython",
            "pudb"
        ],
    }
)