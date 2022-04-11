print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path

WIDTH=480
HEIGHT=600
FPS=15






# colors set up








# Window creating
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_caption((WIDTH,HEIGHT))
pygame.display.set_caption("Shooter")
clock=pygame.time.Clock()



img_dir=path.join(path.dirname(__file__), 'img') 
# Game sprites 
background=pygame.image.load(path.join(img_dir, "field.png")).convert()
background_rect=background.get_rect()
player_img=pygame.image.load(path.join(img_dir, "ship.png")).convert()
npc_img=pygame.image.load(path.join(img_dir, "npc.png")).convert()
bullet_img=pygame.image.load(path.join(img_dir,"bullet.png")).convert()





#player class
class Player(pygame.sprite.Sprite):
    score=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,50))
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centrex=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speedx=0

    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-8
        if keystate[pygame.K_RIGHT]:
            self.speedx=8
        self.rect.x+=self.speedx
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0


















 # mob class












#bullet class




#Game entities innit









# Game Lyfecycle




    # rendering


 

    #win lose  situation 
    



 
    #text 
     

 