class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"=== Funcionários da Empresa: {self.nome} ===")
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            # :.2f limita o pagamento a 2 casas decimais
            print(f"Pagamento: R$ {funcionario.calcular_pagamento():.2f}")
            print("---")
    
    def mostrar_folha_pagamento(self):
        total = sum(funcionario.calcular_pagamento() for funcionario in self.funcionarios)
        # :.2f aqui também para o total geral
        print(f"Total da folha de pagamento da {self.nome}: R$ {total:.2f}")