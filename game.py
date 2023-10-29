import pygame

# pygame setup
pygame.init()
window_height = 800
window_width = 600
screen = pygame.display.set_mode((window_height, window_width))
# PyGame clock
FPS = 10 
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CRIMSON = (220, 0, 0,)
ORGANGE = (255, 127, 0)

bg = pygame.image.load('people.jpg')
bg_rect = bg.get.rect()
bg_rect.topleft = (0, 0)

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Black")
    screen.blit(bg, bg_rect)


    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
