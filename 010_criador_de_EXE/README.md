## README.md

# Projeto PyInstaller

Este projeto contém um script Python para criar um executável a partir de um script Python usando PyInstaller.

## Estrutura do Projeto

```
projeto/
│
├── teste/
│   └── index.py
├── script.py
└── README.md
```

- `teste/index.py`: Script Python que será transformado em executável.
- `script.py`: Script principal que contém a lógica para criar o executável.
- `README.md`: Documentação do projeto.

## Requisitos

- Python 3.x
- PyInstaller

## Instalação

1. Clone o repositório:
    ```bash
    git clone <URL do repositório>
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd projeto
    ```

3. Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```

## Uso

Para criar um executável a partir do script `index.py`, siga os passos abaixo:

1. Navegue até o diretório onde o `script.py` está localizado.
2. Execute o `script.py`:
    ```bash
    python script.py
    ```

## Código

### script.py

```python
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
```

Este script define uma função `criar_executavel` que recebe o caminho de um script Python e utiliza o PyInstaller para criar um executável a partir dele. O output e os erros do processo são exibidos no console.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.