import pygame

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20

display.fill(green)

pygame.display.flip()