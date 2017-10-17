import classes
import pygame

entities = []


def paint(buffer):
    for entity in entities:
        if entity.data.sprite is not None:
            buffer.blit(
                pygame.transform.rotate(entity.data.sprite, entity.data.rot), entity.data.pos)


def spawn(data):
    entities.append(classes.GameObject(data))
    return entities[-1]


def despawn(entity):
    entities.remove(entity)


def update(player, dt):
    for entity in entities:
        entity.update(player, dt)

