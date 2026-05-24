from Parte_A import Armazenador  # Importamos a classe abstrata mãe
from Parte_B import Salvavel

def executar_salvamento_formal(armazenador, dado):
    # O jeito FORMAL (ABC) checa se ele herda de Armazenador
    if isinstance(armazenador, Armazenador):
        armazenador.armazenar(dado)  # Usa o método correto da ABC
    else:
        raise TypeError("O objeto não herda da classe abstrata Armazenador")
    
def executar_salvamento_flexivel(objeto, dado):
    # O jeito FLEXÍVEL (Protocol) checa se ele se comporta como um Salvavel
    if isinstance(objeto, Salvavel):  # Graças ao @runtime_checkable isso funciona!
        objeto.salvar(dado)
    else:
        raise TypeError("O objeto não implementa a interface flexível Salvavel")