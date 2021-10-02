from keys import *
pygame.init()

h = 1080
w = 1920

screen = pygame.display.set_mode((w,h))
running = True

def render(function):
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break

        function()
        pygame.display.update()

    pygame.quit()