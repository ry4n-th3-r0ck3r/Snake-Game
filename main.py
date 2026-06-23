import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
BORDER_SIZE = 20
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Snake starts with one segment
snake = [(300, 300)]

# Moving right initially
dx = CELL_SIZE
dy = 0

# Food
food_x = random.randrange(BORDER_SIZE,
                          WIDTH - BORDER_SIZE,
                          CELL_SIZE)

food_y = random.randrange(BORDER_SIZE,
                          HEIGHT - BORDER_SIZE,
                          CELL_SIZE)
#Main game loop
running = True

while running:

    # Handle Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                dx = -CELL_SIZE
                dy = 0

            elif event.key == pygame.K_RIGHT:
                dx = CELL_SIZE
                dy = 0

            elif event.key == pygame.K_UP:
                dx = 0
                dy = -CELL_SIZE

            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = CELL_SIZE

    # Create New Body Part
    new_body = (
        snake[0][0] + dx,
        snake[0][1] + dy
    )

    # Add Body Part To Snake
    snake.insert(0, new_body)

    # Food Collision
    if new_body == (food_x, food_y):

        food_x = random.randrange(
            BORDER_SIZE,
            WIDTH - BORDER_SIZE,
            CELL_SIZE
        )

        food_y = random.randrange(
            BORDER_SIZE,
            HEIGHT - BORDER_SIZE,
            CELL_SIZE
        )

    else:
        # Remove Tail
        snake.pop()

    # Wall Collision
    if new_body[0] < BORDER_SIZE:
        running = False

    if new_body[0] > WIDTH - BORDER_SIZE - CELL_SIZE:
        running = False

    if new_body[1] < BORDER_SIZE:
        running = False

    if new_body[1] > HEIGHT - BORDER_SIZE - CELL_SIZE:
        running = False

    # Self Collision
    if new_body in snake[1:]:
        running = False

    # Draw Frame
    screen.fill((0, 0, 0))

    # Borders
    pygame.draw.rect(screen, (255, 0, 0),
                     (0, 0, WIDTH, BORDER_SIZE))

    pygame.draw.rect(screen, (255, 0, 0),
                     (0, HEIGHT - BORDER_SIZE,
                      WIDTH, BORDER_SIZE))

    pygame.draw.rect(screen, (255, 0, 0),
                     (0, 0, BORDER_SIZE, HEIGHT))

    pygame.draw.rect(screen, (255, 0, 0),
                     (WIDTH - BORDER_SIZE,
                      0,
                      BORDER_SIZE,
                      HEIGHT))

    # Draw Food
    pygame.draw.rect(
        screen,
        (255, 255, 0),
        (food_x, food_y,
         CELL_SIZE, CELL_SIZE)
    )

    # Snake
    for segment in snake:

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (segment[0],
             segment[1],
             CELL_SIZE,
             CELL_SIZE)
        )

    pygame.display.flip()

    clock.tick(10)

pygame.quit()