import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

query = """
SELECT rp.descricao_recurso, SUM(rp.quantidade_utilizada) AS quantidade_total
FROM RecursosProjeto rp
WHERE rp.tipo_recurso = 'Material'
GROUP BY rp.descricao_recurso
ORDER BY quantidade_total DESC
LIMIT 3;
"""

cursor.execute(query)

resultados = cursor.fetchall()

for resultado in resultados:
    print(f"Recurso: {resultado[0]}, Quantidade Total: {resultado[1]}")

conn.close()
