class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            print(f"Pagamento: {funcionario.calcular_pagamento()}")
            print("---")
    
    def mostrar_folha_pagamento(self):
        total = sum(funcionario.calcular_pagamento() for funcionario in self.funcionarios)
        print(f"Total da folha de pagamento: {total}")