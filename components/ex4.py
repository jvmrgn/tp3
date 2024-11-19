import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

query = '''
SELECT nome_projeto, custo, data_inicio, data_conclusao, f.nome AS funcionario_responsavel
FROM projetos p
JOIN funcionarios f ON p.funcionario_responsavel = f.id_funcionario
WHERE p.status = 'Em Execução';
'''

cursor.execute(query)

resultados = cursor.fetchall()

for row in resultados:
    print(f'Nome do Projeto: {row[0]}')
    print(f'Custo: {row[1]}')
    print(f'Data de Início: {row[2]}')
    print(f'Data de Conclusão: {row[3]}')
    print(f'Funcionário Responsável: {row[4]}')
    print('-' * 40)

conn.close()
