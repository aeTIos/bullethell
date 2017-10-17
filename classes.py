class Player:
    def __init__(self, speed, lives, bombs, sprite):
        self.x = 300
        self.y = 300
        self.speed = speed
        self.lives = lives
        self.bombs = bombs
        self.sprite = sprite

    def paint(self, buffer):
        buffer.blit(self.sprite, (self.x, self.y))


class GameObjectData:
    def __init__(self, pos, direction, rot, scale, sprite, ent_type, code):
        self.pos = pos
        self.direction = direction
        self.rot = rot
        self.scale = scale
        self.sprite = sprite
        self.ent_type = ent_type
        self.code = code
        self.init = False


class GameObject:
    def __init__(self, data):
        self.data = data

    def update(self, player, dt):
        self.data.code(self, player, dt)