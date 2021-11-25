import pygame
import sys

from pygame.constants import K_ESCAPE

FPS = 60
W = 400
H = 700 
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK=(0,0,0)
 
sc = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
x = W // 2 - 40
y = 600
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
            sys.exit()
    sc.fill(BLACK)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, WHITE,(pos),2)
    pygame.draw.rect(sc, WHITE, (x, y,80,15),2)
    pygame.draw.rect(sc, WHITE, (0, 0,W-2,H-2),1)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0: 
        if x-5>0: x -= 5
        else: x=0
    elif keys[pygame.K_RIGHT] and x<W-82:
        if x+5<W-82 : x += 5
        else: x=W-82 
       
    clock.tick(FPS)