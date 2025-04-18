


import csv

def process(date: str, symbol: str, closing_price: float) -> None:
    # Imaginge that this function actually does something.
    assert closing_price > 0.0

with open('leitura_csv_SemCab.txt', 'r') as let_csv:
    tab_reader = csv.reader(let_csv, delimiter='\t')
    for linha in tab_reader:
        data = linha[0]
        acao = linha[1]
        preco = float(linha[2])
        print(data,acao,preco)

