import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_block_size = 10
snake_speed = 15
snake_x, snake_y = width // 2, height // 2
snake_x_change, snake_y_change = 0, 0
snake_body = []
snake_length = 1

food_x = round(random.randrange(0, width - snake_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_block_size) / 10.0) * 10.0

# Define functions
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(window, black, [block[0], block[1], snake_block_size, snake_block_size])

def draw_food(food_x, food_y):
    pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block_size) / 10.0) * 10.0
        snake_length += 1

    # Update snake body
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for collision with boundaries or self
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height or snake_head in snake_body[:-1]:
        game_over = True

    # Clear the window
    window.fill(white)

    # Draw snake and food
    draw_snake(snake_body)
    draw_food(food_x, food_y)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
