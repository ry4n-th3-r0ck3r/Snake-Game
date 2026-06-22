import pygame

pygame.init()

# Window settings
WIDTH = 600
HEIGHT = 600
BORDER_SIZE = 20
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Clock for Frames per Second
clock = pygame.time.Clock()

# Snake head position
x = 300
y = 300

# Starting Direction (Snake goes Right)
dx = CELL_SIZE
dy = 0

# Main game loop
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

    # Move Snake
    x += dx
    y += dy

    # Collision Detection
    if x < BORDER_SIZE:
        running = False

    if x > WIDTH - BORDER_SIZE - CELL_SIZE:
        running = False

    if y < BORDER_SIZE:
        running = False

    if y > HEIGHT - BORDER_SIZE - CELL_SIZE:
        running = False

    # Draw Frame
    screen.fill((0, 0, 0))

    # Top Border
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (0, 0, WIDTH, BORDER_SIZE)
    )

    # Bottom Border
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (0, HEIGHT - BORDER_SIZE, WIDTH, BORDER_SIZE)
    )

    # Left Border
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (0, 0, BORDER_SIZE, HEIGHT)
    )

    # Right Border
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (WIDTH - BORDER_SIZE, 0, BORDER_SIZE, HEIGHT)
    )

    # Snake Head
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (x, y, CELL_SIZE, CELL_SIZE)
    )

    pygame.display.flip()

    # Snake Speed
    clock.tick(10)

pygame.quit()