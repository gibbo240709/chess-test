import pygame
import requests
import rembg
from io import BytesIO

#initialise pygame
pygame.init()

#width and height of screen
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess")
font = pygame.font.Font("freesansbold.ttf", 20)
medium_font = pygame.font.Font("freesansbold.ttf", 40)
big_font = pygame.font.Font("freesansbold.ttf", 50)

timer = pygame.time.Clock()
fps = 60
