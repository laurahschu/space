import pygame
import random
import sys
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from pygame.locals import *

pygame.init()

# Funções auxiliares para manipulação de arquivos
def salvar_marcacoes():
    try:
        with open('marcacoes.txt', 'w') as arquivo:
            for estrela in stars:
                arquivo.write(f"{estrela[0]},{estrela[1][0]},{estrela[1][1]}\n")
        messagebox.showinfo("Salvar Marcações", "Marcações salvas com sucesso!")
    except PermissionError:
        messagebox.showerror("Erro", "Permissão negada ao salvar marcações.")
    except:
        messagebox.showerror("Erro", "Ocorreu um erro ao salvar marcações.")

def carregar_marcacoes():
    try:
        with open('marcacoes.txt', 'r') as arquivo:
            stars.clear()
            lines.clear()
            for linha in arquivo:
                nome, x, y = linha.strip().split(',')
                estrela = (nome, (int(x), int(y)))
                stars.append(estrela)
        messagebox.showinfo("Carregar Marcações", "Marcações carregadas com sucesso!")
    except FileNotFoundError:
        messagebox.showwarning("Carregar Marcações", "Nenhuma marcação encontrada.")
    except:
        messagebox.showerror("Erro", "Ocorreu um erro ao carregar marcações.")

def excluir_marcacoes():
    try:
        os.remove('marcacoes.txt')
        stars.clear()
        lines.clear()
        messagebox.showinfo("Excluir Marcações", "Marcações excluídas com sucesso!")
    except FileNotFoundError:
        messagebox.showwarning("Excluir Marcações", "Nenhuma marcação encontrada.")
    except:
        messagebox.showerror("Erro", "Ocorreu um erro ao excluir as marcações.")

# Configuração da tela e ícone
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Space Marker')

icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Carregamento das imagens e música
fundodetela = pygame.image.load("bgspace.jpeg")
pygame.mixer.music.load("spacesound.mp3")
pygame.mixer.music.play(-1)

# Listas para armazenar as marcações e linhas
stars = []
lines = []

# Função para desenhar as estrelas na tela
def desenhar_estrelas():
    for i, estrela in enumerate(stars):
        pygame.draw.circle(tela, (255, 255, 255), estrela[1], 2)
        texto = font.render(estrela[0], True, (255, 255, 255))
        tela.blit(texto, (estrela[1][0] - 10, estrela[1][1] + 10))

# Função para desenhar as linhas conectando as estrelas marcadas
def desenhar_linhas():
    for estrela1, estrela2 in lines:
        x1, y1 = estrela1[1]
        x2, y2 = estrela2[1]
        x1 = round(x1)
        y1 = round(y1)
        x2 = round(x2)
        y2 = round(y2)
        pygame.draw.line(tela, (255, 255, 255), (x1, y1), (x2, y2), 1)
        distancia_x = abs(x2 - x1)
        distancia_y = abs(y2 - y1)
        soma_distancias = distancia_x + distancia_y
        texto_distancia = font.render(str(soma_distancias), True, (255, 255, 255))
        posicao_texto = (
            (x1 + x2) // 2,
            (y1 + y2) // 2
        )
        tela.blit(texto_distancia, posicao_texto)

# Função para exibir uma caixa de diálogo de entrada de texto e retornar o nome da estrela
def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome_estrela = simpledialog.askstring("Nome do Ponto", "Digite o nome do ponto:")
    root.destroy()  # Fechar a janela de diálogo após obter o nome
    return nome_estrela if nome_estrela else "Estrela Desconhecida"

# Carregamento da fonte para exibição do nome das estrelas
font = pygame.font.SysFont(None, 24)
font_frases = pygame.font.SysFont('calibri', 18, italic=True)
font_nomes = pygame.font.SysFont('calibri', 14)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # Antes de fechar a aplicação, salvar as marcações
            salvar_marcacoes()
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Obter o nome da estrela através de uma caixa de diálogo
            nome_estrela = obter_nome_estrela()
            # Obter a posição do clique do mouse
            posicao_mouse = event.pos
            # Adicionar o nome da estrela e a posição ao registro de marcações
            estrela = (nome_estrela, posicao_mouse)
            stars.append(estrela)

            # Conectar as estrelas com linhas (apenas se houver mais de uma estrela marcada)
            if len(stars) > 1:
                estrela_anterior = stars[-2]
                linha = (estrela_anterior, estrela)
                lines.append(linha)

    tela.blit(fundodetela, (0, 0))
    desenhar_estrelas()
    desenhar_linhas()
