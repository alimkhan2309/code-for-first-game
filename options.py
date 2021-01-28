import pygame
from game import *
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 500))
sounds.click_SE()

def options():
    loop = True
    sounds.opt_background(loop)
    while loop:
        screen.fill((112, 48, 48))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                sounds.click_SE()
                loop = False
                sounds.opt_background(loop)
        # shadow1
        s = pygame.Surface((400, 250))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill((0, 0, 0))           # this fills the entire surface
        screen.blit(s, (80, 120))    # (0,0) are the top-left coordinates

        # box1
        rect = pygame.Rect((100, 100, 400, 250))
        mx, my = pygame.mouse.get_pos()
        if rect.collidepoint(mx,my):
            rect = pygame.Rect((80,120,400,250))
        pygame.draw.rect(screen, (87, 189, 189), rect)

        # shadow2
        s2 = pygame.Surface((150, 150))  # the size of your rect
        s2.set_alpha(128)                # alpha level
        s2.fill((0, 0, 0))           # this fills the entire surface
        screen.blit(s2, (530, 120))    # (0,0) are the top-left coordinates

        # box2
        rect2 = pygame.Rect((550, 100, 150, 150))
        mx, my = pygame.mouse.get_pos()
        if rect2.collidepoint(mx, my):
            rect2 = pygame.Rect((530, 120, 150, 150))
        pygame.draw.rect(screen, (87, 138, 189), rect2)

        # shadow3
        s3 = pygame.Surface((150, 50))  # the size of your rect
        s3.set_alpha(128)                # alpha level
        s3.fill((0, 0, 0))           # this fills the entire surface
        screen.blit(s3, (530, 320))    # (0,0) are the top-left coordinates

        # box3
        rect3 = pygame.Rect((550, 300, 150, 50))
        mx, my = pygame.mouse.get_pos()
        if rect3.collidepoint(mx, my):
            rect3 = pygame.Rect((530, 320, 150, 50))
        pygame.draw.rect(screen, (87, 189, 138), rect3)




        # Text Shadow
        shd = 3
        grey = (40, 40, 40)
        font = pygame.font.SysFont(None, 60)
        font2 = pygame.font.SysFont(None, 40)
        messege_sh = font.render('Shit was too complicated fuck off', True, (grey))
        messege2_sh = font2.render('Press ESC to go back', True, (grey))
        screen.blit(messege_sh, (70 - shd, 400 + shd))
        screen.blit(messege2_sh, (260 - shd, 450 + shd))

        # text
        messege = font.render('Shit was too complicated fuck off', True, (255,255,255))
        messege2 = font2.render('Press ESC to go back', True, (255,255,255))
        screen.blit(messege, (70, 400))
        screen.blit(messege2, (260, 450))

        pygame.display.update()
            
