import pygame
import random

pygame.init()



WIDTH = 600
HEIGHT = 600
BORDER_SIZE = 40
CELL_SIZE = 20

#Game state constant variables.
START = 0
PLAYING = 1
GAME_OVER = 2

#Variable for displayed score
score = 0

#Game fonts for game start and game over screens
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 28)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

#Game has begun.
game_state = START

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

    # +++++++++++++++
    #EVENT HANDLING SECTION
    # +++++++++++++++

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_state == START:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    game_state = PLAYING

        elif game_state == PLAYING:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0

                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0

                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -CELL_SIZE

                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = CELL_SIZE
        elif game_state == GAME_OVER:
            #To be added
            running = False

    #+++++++++++++++
    #GAME LOGIC SECTION#
    #+++++++++++++++
    if game_state == PLAYING:
        new_body = (
            snake[0][0] + dx,
            snake[0][1] + dy
        )

        # Add Body Part To Snake
        snake.insert(0, new_body)

        # Food Collision
        if new_body == (food_x, food_y):

            score += 1

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
            game_state = GAME_OVER

        if new_body[0] > WIDTH - BORDER_SIZE - CELL_SIZE:
            game_state = GAME_OVER

        if new_body[1] < BORDER_SIZE:
            game_state = GAME_OVER

        if new_body[1] > HEIGHT - BORDER_SIZE - CELL_SIZE:
            game_state = GAME_OVER

        # Self Collision
        if new_body in snake[1:]:
            game_state = GAME_OVER

    # +++++++++++++++
    #DRAWING SECTION
    # +++++++++++++++
    screen.fill((0, 0, 0))

    if game_state == START:
        title = font.render("SNAKE", True, (255, 255, 255))
        instructions = small_font.render(
            "Use the Arrow Keys to Move",
            True,
            (255, 255, 255)
        )

        food = small_font.render(
            "Eat the Yellow Food",
            True,
            (255, 255, 255)
        )

        avoid = small_font.render(
            "Avoid the Walls and Yourself",
            True,
            (255, 255, 255)
        )

        start = small_font.render(
            "Press SPACE to Begin",
            True,
            (255, 255, 0)
        )

        screen.blit(title, (220, 100))
        screen.blit(instructions, (160, 200))
        screen.blit(food, (190, 240))
        screen.blit(avoid, (160, 280))
        screen.blit(start, (175, 360))

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
    if game_state == PLAYING:
        # Draw Food
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (food_x, food_y,
             CELL_SIZE, CELL_SIZE)
        )

        #Draw Score
        score_text = small_font.render(
            f"Score: {score}",
            True,
            (255, 255, 255)
        )

        screen.blit(score_text, (15, 10))

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
    elif game_state == GAME_OVER:
        # Draw Border
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, WIDTH, BORDER_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (0, HEIGHT - BORDER_SIZE, WIDTH, BORDER_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, BORDER_SIZE, HEIGHT))
        pygame.draw.rect(screen, (255, 0, 0), (WIDTH - BORDER_SIZE, 0, BORDER_SIZE, HEIGHT))


        # Draw Snake
        for segment in snake:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
            )

        # Draw Food
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (food_x, food_y, CELL_SIZE, CELL_SIZE)
        )

        # Create Text
        game_over = font.render("GAME OVER", True, (255, 0, 0))
        quit_text = small_font.render("Press any key to quit", True, (255, 255, 255))
        score_text = small_font.render(
            f"Final Score: {score}",
            True,
            (255, 255, 255)
        )
        # Draw Text
        screen.blit(game_over, (170, 200))
        screen.blit(quit_text, (180, 280))
        screen.blit(score_text, (200, 260))

    pygame.display.flip()

    clock.tick(10)


pygame.quit()