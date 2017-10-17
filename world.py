import classes
import pygame


class World:
    def __init__(self, assets):
        self.assets = assets
        self.entities = []
        self.player = classes.Player(speed=1, lives=5, bombs=3, sprite=assets.ship)

    def paint(self, buffer):
        for entity in self.entities:
            if entity.data.sprite is not None:
                buffer.blit(
                    pygame.transform.rotate(entity.data.sprite, entity.data.rot), entity.data.pos)

    def spawn(self, data):
        self.entities.append(classes.GameObject(data))
        return self.entities[-1]

    def despawn(self, entity):
        self.entities.remove(entity)

    def update(self, world, dt):
        for entity in self.entities:
            entity.update(world, dt)
