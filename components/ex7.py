# 7. Listar o analista que é pai de 2 (duas) meninas.
import pandas as pd
import os

def listar_analista_pai_de_duas_meninas():
    dir_atual = os.path.dirname(os.path.abspath(__file__))

    funcionarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'))
    dependentes = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'dependentes.csv'))
    cargos = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'cargos.csv'))

    analistas = funcionarios[funcionarios['cargo_id'] == 2]
    meninas = dependentes[dependentes['nome'].str.contains('a|e$', case=False, regex=True)]

    analistas_com_filhos = meninas[meninas['id_funcionario'].isin(analistas['id_funcionario'])]
    analista_pai_duas_meninas = analistas_com_filhos['id_funcionario'].value_counts()

    analista_com_duas_meninas = analista_pai_duas_meninas[analista_pai_duas_meninas == 2]

    if not analista_com_duas_meninas.empty:
        funcionarios_analista = funcionarios[funcionarios['id_funcionario'].isin(analista_com_duas_meninas.index)]
        print(funcionarios_analista)
    else:
        print("Nenhum analista encontrado que seja pai de duas meninas.")

listar_analista_pai_de_duas_meninas()
