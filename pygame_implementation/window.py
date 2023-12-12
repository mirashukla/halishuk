import pygame
import os

class Window(pygame.sprite.Sprite):
    WIDTH = 800
    HEIGHT = 800
    def __init__(self):
        super().__init__()  # Calls parent class construtor (allows inheritance of more properties)
        
        self.blackhole_start_pos = [self.WIDTH // 2, self.HEIGHT // 2]
        self.blackhole_mass = 10000000000
        self.canon_stat_pos = [self.WIDTH // 2, self.HEIGHT]
        
    def set_start_position(self,start_coords):
        self.rect = self.image.get_rect()
        self.rect.centerx = start_coords[0]
        self.rect.bottom = start_coords[1]
        
    def load_image(self, img_name, size):
        image_path = os.getcwd() +"/pygame_implementation/game_pictures/" + img_name
        image = pygame.image.load(image_path)   # Load image
       # image.set_colorkey((255,255,255))             # Converts background to transparent
        self.image = pygame.transform.scale(image, size)  # Resize image