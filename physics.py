from scene_space import *
import pymunk

class PhysicsHandler:
    def __init__(self,scene_space:SceneSpace):
        self.children = scene_space.objects
        self.space = pymunk.Space()
        ...

    def append(self,list_):
        self.children.extend(list_)

    def __call__(self):
        for object in self.children:

            if object.static == False:
                object.yac += 0.004
                object.y += object.yac
                object.x += object.xac

                if object.y>200:
                    object.y = 199
                    object.yac = -abs(object.yac)/10
