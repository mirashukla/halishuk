import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class ObjectA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLACK, (20, 20), 20)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.gravity_radius = 150

class ObjectB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 20))
        self.velocity = 5  # Speed for left/right movement
        self.shoot_cooldown = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.shoot_cooldown = FPS // 2  # Cooldown for shooting
            object_c = ObjectC(self.rect.centerx, self.rect.top)
            all_sprites.add(object_c)
            objects_c_list.append(object_c)

class ObjectC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 128, 0), [(20, 0), (0, 60), (40, 60)])  # Tree body
        pygame.draw.polygon(self.image, (255, 215, 0), [(10, 0), (0, 20), (20, 20)])  # First layer
        pygame.draw.polygon(self.image, (255, 215, 0), [(10, 20), (0, 40), (20, 40)])  # Second layer
        pygame.draw.polygon(self.image, (255, 215, 0), [(10, 40), (0, 60), (20, 60)])  # Third layer
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_y = -2  # Initial upward velocity
        self.mass = 1

    def update(self):
        self.rect.y += self.velocity_y

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Interaction Example")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
objects_a = pygame.sprite.Group()
objects_b = pygame.sprite.Group()
objects_c_list = []  # List to store multiple instances of Object C

# Create objects
object_a = ObjectA()
object_b = ObjectB()

# Add objects to sprite groups
all_sprites.add(object_a, object_b)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update all sprites
    all_sprites.update()

    # Handle shooting cooldown
    if object_b.shoot_cooldown > 0:
        object_b.shoot_cooldown -= 1

    # Update cooldown for all instances of Object C
    for object_c in objects_c_list:
        if object_c.rect.bottom < 0:
            all_sprites.remove(object_c)
            objects_c_list.remove(object_c)

    # Update gravity effect for all instances of Object C
    for object_c in objects_c_list:
        distance = math.hypot(object_a.rect.centerx - object_c.rect.centerx,
                              object_a.rect.centery - object_c.rect.centery)
        if distance < object_a.gravity_radius:
            gravitational_force = 1 / (distance ** 2)  # Simplified gravitational force
            angle = math.atan2(object_a.rect.centery - object_c.rect.centery,
                               object_a.rect.centerx - object_c.rect.centerx)
            object_c.velocity_y += gravitational_force * math.sin(angle)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
