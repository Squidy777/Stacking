import pygame
from pygame.locals import *
from typing import List
# from dropping_blocks import DroppingBlocks

class AttrDict:
    def __init__(self,d):
        ...
        # self.__dict__ = d
    ...


class Sprite:
    def __init__(self,sprite:str, x=0, y=0, z=0, size:tuple=(100,100),physics_meta=None,event_fn=lambda _:None):
        # sprite is basically a raster || picture
        self.image = pygame.image.load(sprite).convert_alpha()
        # self.image = sprite
        self.size = size
        self.x = x
        self.y = y


        self.xac = 0
        self.yac = 0

        self.event_fn = event_fn

        self.physics_meta = AttrDict(physics_meta)
        self.static = False
        ...

    def draw(self, display,cam):  # c stands for camera
        cx, cy, csize = cam()
        image = pygame.transform.scale(self.image, self.size)
        display.blit(image, pygame.rect.Rect((self.x+cx,self.y+cy,self.x+self.size[0],self.y+self.size[1])))
        ...


class SceneSpace:
    def __init__(self):
        self.objects:List[Sprite] = []

        ...

    def append(self,object:Sprite):
        self.objects.append(object)
        ...

    def draw(self, display, cam):
        for object in self.objects:
            object.draw(display,cam)
        ...

    def __call__(self):
        # return
        for object in self.objects:
            if not type(object).__name__ == 'DroppingBlocks':
                object.event_fn(object)


class Camera:
    def __init__(self,x=0,y=0,scale=1):
        self.x = x
        self.y = y
        self.scale = scale

    def __call__(self, *args, **kwargs):
        return self.x, self.y, self.scale
        ...


class StaticRepeat(Sprite):
    def draw(self, display,cam):
        cx, cy, csize = cam()
        image = pygame.transform.scale(self.image, self.size)

        for i in range(6):
            display.blit(image, (i*800-400,0))