# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

print("\033[1;34mCurta o som 🎧\033[m")

# Inicializa o módulo
pygame.init()

# Faz o carregamento da música
pygame.mixer.music.load("/Users/alisonandre/Documents/code/Curso em vídeo/Python3/Mundo_1/03 - Utilizando módulos/background-music.mp3")

# Dá o play
pygame.mixer.music.play()

input("Tocando... aperte Enter para sair")