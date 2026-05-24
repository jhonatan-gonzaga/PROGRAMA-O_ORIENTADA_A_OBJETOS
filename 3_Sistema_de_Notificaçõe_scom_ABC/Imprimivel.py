from typing import Protocol

class Imprimivel(Protocol):
    def imprimir(self):
        pass


class Boleto:
    def __init__(self, codigo, valor, requisito):
        self.valor = valor
        self.codigo = codigo
        self.requisito = requisito

    def imprimir(self) -> None:
        print(f"Imprimindo boleto {self.codigo} no valor de: R$ {self.valor:.2f}")


class Etiqueta:
    def __init__(self, destinatario, endereco, requisito):
        self.destinatario = destinatario
        self.endereco = endereco
        self.requisito = requisito

    def imprimir(self) -> None:
        print(f"Imprimindo etiqueta para {self.destinatario} no endereço: {self.endereco} com requisito: {self.requisito}")


class RelatorioSimples:
    def __init__(self, titulo, requisito):
        self.titulo = titulo
        self.requisito = requisito

    def imprimir(self) -> None:
        print(f"Imprimindo relatório simples: {self.titulo} com requisito: {self.requisito}")


def processar_impressao(imprimivel: Imprimivel) -> None:
    imprimivel.imprimir()