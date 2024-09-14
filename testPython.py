import pandas as pd

data = {
    'Cliente_ID': [101, 102, 103, 101, 104],
    'Produto_ID': [501, 502, 501, 503, 504],
    'Quantidade': [2, 1, 3, 4, 1],
    'Preco_Total': [200.00, 100.00, 300.00, 400.00, 150.00]
}

df = pd.DataFrame(data)

# 1 - Escreva um código Python que calcula o valor total das vendas por cliente.

totalVendasCliente = df.groupby('Cliente_ID')['Preco_Total'].sum().reset_index()
totalVendasCliente = totalVendasCliente.sort_values(by='Preco_Total', ascending=False) # deixar em ordem DESC
print(totalVendasCliente) # utilizei o metodo groupby() para agrupar os clientes pelo id

print('\n')
# 2 - Escreva uma função em Python que recebe um DataFrame e retorna um novo DataFrame onde todos 
# os valores da coluna Preco_Total sejam multiplicados por 1.1 (um aumento de 10%).

def newDf(df):
    novoDf = pd.DataFrame(df).copy() # copio o dataframe que irei receber na funçao
    novoDf['Preco_Total'] = novoDf['Preco_Total'] * 1.1 # adiciono 10% na coluna Preco_Total :)
    print(novoDf)


newDf(data)
