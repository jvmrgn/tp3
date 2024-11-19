import os
import subprocess

def executar_script(script):
    """Executa um script Python no diretório componentes, se o arquivo existir."""
    script_path = os.path.join('components', script)
    
    if os.path.exists(script_path):
        subprocess.run(['python', script_path], check=True)
    else:
        print(f"O script {script} não foi encontrado, pulando...")

def main():
    print("Executando csvToDb.py...")
    subprocess.run(['python', 'components/csvToDb.py'], check=True)

    for i in range(1, 7):
        script = f'ex{i}.py'
        print(f"Verificando e executando {script}...")
        executar_script(script)

if __name__ == "__main__":
    main()
