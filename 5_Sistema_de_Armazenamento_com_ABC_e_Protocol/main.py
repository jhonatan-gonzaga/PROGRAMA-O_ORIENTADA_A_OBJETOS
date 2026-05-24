from Parte_A import Armazenador, ArmazenadorArquivo, ArmazenadorBanco
from Parte_B import Salvavel, ArmazenadorNuvem
from Parte_C import executar_salvamento_formal, executar_salvamento_flexivel

def main():
    armazenador_arquivo = ArmazenadorArquivo()
    armazenador_nuvem = ArmazenadorNuvem()
    dado = "Exemplo de dado"

    # Teste 1 (Formal - ABC)
    executar_salvamento_formal(armazenador_arquivo, dado)

    # Teste 2 (Flexível - Protocol)
    executar_salvamento_flexivel(armazenador_nuvem, dado)

if __name__ == "__main__":
    main()