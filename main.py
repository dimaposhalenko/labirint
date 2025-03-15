

import time

from pygame import*

window = display.set_mode((900, 700))
display.set_caption('Labyrinth')
display.set_icon(image.load('Bitcoin.png'))

background = transform.scale(image.load('Tropical-jungle.jpg'), (900, 700))
clock = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))






 




class GameSprite1(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (60, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))







class GameSprite2(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (50, 45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))











class Player(GameSprite1):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 850:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 630:
            self.rect.y += self.speed




class Player1(GameSprite1):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 850:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed





class Enemy(GameSprite):
    position = 'right'

    def update_l_r(self, start , end):
        
        if self.rect.x <= start: 
            self.position = "right"
        if self.rect.x >= end:
            self.position = "left"
            
        if self.position == "right":
            self.rect.x += self.speed
        elif self.position == "left":
            self.rect.x -= self.speed
        





class Enemy1(GameSprite):
    position = 'right'

    def update_l_r(self, start , end):
        
        if self.rect.x <= start: 
            self.position = "right"
        if self.rect.x >= end:
            self.position = "left"
            
        if self.position == "right":
            self.rect.x += self.speed
        elif self.position == "left":
            self.rect.x -= self.speed

        

class Enemy2(GameSprite2):
    position = 'up'

    def update_l_r(self, start , end):
        
        if self.rect.y <= start: 
            self.position = "up"
        if self.rect.y >= end:
            self.position = "down"
            
        if self.position == "up":
            self.rect.y += self.speed
        elif self.position == "down":
            self.rect.y -= self.speed









class Enemy3(GameSprite):
    position = 'up'

    def update_l_r(self, start , end):
        
        if self.rect.y <= start: 
            self.position = "up"
        if self.rect.y >= end:
            self.position = "down"
            
        if self.position == "up":
            self.rect.y += self.speed
        elif self.position == "down":
            self.rect.y -= self.speed











class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

denga = GameSprite('png-transparent-two-100-g-fine-gold-bars-california-gold-rush-gold-as-an-investment-gold-bar-gold-investment-bullion-gold-thumbnail-removebg-preview.png', 700, 50, 0)
player = Player('images__1_-removebg-preview.png', 100, 600, 5)  
player1 = Player1('смаил_фейс_-removebg-preview.png', 100, 600, 5)  
enemy = Enemy('Без_названия-removebg-preview.png', 800, 250, 1)
enemy1 = Enemy1('Pastel_Pink-removebg-preview.png', 400, 320, 5)
enemy2 = Enemy2('Paastel_Pink-removebg-preview.png', 600, 610, 2)
enemy3 = Enemy3('Без_названия--removebg-preview.png', 770, 50, 2)
gold = GameSprite('Bitcoin.png', 700, 170, 0)

wall1 = Wall(200, 247, 121, 20, 20, 850, 20)
wall2 = Wall(200, 247, 121, 20, 20, 20, 700)
wall3 = Wall(200, 247, 121, 850, 20, 20, 700)
wall4 = Wall(200, 76, 5, 170, 120, 20, 450)
wall5 = Wall(200, 76, 5, 270, 120, 20, 290)
wall6 = Wall(250, 218, 122, 270, 400, 20, 100)
wall7 = Wall(200, 76, 5, 370, 120, 20, 380)
wall8 = Wall(169, 196, 108, 370, 40, 20, 80)
wall9 = Wall(169, 196, 108, 170, 570, 20, 110)
wall10 = Wall(200, 76, 5, 370, 120, 480, 20)
wall12 = Wall(180, 235, 230, 270, 40, 20, 80)
wall13 = Wall(200, 247, 121, 170, 680, 700, 20)
wall14 = Wall(200, 76, 5, 170, 500, 600, 20)
wall15 = Wall(200, 76, 5, 600, 120, 20, 120)
wall16 = Wall(200, 76, 5, 300, 600, 20, 80)
wall17 = Wall(200, 76, 5, 400, 500, 20, 80)
wall18 = Wall(180, 235, 230, 500, 600, 20, 80)
wall19 = Wall(250, 218, 122, 500, 520, 20, 80)
wall20 = Wall(200, 76, 5, 570, 400, 280, 20)


mixer.init()
mixer.music.load('4b243785232586e.ogg')
mixer.music.play()
mixer.music.get_volume()

kick = mixer.Sound('fail.ogg')
money = mixer.Sound('b7caf2273d4a620.ogg')

game = True
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))
    player.reset()
    player1.reset()
    enemy.reset()
    enemy1.reset()
    enemy2.reset()
    enemy3.reset()
    gold.reset()
    denga.reset()
    player.update()
    player1.update()
    enemy.update_l_r(600, 750)
    enemy1.update_l_r(400, 550)
    enemy2.update_l_r(515, 630)



    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()

    wall10.draw_wall()
    wall12.draw_wall()
    wall13.draw_wall()
    wall14.draw_wall() 
    wall15.draw_wall()
    wall15.draw_wall()
    wall16.draw_wall()
    wall17.draw_wall()
    wall18.draw_wall()
    wall19.draw_wall()
    wall20.draw_wall()


    if sprite.collide_rect(player, wall1) or \
        sprite.collide_rect(player, wall2) or \
        sprite.collide_rect(player, wall13) or \
        sprite.collide_rect(player, wall20) or \
        sprite.collide_rect(player, wall16) or \
        sprite.collide_rect(player, wall3) or \
        sprite.collide_rect(player, wall18) or \
        sprite.collide_rect(player, wall17) or \
        sprite.collide_rect(player, wall4) or \
        sprite.collide_rect(player, wall5) or \
        sprite.collide_rect(player, wall7) or \
        sprite.collide_rect(player, wall15) or \
        sprite.collide_rect(player, wall14) or \
        sprite.collide_rect(player, wall10) or \
        sprite.collide_rect(player, wall12) or \
        sprite.collide_rect(player1, wall2) or \
        sprite.collide_rect(player1, wall3) or \
        sprite.collide_rect(player1, wall4) or \
        sprite.collide_rect(player1, wall5) or \
        sprite.collide_rect(player1, wall7) or \
        sprite.collide_rect(player1, wall15) or \
        sprite.collide_rect(player1, wall10) or \
        sprite.collide_rect(player1, wall1) or \
        sprite.collide_rect(player1, wall6) or \
        sprite.collide_rect(player1, wall14) or \
        sprite.collide_rect(player1, wall13) or \
        sprite.collide_rect(player1, wall16) or \
        sprite.collide_rect(player1, wall17) or \
        sprite.collide_rect(player1, wall19) or \
        sprite.collide_rect(player1, wall20) or \
        sprite.collide_rect(player, enemy) or \
        sprite.collide_rect(player1, enemy) or \
        sprite.collide_rect(player, enemy1) or \
        sprite.collide_rect(player1, enemy2) or \
        sprite.collide_rect(player, enemy2) or \
        sprite.collide_rect(player1, enemy1):
        kick.play()
        player.rect.x = 100
        player.rect.y = 600
        player1.rect.x = 100
        player1.rect.y = 600
    if sprite.collide_rect(player, gold):
        time.delay(1000)
        money.play()
        game = False
    
    display.update()
    clock.tick(fps)
