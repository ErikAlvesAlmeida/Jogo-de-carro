import pygame
from tkinter import *

def carro_branco():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_branco_jogo.png")

    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))

        pygame.display.update()
    pygame.quit()

def carro_azul():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_azul_jogo.png")

    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))

        pygame.display.update()
    pygame.quit()

def carro_amarelo():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_amarelo_jogo.png")

    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))

        pygame.display.update()
    pygame.quit()
def carro_prata():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_prata_jogo.png")

    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))

        pygame.display.update()
    pygame.quit()
def carro_preto():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_jogo.png")

    janela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo, (0, 0))
        janela.blit(carro, (x, y))

        pygame.display.update()
    pygame.quit()

def muda_carro():
    janela1 = Tk()

    carrobranco = Button(janela1, width=20, text="CARRO BRANCO", command= carro_branco)
    carroazul = Button(janela1, width=20, text="CARRO AZUL", command= carro_azul)
    carroamarelo = Button(janela1, width=20, text="CARRO AMARELO", command= carro_amarelo)
    carroprata = Button(janela1, width=20, text="CARRO PRATA", command= carro_prata)
    carropreto = Button(janela1, width=20, text="CARRO PRETO", command= carro_preto)

    carroamarelo.place(x=350, y= 250)
    carropreto.place(x=350, y=280)
    carroazul.place(x=350, y=310)
    carroprata.place(x=350, y=340)
    carrobranco.place(x=350, y=370)


    janela1.geometry("800x600+270+050")
    janela1.mainloop()

def sair():
    janela.quit()
def iniciar():
    pygame.init()
    x = 400
    y = 300
    velocidade = 10
    fundo = pygame.image.load("tela_jogo.png")
    carro = pygame.image.load("carro_jogo.png")

    janela = pygame.display.set_mode((800,600))
    pygame.display.set_caption("PÃO")

    janela_aberta = True
    while janela_aberta:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False

        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_w] or comandos[pygame.K_UP]:
            y -= velocidade

        if comandos[pygame.K_s] or comandos[pygame.K_DOWN]:
            y += velocidade

        if comandos[pygame.K_d] or comandos[pygame.K_RIGHT]:
            x += velocidade

        if comandos[pygame.K_a] or comandos[pygame.K_LEFT]:
            x -= velocidade
        if y < -200:
            y = 700

        janela.blit(fundo,(0,0))
        janela.blit(carro,(x,y))

        pygame.display.update()
    pygame.quit()

janela = Tk()
sair = Button(janela,width=20, text="SAIR", command= sair)
iniciar = Button(janela, width=20, text="INICIAR", command= iniciar)
muda_carro = Button(janela, width=20, text="MUDAR CARRO", command= muda_carro)
iniciar.place(x=350, y=250)
sair.place(x=350, y=310)
muda_carro.place(x=350, y=280)
#image =Tk.PhotoImage(file="capa.png")

#image = image.subsample(1,1)

#labelcapa = Tk.Label(image=image)
#labelcapa.place(x=0,y=0,relwidth= 1.0, relheight=1.0)

janela.geometry("800x600+270+050")
janela.mainloop()