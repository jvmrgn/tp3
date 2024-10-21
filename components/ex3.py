# 3. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes:
import sqlite3

def listar_aumento_salarial_ultimos_meses():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    query = '''
    SELECT DISTINCT f.nome
    FROM Funcionarios f
    JOIN HistoricoSalarios hs ON f.id_funcionario = hs.id_funcionario
    WHERE hs.salario > (
        SELECT MAX(salario) 
        FROM HistoricoSalarios 
        WHERE id_funcionario = f.id_funcionario AND (mes = 1 OR mes = 2 OR mes = 3)
    )
    '''
    
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()

listar_aumento_salarial_ultimos_meses()