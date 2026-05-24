from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao}")
    
    @abstractmethod
    def reproduzir(self):
        pass


class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"Reproduzindo vídeo: {self.titulo} com resolução {self.resolucao}")

class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"Reproduzindo podcast: {self.titulo} com apresentador {self.apresentador}")


class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"Reproduzindo texto narrado: {self.titulo} com idioma {self.idioma}")

