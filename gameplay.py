from render import *
from scene_space import *
from dropping_blocks import *
from physics import *

camera = Camera(x=900,y=600)
scene_space = SceneSpace()
physics_handler = PhysicsHandler(scene_space)


car = Sprite('basecart.png',event_fn=car_controls)
dropping_blocks = DroppingBlocks(physics_handler)
floor = StaticRepeat('background.png',x=0,y=0,size=(500,250))


scene_space.append(car)
# scene_space.append(floor)
scene_space.append(dropping_blocks)

physics_handler.append(dropping_blocks.blocks)
image = pygame.image.load("background.png")


@render
def game_play():
    physics_handler()
    scene_space()
    dropping_blocks()

    screen.blit(image,(0,0))



    # screen.fill(255)
    # pygame.draw.rect(screen, (0,255,0), pygame.Rect(0, 1080-220,1920, 1080))

    scene_space.draw(screen,camera)


    ...