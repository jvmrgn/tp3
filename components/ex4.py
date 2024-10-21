# 4. Listar a média de idade dos filhos dos funcionários por departamento.
import sqlite3

def listar_media_idade_filhos_por_departamento():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    query = '''
    SELECT d.nome_departamento, AVG(strftime('%Y', 'now') - strftime('%Y', dep.data_nascimento)) AS media_idade
    FROM Dependentes dep
    JOIN Funcionarios f ON dep.id_funcionario = f.id_funcionario
    JOIN Departamentos d ON f.departamento_id = d.id_departamento
    GROUP BY d.nome_departamento
    '''
    
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()

listar_media_idade_filhos_por_departamento()
