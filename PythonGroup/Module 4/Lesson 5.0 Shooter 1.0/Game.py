print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path

WIDTH = 480
HEIGHT = 600
FPS = 15

# colors set up
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELOW = (255, 255, 0)


# Window creating
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_function("Shooter")
clock = pygame.time.Clock()

img_dir = path.join(path.dirname(__file__), "img")

# Game sprites 
backround = pygame.image.load(path.join(img_dir, "field.png")).convert()
backround_rect = backround.get_rect()
player_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
npc_img = pygame.image.load(path.join(img_dir, "npc.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png")).convert()

#player class
 class Player(pygame.sprite.Sprite):
     score = 0

     def __init__(self):
         pygame.sprite.Sprite__init__(self)
         self.image = pygame.transform.scale(player_img, (50, 50))
         self.image.set_colorkey(WHITE)
         self.image.


















 # mob class












#bullet class




#Game entities innit









# Game Lyfecycle




    # rendering


 

    #win lose  situation 
    



 
    #text 
     

 