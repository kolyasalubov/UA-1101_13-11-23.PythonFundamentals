import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Number expert")  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

number =  random.randint(0,100)
i = 0

font = pygame.font.SysFont('Calibri', 15, True, False)
input_text = ""
response_text = ""
text = font.render("Guess the number:",True,BLACK)
done = True
while done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if   int(input_text) == number and i!=10 :
                    response_text = "Congradulations you entered the sicret number: " + input_text
                    i = 10
                elif int(input_text) > number and i!=10:
                    response_text = "The secret number is less then" + input_text
                    i+=1
                elif int(input_text) < number and i!=10:
                    response_text = "The secret number is higher then" + input_text
                    i+=1
                else:
                    response_text = "Sorry there is no tries anymore"
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
        screen.fill(WHITE)
        text_surface = font.render(input_text,True,BLACK)
        response_surface = font.render(response_text,True,(0,0,0))
        screen.blit(response_surface,[10,50])
        screen.blit(text_surface, [150, 30])
        screen.blit(text,[10,30])
        pygame.display.flip()