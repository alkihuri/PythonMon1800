# Подключить нужные модули
from random import randint 
import pygame 
from os import path
pygame.init() 
# во время игры пишем надписи размера 72
 

# Глобальные переменные (настройки)


# цвета: 


# Классы
class FinalSprite(pygame.sprite.Sprite):
 # constructor 
 def __init__(self, player_image, player_x, player_y, player_speed):
     # Call  the class constructor (Sprite):
     pygame.sprite.Sprite.__init__(self)

     # each sprite must store an image property - an image
     self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
     self.speed = player_speed

     # each sprite must store the property rect - the rectangle in which it is inscribed
     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y



class Hero(pygame.sprite.Sprite):
   def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
       pygame.sprite.Sprite.__init__(self)
       # the picture is loaded from a file and includes proteins of the required sizes:
       self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
                   # use convert_alpha, we need to keep transparency
       # each sprite must store a rect property - a rectangle. This property is needed to determine the touches of sprites.
       self.rect = self.image.get_rect()
       # put the character at the given point (x, y):
       self.rect.x = x
       self.rect.y = y
       # create properties, remember the passed values:
       self.x_speed = x_speed
       self.y_speed = y_speed
       # add the stands_on property - this is the platform on which the character stands
       self.stands_on = False # if none, then the value is False

    def gravitate(self):
       self.y_speed += 0.25

    def jump(self, y):
       if self.stands_on:
           self.y_speed = y

    def update(self):
        self.rect.x += self.x_speed
        # # if we went behind the wall, then we will stand close to the wall
       platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
       if self.x_speed > 0: # we go to the right, the right edge of the character is close to the left edge of the wall
           for p in platforms_touched:
               self.rect.right = min(self.rect.right, p.rect.left) # if they touched several at once, then the right edge is the minimum possible
       elif self.x_speed < 0: # go left, put the left edge of the character close to the right edge of the wall
           for p in platforms_touched:
               self.rect.left = max(self.rect.left, p.rect.right) # if several walls are touched, then the left edge is the maximum
       # now moving vertically      
       self.gravitate()
       self.rect.y += self.y_speed
       # if we went behind the wall, then we will stand close to the wall
       platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
       if self.y_speed > 0: # go down
           for p in platforms_touched:
               self.y_speed = 0
               # We check which of the platforms below is the highest, align with it, remember it as our support:
               if p.rect.top < self.rect.bottom:
                   self.rect.bottom = p.rect.top
                   self.stands_on = p
       elif self.y_speed < 0: # go up
           self.stands_on = False #  so we're not standing on anything!
           for p in platforms_touched:
               self.y_speed = 0  # when colliding with a wall, the vertical speed is extinguished
               self.rect.top = max(self.rect.top, p.rect.bottom) # align the top edge with the bottom edges of the walls that were run over


    #функция для прыжка

    #функция апдейт для данного спрайта. так как спрайт будет премещаться. Самая веселая часть ) 
     

#класс для стены. Делали точно такой же в проекте Лабиринт :))) 
    #конструктор

class Enemy(pygame.sprite.Sprite): # enemy
   def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

   def update(self):
       ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
       self.rect.x += randint(-5, 5)
       self.rect.y += randint(-5, 5)



# Запуск игры 


# список всех персонажей игры:


# список препятствий:

# список врагов:

# список мин:


# создаем персонажа, добавляем его в список всех спрайтов:

# создаем стены, добавляем их:




# создаем врагов, добавляем их:


# создаем мины, добавляем их:
            
            # в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой
            # так легко сможем подрывать бомбы, а также делаем их неподвижными, update() не вызывается

# создаем финальный спрайт, добавляем его: 

# Основной цикл игры: 
 
    # Обработка событий
      
        # Перемещение игровых объектов  

        # дальше проверки правил игры
        # проверяем касание с бомбами: 
                # если бомба коснулась спрайта, то она убирается из списка бомб, а спрайт - из all_sprites!

        # проверяем касание героя с врагами: 
           # robin.kill() # метод kill убирает спрайт из всех групп, в которых он числится

        # проверяем границы экрана: 
             # при выходе влево или вправо переносим изменение в сдвиг экрана 
            # перемещаем на общий сдвиг все спрайты (и отдельно бомбы, они ж в другом списке): 
                        # сам robin тоже в этом списке, поэтому его перемещение визуально отменится
            

        # Отрисовка
        # рисуем фон со сдвигом
        

        # нарисуем все спрайты на экранной поверхности до проверки на выигрыш/проигрыш
        # если в этой итерации цикла игра закончилась, то новый фон отрисуется поверх персонажей
         
        # группу бомб рисуем отдельно - так бомба, которая ушла из своей группы, автоматически перестанет быть видимой
       

        # проверка на выигрыш и на проигрыш:
        

        # проверка на проигрыш:
         
            # пишем текст на экране
             

     

    # Пауза 