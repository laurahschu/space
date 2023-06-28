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

