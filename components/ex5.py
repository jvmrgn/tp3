# 5. Listar qual estagiário possui filho.
import sqlite3

def listar_estagiarios_com_filhos():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    query = '''
    SELECT f.nome AS estagiario
    FROM Funcionarios f
    JOIN Cargos c ON f.cargo_id = c.id_cargo
    JOIN Dependentes dep ON f.id_funcionario = dep.id_funcionario
    WHERE c.descricao = 'Estagiário'
    '''
    
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()

listar_estagiarios_com_filhos()
