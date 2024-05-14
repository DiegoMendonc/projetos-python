import subprocess
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

def criar_executavel(script):
    # Comando para criar o executável usando PyInstaller
    comando = f"pyinstaller --onefile {script}"

    # Executa o comando no terminal
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = processo.communicate()

    # Exibe o output e o error
    print(output.decode("utf-8"))
    print(error.decode("utf-8"))

# Nome do seu script Python
script = ROOTH_PATH / "teste" / "index.py"

# Chama a função para criar o executável
criar_executavel(script)
