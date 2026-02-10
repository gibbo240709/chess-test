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

