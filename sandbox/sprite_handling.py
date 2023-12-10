import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CANON_SPEED = 5
XMAS_TREE_SPEED = 3

# Cannon class
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Replace with your actual image
        self.image.fill((255, 0, 0))  # Replace with your desired color
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= CANON_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += CANON_SPEED

# XmasTree class
class XmasTree(pygame.sprite.Sprite):
    def __init__(self, start_x):
        super().__init__()
        self.image = pygame.Surface((30, 50))  # Replace with your actual image
        self.image.fill((0, 255, 0))  # Replace with your desired color
        self.rect = self.image.get_rect(center=(start_x, HEIGHT))

    def update(self):
        self.rect.y -= XMAS_TREE_SPEED
        if self.rect.bottom < 0:
            self.kill()

# Initialize Pygame
pygame.init()

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cannon and Xmas Trees")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
xmas_trees = pygame.sprite.Group()

# Create game objects
cannon = Cannon()
all_sprites.add(cannon)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Spawn Xmas tree when space bar is pressed
            xmas_tree = XmasTree(cannon.rect.centerx)
            all_sprites.add(xmas_tree)
            xmas_trees.add(xmas_tree)

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.fill((255, 255, 255))  # Replace with your desired background color
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
