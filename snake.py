import pygame
import time

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20
snake_speed = 12

head_x = width // 2
head_y = height // 2

vx = 0
vy = 0

clock = pygame.time.Clock()

while True:

    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
        font = pygame.font.SysFont("None", 100) 
        f_width, f_height = font.size("GAME OVER")
        message = font.render("GAME OVER", True, (255, 0, 0))
        display.blit(message, [(width - f_width) // 2, (height - f_height) // 2])
        pygame.display.flip()
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
    pygame.display.flip()
    clock.tick(snake_speed)