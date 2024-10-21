# 2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes:
import sqlite3

def listar_funcionarios_cargos_departamentos_dependentes():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    query = '''
    SELECT f.nome AS funcionario, c.descricao AS cargo, d.nome_departamento AS departamento, dep.nome AS dependente
    FROM Funcionarios f
    JOIN Cargos c ON f.cargo_id = c.id_cargo
    JOIN Departamentos d ON f.departamento_id = d.id_departamento
    LEFT JOIN Dependentes dep ON f.id_funcionario = dep.id_funcionario
    ORDER BY f.nome
    '''
    
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()

listar_funcionarios_cargos_departamentos_dependentes()
