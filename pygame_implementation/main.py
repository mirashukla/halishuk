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

# Initialize Pygame screen
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("DOINNGGGG")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create game objects
canon = Canon()
blackhole = Blackhole()

# Add objects to sprite group
all_sprites.add(canon)
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
    screen.fill(Constants.BACKGROUND_COLOR)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(Constants.FPS)