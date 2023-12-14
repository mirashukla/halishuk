import pygame
import sys
import numpy as np


from constants import Constants
from window import Window

class Xmas_tree(Window):
    
    def __init__(self,start_coords):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        
        self.load_image("xmas_tree.jpeg", (20,20))
        self.set_start_position(start_coords)
        
        self.velocity_y = -1  # intial speed for up movement
        self.velocity_x = 0  # Speed for left/right movement


    def update(self):
        # Calculate distance between A (canon) and B (blackhole)
        dt = 1 #Constants.FPS
        G = 6.674 * 10**(-11) 
        x = self.rect.centerx # copy.copy(self.rect.centerx)
        y = self.rect.centery #copy.copy(self.rect.centery)
        xV = self.velocity_x # copy.copy(self.velocity_x)   # Speed for left/right movement
        yV = self.velocity_y # copy.copy(self.velocity_y)   # Speed for up movement
        
        dx = self.blackhole_start_pos[0] - x
        dy = self.blackhole_start_pos[1] - y
        r = np.sqrt(dx**2 + dy**2)

        # Calculate gravitational force components
        fx = G * (1 * self.blackhole_mass) * dx / r**3
        fy = G * (1 * self.blackhole_mass) * dy / r**3

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
    screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
    pygame.display.set_caption("Isolated Canon")
    clock = pygame.time.Clock()
    
    # Define starting locations
    CENTER = [Window.WIDTH//2, Window.HEIGHT//2]
    BOTTOM_MIDDLE = [Window.WIDTH//2, Window.HEIGHT -25]
    TOP_MIDDLE = [Window.WIDTH//2, 25]
    RBM = [Window.WIDTH *60/100, Window.HEIGHT -25]
    
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


        