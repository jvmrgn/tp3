# 9. Listar qual departamento possui o maior número de dependentes.
import os
import pandas as pd

def listar_departamento_com_maior_numero_dependentes():
    dir_atual = os.path.dirname(os.path.abspath(__file__))

    dependentes = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'dependentes.csv'))
    funcionarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'))
    departamentos = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'departamentos.csv'))

    dependentes_count = dependentes['id_funcionario'].value_counts().reset_index()
    dependentes_count.columns = ['id_funcionario', 'numero_dependentes']
    
    departamento_count = dependentes_count.merge(funcionarios[['id_funcionario', 'departamento_id']], on='id_funcionario')
    
    departamento_count = departamento_count.groupby('departamento_id')['numero_dependentes'].sum().reset_index()

    departamento_com_mais_dependentes = departamento_count.loc[departamento_count['numero_dependentes'].idxmax()]
    departamento_nome = departamentos[departamentos['id_departamento'] == departamento_com_mais_dependentes['departamento_id']]

    print(departamento_nome)

listar_departamento_com_maior_numero_dependentes()
