import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class ObjectA(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLACK, (20, 20), 20)
        self.rect = self.image.get_rect(center=(x, y))
        self.gravity_radius = 200  # Adjust the radius as needed

    def apply_gravity(self, object_c):
        distance = math.hypot(self.rect.centerx - object_c.rect.centerx,
                              self.rect.centery - object_c.rect.centery)
        if distance < self.gravity_radius:
            angle = math.atan2(self.rect.centery - object_c.rect.centery,
                               self.rect.centerx - object_c.rect.centerx)
            gravitational_force = 1 / (distance ** 2)  # Simplified gravitational force
            object_c.velocity_x += gravitational_force * math.cos(angle)
            object_c.velocity_y += gravitational_force * math.sin(angle)

class ObjectB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 20))

class ObjectC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (10, 10), 10)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_x = 0  # Initial velocities
        self.velocity_y = -10  # Adjusted to half the initial speed


# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Window")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
objects_a = pygame.sprite.Group()
objects_b = pygame.sprite.Group()
objects_c_list = []  # List to store multiple instances of Object C

# Create objects
object_a = ObjectA(WIDTH // 2, HEIGHT // 2)
object_b = ObjectB()

# Add objects to sprite groups
all_sprites.add(object_a, object_b)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                object_b.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                object_b.rect.x += 10
            elif event.key == pygame.K_SPACE:
                # Create a new instance of Object C
                object_c = ObjectC(object_b.rect.centerx, object_b.rect.y)
                objects_c_list.append(object_c)
                all_sprites.add(object_c)

    # Update all instances of Object C
    for object_c in objects_c_list:
        object_c.rect.x += object_c.velocity_x
        object_c.rect.y += object_c.velocity_y

        # Check collision with Object A
        if pygame.sprite.spritecollide(object_a, objects_c_list, False):
            object_a.apply_gravity(object_c)

        # Check collision with Object B
        if pygame.sprite.spritecollide(object_b, objects_c_list, False):
            objects_c_list.remove(object_c)
            all_sprites.remove(object_c)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
