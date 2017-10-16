import sys
import pygame
from classes import *


ship = pygame.image.load("thing.png")

pygame.init()
size1 = width, height = 640, 480

screen = pygame.display.set_mode(size1)


world = Game()
player = Player(1, 5, 3, ship)
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # add key handling

    world.update()  # where the magic happens owo
    # print('\n')
    clock.tick()
    print(clock.get_fps())
    player.paint(screen)
    world.paint(screen, pygame)

    pygame.display.update()

