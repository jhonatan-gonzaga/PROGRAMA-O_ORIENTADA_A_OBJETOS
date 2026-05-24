from Imprimivel import Imprimivel, Boleto, RelatorioSimples, Etiqueta, processar_impressao

def main():
    boleto = Boleto("123", 100.0, "Pagamento")
    etiqueta = Etiqueta("João", "Rua A, 123", "Entrega")
    relatorio = RelatorioSimples("Relatório de Vendas", "Análise de desempenho")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)

if __name__ == "__main__":
    main()