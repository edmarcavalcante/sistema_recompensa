# Esse arquivo é o entry point do projeto. 
# Será o primeiro arquivo executado quando o projeto for iniciado\
# na linha de comando.

# Entry Point é o arquivo principal do projeto

# argparse - esse módulo é uma alternativa ao uso do sys.argv
# é mais fácil de  utilizar. Com ele não precisamos fazer algumas validações
# dos parâmetros passados. Ela estrutura os argumentos passados 
import argparse
import re
from unicodedata import name 

# First function that read the data.
def load(filepath):
    """Loads data from filepath to the database"""
    try:
        with open (filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")

def main():
    parser = argparse.ArgumentParser(
    description="Dunder Mifflin Rewards CLI",
    epilog = "Enjoy and use with cautions.",
    ) #Aqui foi instanciado o objeto parser
    
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default=help
    )# configurando os argumentos posicionais - nesse caso primeiro (subcomando)
    # será umas das opções: load, show ou send
    
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None
    ) # Essa instância configura o segundo argumento (o arquivo que será lido)
    
    args = parser.parse_args()

    try:
        globals()[args.subcommand](args.filepath)
    except  KeyError:
        print("Subcommand is invalid")

    
    if __name__ == "__main__":
        main()