# Projeto Tkinter - Pergunta Urgente

Este projeto é uma aplicação GUI simples feita com Tkinter que faz uma pergunta ao usuário e reage com base na resposta escolhida. 

## Estrutura do Projeto

```
projeto/
│
├── buzz_meme.jpeg
├── script.py
└── README.md
```

- `buzz_meme.jpeg`: Imagem de fundo usada na aplicação.
- `script.py`: Script principal contendo a lógica da aplicação.
- `README.md`: Documentação do projeto.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído com Python)
- Pillow

## Instalação

1. Clone o repositório:
    ```bash
    git clone <URL do repositório>
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd projeto
    ```

3. Instale a biblioteca Pillow:
    ```bash
    pip install pillow
    ```

## Uso

Para executar a aplicação, execute o seguinte comando:
```bash
python script.py
```

## Código

### script.py

```python
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk
    
ROOTH_PATH = Path(__file__).parent

def set_background():
    image = Image.open(ROOTH_PATH / "buzz_meme.jpeg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)
        
def accepted():
    messagebox.showinfo("HUMM", "SABIA QUE VOCÊ É!")
    
def denied():
    button_1.destroy()
    
root = tk.Tk()
root.title = ("PERGUNTA URGENTE!")
root.geometry('600x600')
root.configure(set_background())
    
margin = Canvas(root, width=0, bg="#ffc0dd", height=0, bd=0, highlightthickness=0, relief="ridge")
margin.pack()
text_id = Label(root, bg="#ffc0dd", text="Você é? hehe", fg="#590d22", font=("Montserrat", 24, "bold"))
text_id.pack()
button_1 = tk.Button(root, text="NÃO!", bg="#ffc0dd", command=denied, relief=RIDGE, bd=3, font=("Montserrat", 8, "bold"))
button_1.pack()
root.bind("<Motion>", move_button_1)
button_2 = tk.Button(root, text="OPAAAAA", bg="#ffc0dd", relief=RIDGE, bd=3, command=accepted, font=("Montserrat", 14, "bold"))
button_2.pack()

root.mainloop()
```

## Funcionalidades

- **set_background**: Define a imagem de fundo da janela principal.
- **move_button_1**: Move o botão "NÃO!" para uma posição aleatória se o cursor do mouse estiver próximo.
- **accepted**: Exibe uma mensagem quando o botão "OPAAAAA" é clicado.
- **denied**: Remove o botão "NÃO!" quando clicado.
