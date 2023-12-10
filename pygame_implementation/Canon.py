import pygame
import sys
import os
import logging

from constants import Constants
from xmas_tree import Xmas_tree

class Canon(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        image_path = os.getcwd() +"/game_pictures/canon.jpg"
        image = pygame.image.load(image_path).convert() # Load image
        image.set_colorkey((255,255,255))             # Converts background to transparent
        
        self.image = pygame.transform.scale(image, Constants.CANON_SIZE)  # Resize image
        self.rect = self.image.get_rect()
        self.rect.x = self.start_x()
        self.rect.y = self.start_y()
        self.velocity = 5  # Speed for left/right movement
        self.shoot_cooldown = 0
        
    def start_x(self):
        img_size_x = Constants.CANON_SIZE[0]            # Get x value of canon size
        start_x = (Constants.WIDTH -img_size_x) // 2  # Put img in the center of screen and offset by img size
        return start_x
    
    def start_y(self):
        img_size_y = Constants.CANON_SIZE[1]       # Get y value of canon size
        start_y = Constants.HEIGHT - img_size_y  # Put image at bottom of screen and offset by img size
        return start_y
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
            
        if keys[pygame.K_RIGHT] and self.rect.right < Constants.WIDTH:
            self.rect.x += self.velocity
            
        if keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.shoot_cooldown = Constants.FPS // 4  # Cooldown for shooting
            xmas_tree = Xmas_tree(self.rect.centerx, self.rect.top)
            all_sprites.add(xmas_tree)
            xmas_tree_list.append(xmas_tree)
            logging.info(f"Number of xmas_trees in memory: {len(xmas_tree_list)}")




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
    xmas_tree_list = []
    
    # Create an object with an attached image
    canon = Canon()
    all_sprites.add(canon)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # Update all sprites
        all_sprites.update()
        
            # Handle shooting cooldown
        if canon.shoot_cooldown > 0:
            canon.shoot_cooldown -= 1

        # Update cooldown for all instances of Object C
        for xmas_tree in xmas_tree_list:
            if xmas_tree.rect.bottom < 0:
                all_sprites.remove(xmas_tree)
                xmas_tree_list.remove(xmas_tree)
                logging.info(f"Number of xmas_trees in memory: {len(xmas_tree_list)}")

        # Draw everything
        screen.fill(Constants.BACKGROUND_COLOR)
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(Constants.FPS)


        