import pygame
import sys
import sounds
from pygame.locals import *
from math import sqrt
# from death import deathscreen
import random
pygame.init()

screen = pygame.display.set_mode((800, 500))



def scoreDisplay():
    font2 = pygame.font.SysFont(None, 65)
    score_txt = font2.render(f'Score: {score_value}', True, ((255, 255, 255)))
    screen.blit(score_txt, (300, 420))

def game():
    # User
    x = 400
    y = 250
    width = 50
    height = 50
    vel = 5
    mahmoud = pygame.image.load('mamood.png')

    # Enemy
    enemyImg = pygame.image.load('enemy.png')
    enemyX = random.randint(0, 800)
    enemyY = random.randint(0, 500)
    enemySpeed = 2

    # Food
    foodImg = pygame.image.load('burg.png')
    foodX = random.randint(0, 750)
    foodY = random.randint(0, 450)
    global score_value
    score_value = 0

    # mouse
    clicking = False

    def player():
        #pBox = (x-32, y-32, 64, 64)
        #pygame.draw.rect(screen,(255,255,255),pBox)
        screen.blit(mahmoud, (x-32, y-32))

    def enemy():
        #eBox = (enemyX-25, enemyY-32, 50, 64)
        #pygame.draw.rect(screen,(255,0,255),eBox)
        screen.blit(enemyImg, (enemyX-25, enemyY-32))

    def food():
        #fBox = (foodX-16, foodY-16, 32, 32)
        #pygame.draw.rect(screen,(0,255,0),fBox)
        screen.blit(foodImg, (foodX-16, foodY-16))

    def score():
        font = pygame.font.SysFont(None, 50)
        score_display = font.render(f'Score: {str(score_value)}' , True, ((0,0,0)))
        screen.blit(score_display, (50, 50))
        

    mainloop = True
    while mainloop:
        screen.fill((189, 87, 87))
        pygame.time.delay(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pass
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x-vel > 32:
            x -= vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x+vel < 800 - 32:
            x += vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and y-vel > 32:
            y -= vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y+vel < 500 - 32:
            y += vel

        # enemy movement
        normal = sqrt((enemyX - x)*(enemyX - x) + (enemyY - y)*(enemyY - y))
        
        enemyX -= ((enemyX - x) / normal) * enemySpeed
        enemyY -= ((enemyY - y) / normal) * enemySpeed

        # food eating
        if abs(x - foodX) < 48 and abs(y - foodY) < 48:
            sounds.consume_SE()
            score_value += 1
            foodX = random.randint(0, 750)
            foodY = random.randint(0, 450)

            #enemySpeed *= 1.1
            #vel *= 1.12

            enemySpeed += 0.5
            vel += 0.5

        # enemy eating
        dis = 20
        if abs(x - enemyX) < 57 - dis and abs(y - enemyY) < 64 - dis:
            sounds.kill_SE()
            sounds.died_SE()
            mainloop = False
        
        # Entity
        food()
        player()
        enemy()
        score()
        pygame.display.update()
    return score_value
