import pygame
import sys
import os
from constants import Constants

class Blackhole(pygame.sprite.Sprite):
    
    def __init__(self,image_path):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        
        image = pygame.image.load(image_path)#.convert_alpha() # Load image
        
        self.image = pygame.transform.scale(image, Constants.BLACKHOLE_SIZE)  # Resize image
        self.rect = self.image.get_rect()
        self.rect.x = self.start_x()
        self.rect.y = self.start_y()
        
    def start_x(self):
        img_size_x = Constants.BLACKHOLE_SIZE[0]            # Get x value of canon size
        start_x = (Constants.WIDTH -img_size_x) // 2  # Put img in the center of screen and offset by img size
        return start_x
    
    def start_y(self):
        img_size_y = Constants.BLACKHOLE_SIZE[1]       # Get y value of canon size
        start_y = (Constants.HEIGHT -img_size_y) // 2  # Put image at bottom of screen and offset by img size
        return start_y



# If this script is run directly this will display the image in game window at the location sepcified
if __name__ == "__main__":
    
    # Initialize Pygame
    pygame.init()

    # background color
    RED = (255, 10, 10)
    WHITE = (255, 255, 255)
    
    # Initialize Pygame screen
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption("Image Attachment Example")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()

    # Create an object with an attached image
    img_path = os.getcwd() + "/game_pictures/blackhole.png"
    object_with_image = Blackhole(img_path)
    all_sprites.add(object_with_image)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw everything
        screen.fill(RED)
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()