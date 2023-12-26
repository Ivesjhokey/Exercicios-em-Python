'''Faça um programa em python que abra e reproduza o audio de um arquivo MP3'''

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('vamosbeber.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

#obs esse programa so funciona por causa da biblioteca play sound, utiliza-la em outra IDE sem ser o pycharm devera procurar outra biblioteca.
