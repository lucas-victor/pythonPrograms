'''
Exercícios de Python para a assimilação do conteúdo já apresentado
Curso de Python
Exercício 4
---
Faça um script que abra e execute um arquivo MP3.
Módulo: pygame
'''
# Importando o PyGame
import pygame

# Inicializando o PyGame
pygame.init()

# Carregando o arquivo MP3 e executando
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
