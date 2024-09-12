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

print('\n')
# 2 - Escreva uma query SQL que retorna a soma total de vendas por categoria de produto, 
# ordenada do maior para o menor valor. 

cursor.execute('''
    SELECT Categoria, SUM(Preco_Unitario)
    FROM Produtos
    GROUP BY Categoria 
    ORDER BY Categoria DESC
''')

resultado_2 = cursor.fetchall()

for categoria, total_venda_2 in resultado_2:
    print(f'Categoria: {categoria} | Total de Vendas: {total_venda_2}')

print('\n')
# 2.1 - Resolvendo usando as duas tabelas

cursor.execute('''
    SELECT p.Categoria, SUM(v.Preco_Total) AS Total_vendas
    FROM Vendas v
    JOIN Produtos p ON v.Produto_ID = p.Produto_ID
    GROUP BY p.Categoria
    ORDER BY Total_vendas DESC;
''')

resultado_2_1 = cursor.fetchall()

for categoria, total_venda_2_1 in resultado_2_1:
    print(f'Categoria: {categoria} | Total Venda: {total_venda_2_1}')

print('\n')
# 3 - Usando as tabelas `Vendas` e `Produtos`, escreva uma query SQL que retorna o nome da categoria 
# e a quantidade total vendida de produtos dessa categoria






conn.close()