import pygame
import sys
from sounds import *
from sounds import click_SE
from pygame.locals import *
from death import deathscreen
from game import *
from options import options
pygame.init()

pygame.display.set_caption("Mahmoud")
icon = pygame.image.load('mamood.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 500))



def menu():
    menuloop = True
    while menuloop:
        screen.fill((189, 87, 87))
        mx, my = pygame.mouse.get_pos()
        play_btn = pygame.Rect(200, 50, 400, 150)
        option_btn = pygame.Rect(200, 250, 400, 150)
        pygame.draw.rect(screen, (87, 189, 189), play_btn)
        pygame.draw.rect(screen, (87, 189, 189), option_btn)


        # Text
        font = pygame.font.SysFont(None, 100)
        font2 = pygame.font.SysFont(None, 50)
        start = font.render('START', True, ((255,255,255)))
        option_txt = font.render('OPTIONS', True, ((255,255,255)))
        creds = font2.render('Made by Alim', True, ((255,255,255)))
        screen.blit(start, (290, 100))
        screen.blit(option_txt, (235, 300))
        screen.blit(creds, (300, 450))

        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pass
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if play_btn.collidepoint(mx, my):
            if click:
                sounds.click_SE()
                game()
                deathscreen()

        if option_btn.collidepoint(mx, my):
            if click:
                sounds.click_SE()
                options()
        pygame.display.update()
menu()

