import pygame
import sys
import os
import logging

from constants import Constants

class Cannon(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        self.load_image()
        self.set_start_position()
        self.velocity = 5  # Speed for left/right movement
        self.shoot_cooldown = 0
        
    def load_image(self):
        image_path = os.getcwd() +"/pygame_implementation/game_pictures/canon.jpg"
        image = pygame.image.load(image_path).convert() # Load image
        image.set_colorkey((255,255,255))             # Converts background to transparent
        
        self.image = pygame.transform.scale(image, Constants.CANON_SIZE)  # Resize image
    def set_start_position(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = Constants.WIDTH // 2
        self.rect.bottom = Constants.HEIGHT
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
            
        if keys[pygame.K_RIGHT] and self.rect.right < Constants.WIDTH:
            self.rect.x += self.velocity
            



# If this script is run directly this will display the image in game window at the location sepcified
if __name__ == "__main__":
    
    # Configure the logging module
    logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

    # Initialize Pygame
    pygame.init()
    
    # Initialize Pygame screen
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Isolated Canon")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
   
    
    # Create an object with an attached image
    canon = Cannon()
    all_sprites.add(canon)
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

        # canon.xmas_tree_sprites.update()
        canon.update()
        
        # Draw everything
        screen.fill(Constants.BACKGROUND_COLOR)
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(Constants.FPS)


        