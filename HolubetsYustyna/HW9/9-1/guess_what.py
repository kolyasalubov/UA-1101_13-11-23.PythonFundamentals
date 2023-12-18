import pygame
import random
from colors_icons import *

WIDTH_DISPLAY = 650
HEIGHT_DISPLAY = 500
FPC = 60

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption('GUESS WHAT')
pygame.display.set_icon(ICON)

done = False
clock = pygame.time.Clock()

font = pygame.font.Font('C:\\WINDOWS\\Fonts\\ROCC____.TTF', 40)
text = font.render('Guess a number from the range of 1 to 100', True, CORN_SILK_COL )
gameDisplay.blit(text, [45, 30])

font_2 = pygame.font.Font('C:\\WINDOWS\\Fonts\\ROCC____.TTF', 20)
help_center = font_2.render('Click on the red circle and enter your number.  Then press check and try again.', True, CORN_SILK_COL)

inp_default_col = pygame.Color(FIREBRICK_COL)
inp_active_col = pygame.Color(BLACK_COL)
inp_col = inp_default_col

active = False
check = False
win = False
lost = False
user_inp = ''

try_count = 0

rand_numb = random.randint(1, 100)

while not done:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if help_btn.collidepoint(event.pos):
                gameDisplay.blit(help_center, (55, 80))
            else:
                pygame.draw.rect(gameDisplay, BLACK_COL, (50, 80, 650, 90))
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_inp.collidepoint(event.pos):
                active = True
                user_inp = ''
            else:
                active = False
    
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                user_inp = user_inp[:-1]
            else:
                user_inp += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and user_inp:
            if check_btn.collidepoint(event.pos):
                check = True

        if (win or lost) and event.type == pygame.MOUSEBUTTONDOWN:
            if restart_btn.collidepoint(event.pos):
                pygame.draw.rect(gameDisplay, BLACK_COL, (250, 400, 300, 450))
                pygame.draw.rect(gameDisplay, BLACK_COL, (200, 280, 300, 380))
                pygame.draw.circle(gameDisplay, BLACK_COL, [580, 450], 20)

                win = False
                lost = False
                check = False
                rand_numb = random.randint(1, 100)
                try_count = 0
                col_list = [BLACK_COL, FIREBRICK_COL, INDINA_RED_COL, LIGHT_CORAL_COL, LIGHT_SALMON_COL,\
                            KHAKI_COL, GOLD_COL, GOLDEN_ROD_COL, OLIVE_COL, DARK_OLIVE_GREEN_COL,\
                            DARK_SLATE_GREY_COL]

    if active:
        if try_count != 9:
            inp_col = inp_active_col 
        else:
            inp_col = BLACK_GREY
    else:
        inp_col = inp_default_col

    circle10 = pygame.draw.circle(gameDisplay, col_list[10], [325, 270], 130)
    circle9 = pygame.draw.circle(gameDisplay, col_list[9], [325, 270], 120)
    circle8 = pygame.draw.circle(gameDisplay, col_list[8], [325, 270], 110)
    circle7 = pygame.draw.circle(gameDisplay, col_list[7], [325, 270], 100)
    circle6 = pygame.draw.circle(gameDisplay, col_list[6], [325, 270], 90)
    circle5 = pygame.draw.circle(gameDisplay, col_list[5], [325, 270], 80)
    circle4 = pygame.draw.circle(gameDisplay, col_list[4], [325, 270], 70)
    circle3 = pygame.draw.circle(gameDisplay, col_list[3], [325, 270], 60)
    circle2 = pygame.draw.circle(gameDisplay, col_list[2], [325, 270], 50)
    circle_inp = pygame.draw.circle(gameDisplay, inp_col, [325, 270], 40)

    help_btn = pygame.draw.circle(gameDisplay, CORN_SILK_COL, [580, 350], 20)
    gameDisplay.blit(HELP, (545, 315))

    user_guess = font.render(user_inp, True, CORN_SILK_COL)
    gameDisplay.blit(user_guess, (circle_inp.x+30, circle_inp.y+15))

    if user_inp:
        check_btn = pygame.draw.rect(gameDisplay, BLACK_COL, (250, 400, 300, 450))
        text_check_btn = font.render('check', True, CORN_SILK_COL )
        gameDisplay.blit(text_check_btn, [290, 430])

    if check:
        pygame.draw.rect(gameDisplay, BLACK_COL, (250, 400, 300, 450))
        print(rand_numb)
        if int(user_inp) == rand_numb:
            win = True
            text_success = font.render('Genius!', True, CORN_SILK_COL )
            gameDisplay.blit(text_success, [280, 430])
        else:
            try_count += 1
            col_list[-try_count] = BLACK_COL
            if int(user_inp) > rand_numb:
                text_hint = font.render('aim lower', True, CORN_SILK_COL)
            else:
                text_hint = font.render('aim higher', True, CORN_SILK_COL)
            gameDisplay.blit(text_hint, [260, 430])
            if try_count == 10:
                lost = True
        check = False
        user_inp = ''
    
    if win:
        pygame.draw.circle(gameDisplay, BLACK_COL, [325, 270], 40)
        gameDisplay.blit(TROPHY, (290, 240))
        
    if lost:
        pygame.draw.circle(gameDisplay, BLACK_COL, [325, 270], 40)
        gameDisplay.blit(FAIL, (270, 230))
        text_fail = font.render('Unfortunately...', True, CORN_SILK_COL )
        gameDisplay.blit(text_fail, [240, 340])

    if win or lost:
        pygame.draw.rect(gameDisplay, BLACK_COL, (250, 400, 300, 450))
        restart_btn = pygame.draw.circle(gameDisplay, CORN_SILK_COL, [580, 450], 20)
        gameDisplay.blit(AGAIN, (565, 435))


    pygame.display.update()
    clock.tick(FPC)

