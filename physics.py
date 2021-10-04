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
        # [ (pymunk.Body())for object in self.children]

        run_collision(self.children)

        for object in self.children:


            if object.static == False:
                object.yac += 0.4
                object.y += object.yac
                object.x += object.xac

                if object.y>200:
                    object.y = 199
                    object.yac = -abs(object.yac)/10



def run_collision(body_list):
    for obj in body_list:
        if not obj.static:
            for obj_y in body_list:
                if not obj_y.static:
                    if abs(obj.x-obj_y.x) < 40:
                        d = (obj.x-obj_y.x)/200
                        obj.xac   += d
                        obj_y.xac -= d

                    if abs(obj.y-obj_y.y) < 40:
                        d = (obj.y-obj_y.y)/200
                        obj.yac   += d
                        obj_y.yac -= d




            