import pygame
import time
import random
import os

os.getcwd()

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20
snake_speed = 12

head_x = width // 2 // segment_size * segment_size
head_y = height // 2 // segment_size * segment_size

vx = 0
vy = 0

clock = pygame.time.Clock()

snake = []
snake_lenght = 1

def get_random_point():
    x = random.randint(0, width - segment_size) // segment_size * segment_size
    y = random.randint(0, height - segment_size) // segment_size * segment_size
    return x, y


def show_snake(snake_list):
    for _x, _y in snake_list:
        pygame.draw.rect(display, black, [_x, _y, segment_size, segment_size])


# def show_score(score):
#     _font = pygame.font.SysFont("./arial.ttf", 30)
#     value = _font.render("Очки: " + str(score), True, black)
#     display.blit(value, [10, 10])




food_x, food_y = get_random_point()


while True:

    game_over = False
    # Проверим столкновение со снеткой
    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
        game_over = True

    if game_over:
        # font = pygame.font.SysFont("./arial.ttf", 100)
        # f_width, f_height = font.size("GAME OVER")
        # message = font.render("GAME OVER", True, (255, 0, 0))
        # display.blit(message, [(width - f_width) // 2, (height - f_height) // 2])
        # pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vy = segment_size
                vx = 0
            elif event.key == pygame.K_UP:
                vy = -segment_size
                vx = 0
            elif event.key == pygame.K_LEFT:
                vy = 0
                vx = -segment_size
            elif event.key == pygame.K_RIGHT:
                vy = 0
                vx = segment_size

    head_x += vx
    head_y += vy

    display.fill(green)
    pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])

    snake.append((head_x, head_y))
    if len(snake) > snake_lenght:
        del(snake[0])

    show_snake(snake)
    # show_score(snake_lenght - 1)

    pygame.draw.rect(display, (255, 0, 0), [food_x, food_y, segment_size, segment_size])

    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        snake_lenght += 1

    pygame.display.flip()
    clock.tick(snake_speed)
