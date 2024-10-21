# 10. Listar a média de salário por departamento em ordem decrescente.
import os
import pandas as pd

def listar_media_salario_por_departamento():
    dir_atual = os.path.dirname(os.path.abspath(__file__))

    historico_salarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'historico_salarios.csv'))
    funcionarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'))
    departamentos = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'departamentos.csv'))

    salarios_media = historico_salarios.groupby('id_funcionario')['salario'].mean().reset_index()
    
    salarios_media = salarios_media.merge(funcionarios[['id_funcionario', 'departamento_id']], on='id_funcionario')
    
    salarios_media_por_departamento = salarios_media.groupby('departamento_id')['salario'].mean().reset_index()

    salarios_media_por_departamento = salarios_media_por_departamento.merge(
        departamentos[['id_departamento', 'nome_departamento']],
        left_on='departamento_id',
        right_on='id_departamento'
    )
    
    salarios_media_por_departamento = salarios_media_por_departamento[['nome_departamento', 'salario']].sort_values(by='salario', ascending=False)

    print(salarios_media_por_departamento)

listar_media_salario_por_departamento()
