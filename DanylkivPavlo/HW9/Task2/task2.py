import pygame
pygame.init()

RED = (255,0,0)
BLACK = (0,0,0)
CORD_X = 50
CORD_Y = 50
MOVE = 7
WIDTH = 100
HEIGHT = 80
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600


pygameDisp = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("HI,it's my first game! ")
run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and CORD_Y > MOVE:
        CORD_Y = CORD_Y - MOVE
    if keys[pygame.K_DOWN] and CORD_Y < SCREEN_HEIGHT - HEIGHT - MOVE:
        CORD_Y += MOVE
    if keys[pygame.K_LEFT] and CORD_X > MOVE:
        CORD_X = CORD_X - MOVE
    if keys[pygame.K_RIGHT] and CORD_X < SCREEN_WIDTH - WIDTH - MOVE:
        CORD_X = CORD_X + MOVE

    pygameDisp.fill((0, 0, 0))
    pygame.draw.rect(pygameDisp,(255,0,0), [CORD_X,CORD_Y,WIDTH,HEIGHT])

    #pygame.draw.rect(pygameDisp, (255,0,0), [55,50,80,55])
    pygame.display.update()
    clock.tick(30)