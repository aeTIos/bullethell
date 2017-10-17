import classes


class Patterns:
    # everything under this is testing code
    def fourbulletspread(self, parent, world, dt):
        assets = world.assets
        data = parent.data
        if data.init is False:
            data.init = True
            data.bullets = [world.spawn(classes.GameObjectData(
                                        pos=[data.pos[0], data.pos[1]],
                                        rot=0,
                                        direction=[0, 0.02],
                                        sprite=assets.bullet,
                                        code=self.bulletcode))]

        data.bullets[0].data.pos[0] += 10*dt

        if data.bullets[0].data.pos[0] > 250:
            data.bullets[0].data.init = True
            world.despawn(parent)

    def bulletcode(self, parent, world, dt):
        data = parent.data

        def doesthiswork():
            if data.init is True:
                if data.pos[0] < world.player.x:
                    data.pos[0] += 0.02
                data.pos[0] += data.direction[0]
                data.pos[1] += data.direction[1]

        if data.init is True:
            doesthiswork()


