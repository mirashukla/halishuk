import pygame
import sys
import os
from constants import Constants

class Xmas_tree(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        image_path = os.getcwd() +"/game_pictures/xmas_tree.jpeg"
        image = pygame.image.load(image_path).convert() # Load image
        image.set_colorkey((255,255,255))             # Converts background to transparent, assuming white background
        
        self.image = pygame.transform.scale(image, Constants.XMAS_TREE_SIZE)  # Resize image
        self.rect = self.image.get_rect()
        self.rect.x = x     #self.start_x()
        self.rect.y = y     #self.start_y()
        self.velocity = 5  # Speed for left/right movement
        
    def start_x(self):
        img_size_x = Constants.XMAS_TREE_SIZE[0]            # Get x value of canon size
        start_x = (Constants.WIDTH -img_size_x) // 2  # Put img in the center of screen and offset by img size
        return start_x
    
    def start_y(self):
        img_size_y = Constants.XMAS_TREE_SIZE[1]       # Get y value of canon size
        start_y = Constants.HEIGHT - img_size_y  # Put image at bottom of screen and offset by img size
        return start_y
    
    def update(self):
        
        if self.rect.bottom < 0:
            self.kill()
 
        self.rect.y -= self.velocity
        



# If this script is run directly this will display the image in game window at the location sepcified
if __name__ == "__main__":
    
    # Initialize Pygame
    pygame.init()
    
    # Initialize Pygame screen
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Isolated Canon")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    # Create an object with an attached image
    start_X = Constants.WIDTH // 2 
    start_y = Constants.HEIGHT
    xmas_tree = Xmas_tree(start_X,start_y)
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


        