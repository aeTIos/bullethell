import sys
import pygame

import objectcode
import world
import classes
import gameassets

# initialise pygame things
pygame.init()
size1 = 640, 480
screen = pygame.display.set_mode(size1)
clock = pygame.time.Clock()

assets = gameassets.Assets()
game = world.World(assets)

patterns = objectcode.Patterns()


# test code
game.spawn(classes.GameObjectData(pos=(40, 40), direction=(0, 0),
                                  code=patterns.fourbulletspread))

while True:
    clock.tick()
    dt = clock.get_time() / 1000  # get time since last frame in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    game.update(game, dt)

    screen.fill((0, 0, 0))
    game.player.paint(screen)
    game.paint(screen)
    pygame.display.update()
