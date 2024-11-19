import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute('''
SELECT 
    d.nome_departamento, 
    SUM(r.custo_total) AS custo_total_projetos
FROM 
    Projetos p
JOIN 
    Departamentos d ON p.departamento_id = d.id_departamento
JOIN 
    RecursosProjeto r ON p.id_projeto = r.id_projeto
WHERE 
    p.status = 'Concluído'
GROUP BY 
    d.nome_departamento;
''')

resultados = cursor.fetchall()

for resultado in resultados:
    print(f"Departamento: {resultado[0]}, Custo Total dos Projetos: {resultado[1]}")

conn.close()
