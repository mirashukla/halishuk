import pygame
import sys

from classes import *

# Constants
WIDTH, HEIGHT = 500, 400
FPS = 60

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")

# Define box
box = pygame.Rect((300,250,50,50))

run = True

while run:
    
    pygame.draw.rect(screen, (255,0,0), box)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()