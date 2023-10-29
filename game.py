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

rows = 3
cols = 3
num_cells = rows * cols 

cell_width = window_width // rows 
cell_height = window_height // cols 

cells = []
rand_indexes = list (range(0, num_cells))
print(rand_indexes)
print()
for i in range (num_cells):
    x = (i % rows) * cell_width 
    y = (i // cols) * cell_height
    rect = pygame.rect(x, y, cell_width, cell_height)
    rand_pos = random.choice(rand_indexes)
    rand_indexes.remove(rand_indexes)
    cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})

    print(cells[i])

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Black")

    for i, val in enumerate(cells):
        pos = cells[i]['pos']
        img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
        screen.blit(bg, cells[i]['rect'], img_area)

    screen.blit(bg, bg_rect, (400, 300, 100, 100))


    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
