import sqlite3
import json

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

query_1 = '''
SELECT p.id_projeto, p.nome_projeto, p.custo, p.data_inicio, p.data_conclusao, f.nome
FROM projetos p
JOIN funcionarios f ON p.funcionario_responsavel = f.id_funcionario
WHERE p.status = 'Em Execução';
'''

try:
    cursor.execute(query_1)

    resultados_1 = cursor.fetchall()

    projetos_em_execucao = []
    for resultado in resultados_1:
        projeto = {
            'id_projeto': resultado[0],
            'nome_projeto': resultado[1],
            'custo': resultado[2],
            'data_inicio': resultado[3],
            'data_conclusao': resultado[4] if resultado[4] else 'Em andamento', 
            'funcionario_responsavel': resultado[5]
        }
        projetos_em_execucao.append(projeto)

    with open('projetos_em_execucao.json', 'w', encoding='utf-8') as json_file:
        json.dump(projetos_em_execucao, json_file, ensure_ascii=False, indent=4)

    print("Arquivo JSON gerado com sucesso!")

except sqlite3.OperationalError as e:
    print(f"Erro na consulta SQL: {e}")

conn.close()
