import os
import pandas as pd
import sqlite3

dir_atual = os.path.dirname(os.path.abspath(__file__))

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

def csv_para_db(nome_csv, nome_tabela):
    df = pd.read_csv(nome_csv)
    
    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
    print(f'Tabela {nome_tabela} carregada com sucesso!')

tabelas = {
    os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'): 'Funcionarios',
    os.path.join(dir_atual, '..', 'tabelas', 'cargos.csv'): 'Cargos',
    os.path.join(dir_atual, '..', 'tabelas', 'departamentos.csv'): 'Departamentos',
    os.path.join(dir_atual, '..', 'tabelas', 'historico_salarios.csv'): 'HistoricoSalarios',
    os.path.join(dir_atual, '..', 'tabelas', 'dependentes.csv'): 'Dependentes',
    os.path.join(dir_atual, '..', 'tabelas', 'projetos.csv'): 'Projetos',
    os.path.join(dir_atual, '..', 'tabelas', 'recursos_projeto.csv'): 'RecursosProjeto'

}

for arquivo_csv, nome_tabela in tabelas.items():
    csv_para_db(arquivo_csv, nome_tabela)

conn.close()
