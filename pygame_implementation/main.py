# External
import pygame
import sys
import os

# Classes
from Canon import Canon
from Blackhole import Blackhole
from constants import Constants


# Initialize Pygame
pygame.init()

# background color
RED = (255, 10, 10)
WHITE = (255, 255, 255)

# Initialize Pygame screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("DOINNGGGG")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create canon
img_path = os.getcwd() + "/game_pictures/canon.jpg"
canon = Canon(img_path)
all_sprites.add(canon)

# Create blackole
img_path = os.getcwd() + "/game_pictures/blackhole.png"
blackhole = Blackhole(img_path)
all_sprites.add(blackhole)

# Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        
    # Update all sprites
    all_sprites.update()
    
    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(Constants.FPS)