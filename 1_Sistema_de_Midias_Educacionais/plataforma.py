class plataforma:
    def __init__(self, nome, lista_midias):
        self.nome = nome
        self.lista_midias =[]
    
    def adicionar_midia(self, midia):
        self.lista_midias.append(midia)
    
    def lista_midia(self):
        for midia in self.lista_midias:
            midia.mostrar_info()
    
    def reproduzir_todas(self):
        for midia in self.lista_midias:
            midia.reproduzir()
    
    