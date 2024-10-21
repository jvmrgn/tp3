# Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000.
import os
import pandas as pd

def listar_analista_salario_mais_alto_entre_5000_e_9000():
    dir_atual = os.path.dirname(os.path.abspath(__file__))

    funcionarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'funcionarios.csv'))
    historico_salarios = pd.read_csv(os.path.join(dir_atual, '..', 'tabelas', 'historico_salarios.csv'))
    
    analistas = funcionarios[funcionarios['cargo_id'] == 2]
    
    salarios_analistas = historico_salarios[historico_salarios['id_funcionario'].isin(analistas['id_funcionario'])]
    
    salarios_analistas = salarios_analistas[(salarios_analistas['salario'] >= 5000) & (salarios_analistas['salario'] <= 9000)]
    
    if not salarios_analistas.empty:
        salario_mais_alto = salarios_analistas.loc[salarios_analistas['salario'].idxmax()]
        
        funcionario = funcionarios[funcionarios['id_funcionario'] == salario_mais_alto['id_funcionario']]
        
        print(funcionario)
    else:
        print("Nenhum analista encontrado com salário entre 5000 e 9000.")

listar_analista_salario_mais_alto_entre_5000_e_9000()
