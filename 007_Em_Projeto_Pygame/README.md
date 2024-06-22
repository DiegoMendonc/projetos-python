# Projeto: Desenho Animado com Pygame

Este projeto é um exemplo simples de uma animação usando a biblioteca Pygame. A aplicação cria uma janela onde diversos elementos gráficos são desenhados e animados em um loop contínuo.

## Estrutura do Projeto

```
projeto/
│
├── script.py
└── README.md
```

- `script.py`: Script principal contendo a lógica de inicialização, desenho e animação dos elementos gráficos.
- `README.md`: Documentação do projeto.

## Requisitos

- Python 3.x
- Pygame

## Instalação

1. Instale o Pygame:
    ```bash
    pip install pygame
    ```

2. Clone o repositório:
    ```bash
    git clone <URL do repositório>
    ```

3. Navegue até o diretório do projeto:
    ```bash
    cd projeto
    ```

## Uso

Para executar a aplicação, execute o seguinte comando:
```bash
python script.py
```

## Funcionalidades

### Inicialização

A aplicação inicializa o Pygame, define o tamanho da janela e o título da janela do jogo.

### Loop Principal

O loop principal do jogo faz o seguinte:
- Limpa a tela.
- Desenha vários elementos gráficos (círculos, linhas, retângulos) na tela.
- Atualiza a posição dos elementos para criar a animação.
- Lida com eventos de saída para fechar a janela do jogo.

### Elementos Gráficos

Os elementos gráficos desenhados na tela incluem:
- Dois círculos azuis.
- Três linhas amarelas.
- Um retângulo branco.

### Animação

Os elementos são desenhados em posições que são atualizadas em cada iteração do loop, criando uma animação contínua. A variável `y` é incrementada continuamente e usada para modificar as posições verticais dos elementos gráficos.

## Código

### script.py

```python
# Bibliotecas
import pygame as py
from pygame.locals import *
from sys import exit

# Inicialização
py.init()

# Tela da estrutura
largura = 640
altura = 480
x = largura / 2
y = 0

tela = py.display.set_mode((largura, altura))

# Nome da Janela do Game
py.display.set_caption("Meu Desenho :)")
relogio = py.time.Clock()

# Criação do Looping Principal do Game
while True:
    relogio.tick(180)
    tela.fill((0, 0, 0))
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            exit()
            
    py.draw.circle(tela, (0, 0, 200), (400, (y + 180)), 40)
    py.draw.line(tela, (255, 255, 0), (100, (y + 1)), (200, (y + 180)), 5)
    py.draw.line(tela, (255, 255, 0), (400, (y + 1)), (300, (y + 180)), 5)
    py.draw.circle(tela, (0, 0, 200), (100, (y + 180)), 40)
    py.draw.rect(tela, (255, 255, 255), (240, (y + 200), 10, 20))
    py.draw.line(tela, (255, 255, 0), (20, (y + 400)), (480, (y + 350)), 20)
    
    if y >= altura:
        y = 0
    y += 1
    
    py.display.update()
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.