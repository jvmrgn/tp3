import sqlite3

conn = sqlite3.connect('empresa.db') 
cursor = conn.cursor()

query = '''
SELECT p.id_projeto, p.nome_projeto, COUNT(d.id_dependente) AS num_dependentes
FROM projetos p
JOIN funcionarios f ON p.funcionario_responsavel = f.id_funcionario
LEFT JOIN dependentes d ON f.id_funcionario = d.id_funcionario
GROUP BY p.id_projeto, p.nome_projeto
ORDER BY num_dependentes DESC
LIMIT 1;
'''

cursor.execute(query)

resultado = cursor.fetchone()

if resultado:
    print(f'Projeto com mais dependentes:')
    print(f'ID do Projeto: {resultado[0]}')
    print(f'Nome do Projeto: {resultado[1]}')
    print(f'Número de Dependentes: {resultado[2]}')
else:
    print('Nenhum projeto encontrado.')

conn.close()
