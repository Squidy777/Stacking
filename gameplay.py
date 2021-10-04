import pygame, sys, random
from render import *
from scene_space import *
from dropping_blocks import *
from physics import *
import pathlib


pygame.init()

size = (1920, 1080)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Menu")

click = False

fps = pygame.time.Clock()

menu_button = pygame.Rect(size[0] / 2 - 200, size[1] / 2, 400, 80)

menu_button_color = (255,0,0)

menu_color = (0,255,0)

while True:
    screen.fill(menu_color)


    mx, my = pygame.mouse.get_pos()

    pygame.draw.rect(screen, menu_button_color, menu_button)

    if click:
        if menu_button.collidepoint((mx, my)):

            camera = Camera(x=900, y=600)
            scene_space = SceneSpace()
            physics_handler = PhysicsHandler(scene_space)

            car = Sprite('basecart.png', event_fn=car_controls)
            dropping_blocks = DroppingBlocks(physics_handler)
            floor = StaticRepeat('background.png', x=0, y=0, size=(500, 250))

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

                screen.blit(image, (0, 0))

                # screen.fill(255)
                # pygame.draw.rect(screen, (0,255,0), pygame.Rect(0, 1080-220,1920, 1080))

                scene_space.draw(screen, camera)

                ...

    click = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.update()
    fps.tick(120)

