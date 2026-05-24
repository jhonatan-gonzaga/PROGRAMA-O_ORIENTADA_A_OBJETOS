from funcionario import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from empresa import Empresa

def main():
    empresa = Empresa("Exemplo Ltda.")

    # Criando funcionários
    func1 = FuncionarioAssalariado("João", "123.456.789-00", 3000.0)
    func2 = FuncionarioHorista("Maria", "987.654.321-00", 160, 25.0)
    func3 = FuncionarioComissionado("Pedro", "456.789.123-00", 10000.0, 0.1)

    # Adicionando funcionários à empresa
    empresa.adicionar_funcionario(func1)
    empresa.adicionar_funcionario(func2)
    empresa.adicionar_funcionario(func3)

    # Listando funcionários
    empresa.listar_funcionarios()

    # Mostrando folha de pagamento
    empresa.mostrar_folha_pagamento()

if __name__ == "__main__":
    main()