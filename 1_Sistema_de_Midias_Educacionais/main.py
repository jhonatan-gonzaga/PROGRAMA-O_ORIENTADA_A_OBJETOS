from plataforma import Plataforma
from midia import Midia, Video, Podcast, TextoNarrado

def main():
    plataforma = Plataforma("Minha Plataforma", [])
    
    video1 = Video("teste", 360, "144p")
    podcast1 = Podcast("Podcast 1", "Descrição do podcast 1", 60)
    texto1 = TextoNarrado("Texto 1", "Descrição do texto 1", "Conteúdo do texto 1")

    plataforma.adicionar_midia(video1)
    plataforma.adicionar_midia(podcast1)
    plataforma.adicionar_midia(texto1)

    print("Mídias na plataforma:")
    plataforma.lista_midia()

    print("\nReproduzindo todas as mídias:")
    plataforma.reproduzir_todas()

if __name__ == '__main__':
    main()