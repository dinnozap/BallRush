#--------------------------IMPORT---------------------------#

import pygame, time
from random import randrange
from pygame.locals import *
from ressources import *
print("Initialisation de PyGame ...")
pygame.init()
print("Initialisation finie !")

#-----------------------------------------------------------#

















#-----------------------GRAPHIC-----------------------------#
point = 0
ennemyax_X = 0
ennemyax_Y = 10

fenetre = pygame.display.set_mode((568, 568))
image_fond = pygame.image.load("jumpgames/images/fond").convert()
fenetre.blit(image_fond, (0, 0))        

ball = pygame.image.load(ball_haut).convert_alpha()
persoax_X = 0
persoax_Y = 0
fenetre.blit(ball, (persoax_X, persoax_Y))
coord_ball = ball.get_rect()

ennemy = pygame.image.load("ennemy.png").convert_alpha()
persoax_X = 0
persoax_Y = 0
fenetre.blit(ennemy, (ennemyax_X, ennemyax_Y))
coord_ennemy = ennemy.get_rect()

nourriture = pygame.image.load("nourriture.png").convert_alpha()
nourriture_x = randrange(45,565)
nourriture_y = randrange(45, 565)
coord_nourriture = ball.get_rect()
fenetre.blit(nourriture, (nourriture_x, nourriture_y))
pygame.display.flip()




#-----------------------------------------------------------#
#----------------------INTERACTION/FONCTION-----------------#

pygame.key.set_repeat(40, 1)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                 persoax_Y = persoax_Y + 1
                 ball = pygame.image.load(ball_bas).convert_alpha()
            if event.key == K_RIGHT or event.key == K_d:
                persoax_X = persoax_X + 1
                ball = pygame.image.load(ball_droit).convert_alpha()
            if event.key == K_UP or event.key == K_z:
                persoax_Y = persoax_Y - 1
                ball = pygame.image.load(ball_haut).convert_alpha()
            if event.key == K_LEFT or event.key == K_q:
                persoax_X = persoax_X - 1
                ball = pygame.image.load(ball_gauche).convert_alpha()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                fireax_X = event.pos[0]
                fireax_Y = event.pos[1]
        ennemyax_X = ennemyax_X + 1
        ennemyax_Y = ennemyax_Y + 1







        if persoax_X < 0:
    		persoax_X = 549
    	elif persoax_X > 550:
    		persoax_X = 4
    	elif persoax_Y < 0:
    		persoax_Y = 549
    	elif persoax_Y > 550:
    		persoax_Y = 4
        if  persoax_X < nourriture_x  + 30 and persoax_X > nourriture_x - 30 and persoax_Y < nourriture_y + 30 and persoax_Y > nourriture_y - 30:
            nourriture_x = randrange(45,565)
            nourriture_y = randrange(45, 565)
            point = point + 1
            
            print point
            
     
  	fenetre.blit(image_fond, (0,0))          
    fenetre.blit(ball,(persoax_X, persoax_Y))  
    fenetre.blit(ennemy,(ennemyax_X, ennemyax_Y))  
    fenetre.blit(nourriture, (nourriture_x, nourriture_y))
    pygame.display.flip()
