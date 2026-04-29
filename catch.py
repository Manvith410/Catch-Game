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
GOLD = (255, 215, 0)
# Game objects
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 7
apple_size = 30
apple_x = random.randint(0, WIDTH - apple_size)
apple_y = 0
apple_speed = 5
bonus_x = random.randint(0, WIDTH - apple_size)
bonus_y = -100  # start offscreen
bonus_active = False  # not visible at start
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
        # Randomly spawn bonus item
if not bonus_active and random.randint(1, 180) == 1:
    bonus_active = True
    bonus_x = random.randint(0, WIDTH - apple_size)
    bonus_y = 0
if bonus_active:
    bonus_y += apple_speed
    # Move apple
    apple_y += apple_speed
    # Check catch
    if (basket_y < apple_y + apple_size and
        basket_x < apple_x + apple_size and
        basket_x + basket_width > apple_x):
        score += 1
        apple_x = random.randint(0, WIDTH - apple_size)
        apple_y = 0
        apple_speed += 0.3
    # Check miss
    if apple_y > HEIGHT:
        misses += 1
        apple_x = random.randint(0, WIDTH - apple_size)
        apple_y = 0
        # Check bonus catch
if bonus_active and (basket_y < bonus_y + apple_size and
    basket_x < bonus_x + apple_size and
    basket_x + basket_width > bonus_x):
    score += 2
    bonus_active = False
    bonus_y = -100

# Check bonus miss
if bonus_active and bonus_y > HEIGHT:
    bonus_active = False
    bonus_y = -100
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
    pygame.draw.rect(screen, RED, (apple_x, apple_y, apple_size, apple_size))
    if bonus_active:
        pygame.draw.rect(screen, GOLD, (bonus_x, bonus_y, apple_size, apple_size))
    # Draw score and hearts
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    for i in range(3 - misses):
        screen.blit(heart_img, (WIDTH - 120 - (i * 110), 10))
    pygame.display.flip()
pygame.quit()
