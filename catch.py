import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catching Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (220, 50, 50)
BLACK = (0, 0, 0)

# Game objects
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 7

item_size = 30
item_x = random.randint(0, WIDTH - item_size)
item_y = 0
item_speed = 5

score = 0
misses = 0
font = pygame.font.SysFont("segoeui", 40)
heart_img = pygame.image.load("heart.png")
heart_img = pygame.transform.scale(heart_img, (100, 100))
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move item
    item_y += item_speed

    # Check catch
    if (basket_y < item_y + item_size and
        basket_x < item_x + item_size and
        basket_x + basket_width > item_x):
        score += 1
        item_x = random.randint(0, WIDTH - item_size)
        item_y = 0
        item_speed += 0.3

    # Check miss
    if item_y > HEIGHT:
        misses += 1
        item_x = random.randint(0, WIDTH - item_size)
        item_y = 0

    # Game over
    if misses >= 3:
        screen.fill(BLACK)
        msg = font.render(f"Game Over! Score: {score}", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

   # Draw everything
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.rect(screen, RED, (item_x, item_y, item_size, item_size))

    # Draw score and hearts
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    for i in range(3 - misses):
        screen.blit(heart_img, (WIDTH - 120 - (i * 30), 10))

    pygame.display.flip()

pygame.quit()