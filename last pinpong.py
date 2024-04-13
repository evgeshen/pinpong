from pygame import *
from random import randint
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image).convert_alpha(), (w, h))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


    
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("")

background = transform.scale(image.load("fon.jpg"), (win_width, win_height))

player1 = GameSprite('tenisrocket.png', win_width/2 - 30, win_height - 80, 15, 60, 60)

clock = time.Clock()
FPS = 60
ticks = 0

player1.update() 

player1.draw()

ticks += 1
display.update()
clock.tick(FPS)