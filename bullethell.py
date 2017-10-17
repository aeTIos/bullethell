import sys
import pygame

import objectcode
import world
import classes
import assets

# initialise pygame things
pygame.init()
size1 = 640, 480
screen = pygame.display.set_mode(size1)
clock = pygame.time.Clock()

# test code
player = classes.Player(speed=1, lives=5, bombs=3, sprite=assets.ship)
world.spawn(classes.GameObjectData(pos=(40, 40), direction=(0, 0), rot=None, scale=None, sprite=None, ent_type=None,
            code=objectcode.fourbulletspread))

while True:
    clock.tick()
    dt = clock.get_time() / 1000  # get time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    world.update(player, dt)

    screen.fill((0, 0, 0))
    player.paint(screen)
    world.paint(screen)
    pygame.display.update()

