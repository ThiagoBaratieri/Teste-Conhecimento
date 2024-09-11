import sqlite3

conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

# Tabela 1
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

dados = [
    (1, '2024-01-10', 101, 501, 2, 200.00),
    (2, '2024-01-15', 102, 502, 1, 100.00),
    (3, '2024-02-01', 103, 501, 3, 300.00),
    (4, '2024-02-05', 101, 503, 4, 400.00),
    (5, '2024-02-10', 104, 504, 1, 150.00)
]

for idVenda, data, clienteId, produtoId, qntd, precoTotal in dados:
    cursor.execute('''
        INSERT INTO Vendas (ID_Venda, Data, Cliente_ID, Produto_ID, Quantidade, Preco_Total)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (idVenda, data, clienteId, produtoId, qntd, precoTotal))

conn.commit()
conn.close()