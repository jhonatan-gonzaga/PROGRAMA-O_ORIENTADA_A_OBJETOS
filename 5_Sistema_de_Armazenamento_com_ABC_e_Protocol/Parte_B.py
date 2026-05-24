from typing import Protocol, Any, runtime_checkable

@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado: Any) -> None:
        pass


class ArmazenadorNuvem:
    def __init__(self):
        self.dados = []

    def salvar(self, dado: Any) -> None:
        self.dados.append(dado)
        # ADICIONE ESSE PRINT AQUI:
        print(f"Sucesso! Dado '{dado}' armazenado de forma flexível na nuvem.")