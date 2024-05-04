#Bibliotecas
import pygame as py
from pygame.locals import *
from sys import exit

#Inicialização:
py.init()

#Tela da estrutura:
largura = 640
altura = 480
x = largura / 2
y = 0

tela = py.display.set_mode((largura, altura))

#Nome da Janela do Game:
py.display.set_caption("Meu Desenho :)")
relogio = py.time.Clock()

#Criação do Looping Principal do Game:
while True:
    relogio.tick(180)
    tela.fill((0, 0, 0))
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            exit()
            
    py.draw.circle(tela, (0, 0, 200), (400, (y +180)), 40)
    py.draw.line(tela, (255, 255, 0), (100, (y + 1)), (200, (y + 180)), 5)
    py.draw.line(tela, (255, 255, 0), (400, (y + 1)), (300, (y + 180)), 5)
    py.draw.circle(tela, (0, 0, 200), (100, (y + 180)), 40)
    py.draw.rect(tela, (255,255,255), (240, (y + 200), 10, 20))
    py.draw.line(tela, (255,255, 0), (20, (y + 400)), (480, (y + 350)), 20)
    
    if y >= altura:
        y = 0
    y += 1
    
    py.display.update()
