# External
import sys
import pygame

# Classes
from Cannon import Cannon
from Blackhole import Blackhole
from constants import Constants
from xmas_tree import Xmas_tree
from window import Window

# Initialize Pygame
pygame.init()

# Initialize Pygame screen
screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
pygame.display.set_caption("DOINNGGGG")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
xmas_tree_sprites = pygame.sprite.Group()

# Create game objects
cannon = Cannon()
blackhole = Blackhole()

# Add objects to sprite group 
all_sprites.add(cannon)
all_sprites.add(blackhole)

# Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Spawn Xmas tree when space bar is pressed
            xmas_tree = Xmas_tree([cannon.rect.centerx,cannon.rect.top])
            xmas_tree_sprites.add(xmas_tree)
            all_sprites.add(xmas_tree)
        
    # Update all sprites
    cannon.update()
    xmas_tree_sprites.update()
    
    # Handle shooting cooldown
    if cannon.shoot_cooldown > 0:
        cannon.shoot_cooldown -= 1

    # Draw everything
    screen.fill(Constants.BACKGROUND_COLOR)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(Constants.FPS)
    