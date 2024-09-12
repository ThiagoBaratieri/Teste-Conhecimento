# Criar Tabelas

import sqlite3

def dadoExiste(cursor, tabela, id_coluna, id_valor):
    cursor.execute(f'SELECT 1 FROM {tabela} WHERE {id_coluna} = ?', (id_valor,))
    return cursor.fetchone() is not None



conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

# Tabela 1 - Vendas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendas (
        ID_venda INTEGER PRIMARY KEY,
        Data TEXT NOT NULL,
        Cliente_ID INTEGER NOT NULL,
        Produto_ID INTEGER NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco_Total REAL NOT NULL               
    )
''')

dados_tabela_vendas = [
    (1, '2024-01-10', 101, 501, 2, 200.00),
    (2, '2024-01-15', 102, 502, 1, 100.00),
    (3, '2024-02-01', 103, 501, 3, 300.00),
    (4, '2024-02-05', 101, 503, 4, 400.00),
    (5, '2024-02-10', 104, 504, 1, 150.00)
]


for idVenda, data, clienteId, produtoId, qntd, precoTotal in dados_tabela_vendas:
    if not dadoExiste(cursor, 'Vendas', 'ID_venda', idVenda):
        cursor.execute('''
            INSERT INTO Vendas (ID_Venda, Data, Cliente_ID, Produto_ID, Quantidade, Preco_Total)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (idVenda, data, clienteId, produtoId, qntd, precoTotal))

# Tabela 2 - Produtos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
        Produto_ID INTEGER PRIMARY KEY,
        Categoria TEXT NOT NULL,
        Preco_Unitario REAL NOT NULL               
    )               
''')

dados_tabela_produtos = [
    (501, 'Eletrônico', 100.00),
    (502, 'Móveis', 100.00),
    (503, 'Eletrônico', 100.00),
    (504, 'Móveis', 150.00),
    (505, 'Eletrodomésticos', 200.00)
]

for prodId, cat, precoUni in dados_tabela_produtos:
    if not dadoExiste(cursor, 'Produtos', 'Produto_ID', prodId):
        cursor.execute('''
            INSERT INTO Produtos (Produto_ID, Categoria, Preco_Unitario)
            VALUES (?, ?, ?)
        ''', (prodId, cat, precoUni))


conn.commit()
conn.close()