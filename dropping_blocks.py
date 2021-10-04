from scene_space import *
from random import randint


class DroppingBlocks:
    def __init__(self,physics_obj):
        self.physics_obj = physics_obj
        self.static = True
        # self.event_fn = lambda x:None
        self.offset = offset = 600
        self.offsetx = offsetx = 20

        self.create_sprite = lambda:Sprite('sprites/log.png',
                                           x=randint(-offsetx,offsetx),y=randint(-700-offset,-700+offset))

        self.blocks = [
            self.create_sprite() for _ in range(3)
        ]

    def draw(self, display, cam):  # c stands for cameras
        cx, cy, csize = cam()

        for block in self.blocks:
            block.draw(display,cam)

            # image = pygame.transform.scale(self.image, self.size)
            # display.blit(image, pygame.rect.Rect((self.x + cx, self.y + cy, self.x + self.size[0], self.y + self.size[1])))
        ...

    def __call__(self):
        if not randint(0,10):
            o = self.create_sprite()
            self.physics_obj.append([o])
            self.blocks.append(o)


        # asfsaf
        ...
