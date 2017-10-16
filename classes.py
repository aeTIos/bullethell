class Game:
    def __init__(self):
        self.entities = []

    def spawn(self, data):
        self.entities.append(GameObject(data))
        # print('spawned object: ', self.entities[-1])

    def despawn(self, entity):
        self.entities.remove(entity)

    def update(self):
        print('number of entities:', len(self.entities))
        for entity in self.entities:
            entity.update()

    def paint(self, buffer, pygame):
        for entity in self.entities:
            buffer.blit(pygame.transform.rotate(entity.data.sprite, entity.data.rot), (entity.data.x, entity.data.y))


class Player:
    def __init__(self, speed, lives, bombs, sprite):
        self.x = 320
        self.y = 300
        self.speed = speed
        self.lives = lives
        self.bombs = bombs
        self.sprite = sprite

    def paint(self, buffer):
        buffer.blit(self.sprite, (self.x, self.y))


class GameObjectData:
    def __init__(self, x, y, rot, scale, sprite, ent_type, code):
        self.x = x
        self.y = y
        self.rot = rot
        self.scale = scale
        self.sprite = sprite

        self.ent_type = ent_type

        self.code = code

        self.init = False


class GameObject:
    def __init__(self, data):
        self.data = data

    def update(self):
        self.data.code(self)