import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

query = """
SELECT d.nome_departamento, AVG(h.salario) AS media_salario
FROM funcionarios f
JOIN projetos p ON f.id_funcionario = p.funcionario_responsavel
JOIN HistoricoSalarios h ON f.id_funcionario = h.id_funcionario
JOIN departamentos d ON f.departamento_id = d.id_departamento
WHERE p.status = 'Concluído'
AND h.mes = (SELECT MAX(mes) FROM HistoricoSalarios WHERE id_funcionario = f.id_funcionario)
AND h.ano = (SELECT MAX(ano) FROM HistoricoSalarios WHERE id_funcionario = f.id_funcionario)
GROUP BY d.nome_departamento
"""

cursor.execute(query)

resultados = cursor.fetchall()

for resultado in resultados:
    print(f"Departamento: {resultado[0]}, Média Salário: {resultado[1]:.2f}")

conn.close()
