#Configuração iniciais
import pygame as pg 
import random

pg.init()
pg.display.set_caption("JOGUIN DO PYTHON")
largura, altura = 600, 400
tela = pg.display.set_mode((largura, altura))
relogio = pg.time.Clock()

#cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametros da cobra:
tamanho_quadrado = 10
velocidade_jogo = 15

#Criar funções específicas:
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20) * 20 
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20) * 20
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pg.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pg.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])
    
def desenhar_pontuacao(pontuacao):
    fonte = pg.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])    

#pegar a interação do usuario
def selecionar_velocidade(tecla):
    if tecla == pg.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pg.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pg.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pg.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0        
    return velocidade_x, velocidade_y
    
def rodar_jogo():
    fim_jogo = False
    
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    #Criar um loop infinito 
    while not fim_jogo:
        tela.fill(preta)
        for evento in pg.event.get():
            
            #criar a logica de terminar o jogo
            if evento.type == pg.QUIT:
                fim_jogo = True
            
            #Fechar a tela ou teclado para mover a cobra
            elif evento.type == pg.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        #Desenhar os objetos do jogo na tela:        
        # Comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)   
        
        #Cobra bater na parede ou Cobra bateu na cobra          
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
            
        # atualizar a posicao da cobra
        x += velocidade_x
        y += velocidade_y
        
        #Cobrinha 
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels [0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True 
        desenhar_cobra(tamanho_quadrado, pixels)
        
        # pontuação
        desenhar_pontuacao(tamanho_cobra -1)
        
        #Atualização da tela
        pg.display.update()
        
        #Criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(velocidade_jogo)
rodar_jogo()