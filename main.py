import os
import subprocess

def executar_script(script):
    """Executa um script Python no diretório componentes."""
    script_path = os.path.join('components', script)
    subprocess.run(['python', script_path], check=True)

def main():
    # Executar o script csvToDb
    print("Executando csvToDb.py...")
    subprocess.run(['python', 'components/csvToDb.py'], check=True)

    # Executar as consultas de ex1.py até ex10.py
    for i in range(1, 11):
        script = f'ex{i}.py'
        print(f"Executando {script}...")
        executar_script(script)

if __name__ == "__main__":
    main()
