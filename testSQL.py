# Manipular as tabelas

import sqlite3

conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

# 1 - Escreva uma query SQL que retorna o total de vendas (em valor) por cliente. 

cursor.execute('''
    SELECT Cliente_ID, SUM(Preco_Total)
    FROM Vendas
    GROUP BY Cliente_ID
''')
resultado = cursor.fetchall()

for cliente_id, total_vendas in resultado:
    print(f'ID do Cliente: {cliente_id} | Total de Vendas: {total_vendas}')

conn.close()