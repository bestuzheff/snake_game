import pygame

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20

head_x = width // 2
head_y = height // 2

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display.fill(green)
    pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])
    pygame.display.flip()