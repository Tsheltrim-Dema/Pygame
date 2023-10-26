import pygame

#initial
#  the pygame 
pygame.init()

#setup the window 
window_width = 800
window_height = 600
window ==
pygame.display.set.mode((window_width,window_height))
pygame.display.set_caption("Puzzul Game")

#Game loop
running = True
while running:
    #event handling 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # update game logic
   #Render game graphics 
   window.fill((255, 255, 255))
   #Draw puzzul pices, backgroud, etc

   #update the display
   pygame.display.flip()

# Quit the game 
pygame.quit()



     
