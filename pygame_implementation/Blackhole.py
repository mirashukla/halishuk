import pygame
import sys
import os
from constants import Constants
from window import Window

class Blackhole(Window):
    
    def __init__(self):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)

        self.load_image("blackhole.png", (50,50))
        self.set_start_position(self.blackhole_start_pos)
        
    


# If this script is run directly this will display the image in game window at the location sepcified
if __name__ == "__main__":
    
    # Initialize Pygame
    pygame.init()
    
    # Initialize Pygame screen
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Image Attachment Example")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    # Create an object with an attached image
    
    blackhole = Blackhole()
    all_sprites.add(blackhole)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw everything
        screen.fill(Constants.BACKGROUND_COLOR)
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()