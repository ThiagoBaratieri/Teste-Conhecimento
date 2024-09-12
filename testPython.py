import pandas as pd

data = {
    'Cliente_ID': [101, 102, 103, 101, 104],
    'Produto_ID': [501, 502, 501, 503, 504],
    'Quantidade': [2, 1, 3, 4, 1],
    'Preco_Total': [200.00, 100.00, 300.00, 400.00, 150.00]
}

df = pd.DataFrame(data)

# 1 - Escreva um código Python que calcula o valor total das vendas por cliente.

cliente_id = data['Cliente_ID']
produto_id = data['Produto_ID']
preco_total = data['Preco_Total']

print(cliente_id)
