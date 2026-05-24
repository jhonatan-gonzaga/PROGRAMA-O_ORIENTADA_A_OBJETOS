from abc import ABC, abstractmethod

class Armazenador(ABC):
    @abstractmethod
    def armazenar(self, dado):
        pass

class ArmazenadorArquivo(Armazenador):
    def armazenar(self, dado):
        
        print("Armazenando dado em arquivo...")

class ArmazenadorBanco(Armazenador):
    def armazenar(self, dado):
        # Implementação para armazenar em banco de dados
        print("Armazenando dado em banco de dados...")

def salva(dado, armazenador):
    armazenador.armazenar(dado) 