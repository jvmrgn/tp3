import sqlite3

def listar_tabelas():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    tabelas = {
        'Funcionarios': 'id_funcionario',
        'Cargos': 'id_cargo',
        'Departamentos': 'id_departamento',
        'HistoricoSalarios': 'id_funcionario', 
        'Dependentes': 'id_dependente'
    }

    for tabela, coluna_id in tabelas.items():
        cursor.execute(f'SELECT * FROM {tabela} ORDER BY {coluna_id} ASC')
        print(f"--- {tabela} ---")
        for row in cursor.fetchall():
            print(row)
        print('\n')

    conn.close()

listar_tabelas()
