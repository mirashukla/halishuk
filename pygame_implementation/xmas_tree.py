import pygame
import sys
import os
import numpy as np
import copy 

from constants import Constants
from Blackhole import Blackhole

class Xmas_tree(pygame.sprite.Sprite):
    
    def __init__(self,start_coords):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        image_path = os.getcwd() +"/pygame_implementation/game_pictures/xmas_tree.jpeg"
        image = pygame.image.load(image_path).convert() # Load image
        image.set_colorkey((255,255,255))             # Converts background to transparent, assuming white background
        
        self.image = pygame.transform.scale(image, Constants.XMAS_TREE_SIZE)  # Resize image
        self.rect = self.image.get_rect()
        self.rect.centerx = start_coords[0]    #self.start_x()
        self.rect.centery = start_coords[1]     #self.start_y()
        self.velocity_y = -3  # Speed for up movement
        self.velocity_x = 0  # Speed for left/right movement
        self.blackhole = Blackhole()
        
    # def start_x(self):
    #     img_size_x = Constants.XMAS_TREE_SIZE[0]            # Get x value of canon size
    #     start_x = (Constants.WIDTH -img_size_x) // 2  # Put img in the center of screen and offset by img size
    #     return start_x
    
    # def start_y(self):
    #     img_size_y = Constants.XMAS_TREE_SIZE[1]       # Get y value of canon size
    #     start_y = Constants.HEIGHT - img_size_y  # Put image at bottom of screen and offset by img size
    #     return start_y
    
    def update(self):
        # Calculate distance between A (canon) and B (blackhole)
        dt = 1 #Constants.FPS
        G = 6.674 * 10**(-11) 
        x = copy.copy(self.rect.centerx)
        y = copy.copy(self.rect.centery)
        xV = copy.copy(self.velocity_x)   # Speed for left/right movement
        yV = copy.copy(self.velocity_y)   # Speed for up movement
        
        dx = self.blackhole.rect.centerx - x
        dy = self.blackhole.rect.centery - y
        r = np.sqrt(dx**2 + dy**2)

        # Calculate gravitational force components
        fx = G * (500 * Constants.BLACKHOLE_MASS) * dx / r**3
        fy = G * (500 * Constants.BLACKHOLE_MASS) * dy / r**3

        # Update velocities of A
        xV += fx * dt
        yV += fy * dt

        self.velocity_x= xV
        self.velocity_y= yV
        
        # Update the position of A
        self.rect.centerx = x + (xV * dt)
        self.rect.centery = y + (yV * dt) 

    #     print("xmas tree updated!")
        #self.rect.centery += self.velocity_y
        



# If this script is run directly this will display the image in game window at the location sepcified
if __name__ == "__main__":
    
    # Initialize Pygame
    pygame.init()
    
    # Initialize Pygame screen
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Isolated Canon")
    clock = pygame.time.Clock()
    
    # Define starting locations
    CENTER = [Constants.WIDTH//2, Constants.HEIGHT//2]
    BOTTOM_MIDDLE = [Constants.WIDTH//2, Constants.HEIGHT -25]
    TOP_MIDDLE = [Constants.WIDTH//2, 25]
    RBM = [Constants.WIDTH *60/100, Constants.HEIGHT -25]
    
    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    # Create an object with an attached image
    #start_X = Constants.WIDTH // 2 
    #start_y = Constants.HEIGHT // 2
    
   
    xmas_tree = Xmas_tree(RBM)
    all_sprites.add(xmas_tree)

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


        