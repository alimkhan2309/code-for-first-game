import pygame
import sys
import sounds
from game import scoreDisplay
from game import game

pygame.init()
screen = pygame.display.set_mode((800, 500))
# score_value = score_value
# scr = str(score_value)

def deathscreen():
    deathloop = True
    while deathloop:
        screen.fill((189, 87, 87))

        mx, my = pygame.mouse.get_pos()
        playagain_btn = pygame.Rect(200, 50, 400, 150)
        backtomenu_btn = pygame.Rect(200, 250, 400, 150)
        pygame.draw.rect(screen, (87, 189, 189), playagain_btn)
        pygame.draw.rect(screen, (87, 189, 189), backtomenu_btn)


        # Text
        font = pygame.font.SysFont(None, 100)
        again = font.render('AGAIN', True, ((255, 255, 255)))
        b2menu = font.render('MENU', True, ((255, 255, 255)))
        screen.blit(again, (290, 100))
        screen.blit(b2menu, (300, 300))

        scoreDisplay()
    
        click = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                deathloop = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click = True

        if playagain_btn.collidepoint(mx, my):
            if click:
                sounds.click_SE()
                game()
        if backtomenu_btn.collidepoint(mx, my):
            if click:
                sounds.click_SE()
                deathloop = False
        pygame.display.update()
