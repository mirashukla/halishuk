import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60

# background color
RED = (255, 10, 10)


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, width_of_window, height_of_window, image_path):
        
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        
        image = pygame.image.load(image_path).convert() # Load image
        image.set_colorkey((255, 255, 255))             # Converts background to transparent
        self.size_of_image = (100,100)                  # set desire size of image
        
        self.image = pygame.transform.scale(image, self.size_of_image)  # Resize image
        self.rect = self.image.get_rect()
        self.rect.x = self.start_x(width_of_window)
        self.rect.y = self.start_y(height_of_window)
        
    def start_x(self,width_of_window):
        img_size_x = self.size_of_image[0]            # Get x value of canon size
        start_x = (width_of_window -img_size_x) // 2  # Put img in the center of screen and offset by img size
        return start_x
    
    def start_y(self,height_of_window):
        img_size_y = self.size_of_image[1]       # Get y value of canon size
        start_y = height_of_window - img_size_y  # Put image at bottom of screen and offset by img size
        return start_y
        

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Attachment Example")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create an object with an attached image
img_path = "/home/bailey/Documents/Software Exploration/Project with mira/hallishuk/game_pictures/canon.jpg"
object_with_image = GameObject(WIDTH, HEIGHT, img_path)
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

    # Cap the frame rate
    clock.tick(FPS)
