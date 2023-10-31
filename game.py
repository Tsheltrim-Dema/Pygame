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

bg = pygame.image.load('elephant.jpg') 
bg_rect = bg.get.rect()
bg_rect.topleft = (0, 0)

font_title = pygame.font.font('Hello Avocado.ttf', 64)
font_content = pyame.font.font('Hello Avocado.ttf', 40)

play_again_text = font_title.render('play Again?', True, WHITE)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (window_height // 2, window_width // 2 )

continue_text = font_content.render('press space', True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (window_width // 2, window_height // 2 + 50)

img_selected = None
is_game_over = false

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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = false 
        if event_type == pygame.MOUSEBUTTONDOWN and event_button == 1 and not is_game_over:
            mouse_pos = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell['rect']
                order = cell['order']
                if rect.collidepoint(mouse_pos):
                    if not img_selected:
                        img_selected:
                        cell['border'] = RED
                    else:
                        current_img = cell
                        if current_img['order'] != selected_img['order']:
                            #swap the image
                            temp = selected_img['pos']
                            cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['border'] = temp

                            cells[selected_img['order']]['border'] = WHITE
                            selected_img = None

                            #check if the puzzul is sloved
                            is_game_over = True
                            for cell in cells:
                                if cell['order'] !=cell['pos']:
                                    is_game_over = False
                                    
                              


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Black")
if not is_game_over:
    for i, val in enumerate(cells):
        pos = cells[i]['pos']
        img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
        screen.blit(bg, cells[i]['rect'], img_area)
        pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
else:
    screen.blit(bg, bg_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(continue_text, continue_rect)

    screen.blit(bg, bg_rect, (400, 300, 100, 100))


    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
