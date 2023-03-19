import pygame
import os
import random
import time
pygame.font.init()


WIDTH = 1550
HEIGHT = 820
BLACK = (0,0,0)
WHITE = (255,255,255)
X,Y = 40,50
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join('tai nguyen','monster.png')),(X+50,Y+40))
FPS = 60
ENEMY_IMG = pygame.transform.scale(pygame.image.load(os.path.join('tai nguyen','monster 2.png')),(X,Y))
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('dong anh dzai 102')
class Enemy:
    def __init__(self,x,y,health = 100) :
        self.enemy_img = ENEMY_IMG
        self.x = x
        self.y = y
        self.health = health
        self.mask = pygame.mask.from_surface(self.enemy_img) 
    def move(self,vel):
        self.x -= vel
    def draw(self,window):
        window.blit(self.enemy_img,(self.x,self.y))
    def get_width(self):
        return self.enemy_img.get_width()
    def collision(self, obj):
        return collide(self, obj)
class Player:
    def __init__(self,x,y,health = 100):
        self.player_img = PLAYER
        self.x = x
        self.y = y
        self.health = health
        self.mask = pygame.mask.from_surface(self.player_img)
    def draw(self,window):
        window.blit(self.player_img,(self.x,self.y))
    def collision(self,obj):
        return collide(self,obj)
# class Enemyright :
#     def __init__(self,x,y,health = 100) :
#         self.enemy_img = ENEMY_IMG
#         self.x = x
#         self.y = y 
#         self.health = health
#         self.mask = pygame.mask.from_surface(self.enemy_img)
#     def move(self, vel) :
#         self.x -= vel 
#     def draw(self,window) :
#         window.blit(self.enemy_img,(self.x,self.y))
#     def get_width(self):
#         return self.enemy_img.get_width()
def collide(obj1,obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y 
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None    
def main():
    enemies = [] 
    lost = False
    lives = 1
    player = Player(750,700)
    def draw_window() :
        WIN.fill(WHITE)
        player.draw(WIN)
       
        for enemFromRight in enemies :
            enemFromRight.draw(WIN)
        # for enemFromLeft in enemies :
        #     enemFromLeft.draw(WIN)

        pygame.display.update()
        if lost == True:
            lost_label = lost_font.render("MÀY NGU", 1, (0,0,0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 200))
            pygame.display.update()


    wave_length = 5
    enemy_vel = 1
    enemy_vel = float(enemy_vel)
    clock = pygame.time.Clock()
    run = True
    while run :
        lost_count = 0
        lost_font = pygame.font.SysFont("comicsans",200)
        clock.tick(FPS)
        if  len(enemies) == 0 :
            enemy_vel += 0.5
            wave_length += 5
            # for i in range(wave_length):
            #     enemFromLeft = Enemy(random.randrange(-4000,0),random.randrange(400,800))
            #     enemies.append(enemFromLeft)

            for i in range(wave_length):
                enemFromRight = Enemy(random.randrange(1550,3000),random.randrange(500,800))   
                enemies.append(enemFromRight)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False


        for enemFromRight in enemies[:]:
            enemFromRight.move(enemy_vel)
            if enemFromRight.x + enemFromRight.get_width() < 50:
                enemies.remove(enemFromRight)
            if collide(enemFromRight,player):
                enemies.remove(enemFromRight)
                lives = lives - 1
        if lives == 0:
            lost = True
            lost_count += 1
        if lost:
            lost_label = lost_font.render("MÀY NGU", 1, (0,0,0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 200))
            pygame.display.update()
            if lost_count > FPS*3:
                run = false
            else:
                continue
        # for enemFromLeft in enemies[:]:
        #     enemFromLeft.move(enemy_vel)
        #     if enemFromLeft.x + enemFromLeft.get_width() > 1450:
        #         enemies.remove(enemFromLeft)

        draw_window()
    pygame.quit()

if __name__ == '__main__':
    main()