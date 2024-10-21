# 6. Listar o funcionário que teve o salário médio mais alto.
import os
import pandas as pd

def listar_funcionario_salario_medio_mais_alto():
    dir_atual = os.path.dirname(os.path.abspath(__file__))

    historico_salarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'historico_salarios.csv'))
    funcionarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'))

    salario_medio = historico_salarios.groupby('id_funcionario')['salario'].mean().reset_index()
    salario_medio = salario_medio.merge(funcionarios[['id_funcionario', 'nome']], on='id_funcionario')
    
    funcionario_alto = salario_medio.loc[salario_medio['salario'].idxmax()]

    print(funcionario_alto)

listar_funcionario_salario_medio_mais_alto()
