from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
 
 
font2 = font.Font(None, 36)
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
 
class Player(GameSprite):
    def update_r(self):  
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

 
 

back = (200, 255, 255) 
win_width = 600
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))



finish = False
run = True #флаг сбрасывается кнопкой закрытия окна
rocket1 = Player("rocket.png", 30, 200, 40, 50, 15)
rocket2 = Player("rocket.png", 520, 200, 40, 50, 15)
ball = GameSprite("ball.png", 200, 200, 60, 150, 15)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (100, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (100, 0, 0))


speed_x = 3
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
         

    if not finish:
        window.fill(back)
        rocket1.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        rocket1.reset()
        rocket2.reset()
        ball.reset()
        time.delay(50)
        
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
    
        display.update()




    
