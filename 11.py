import pygame
import sys

FPS = 60
W = 400
H = 700 
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK=(0,0,0)
x = W // 2 - 40
y = 600

sc = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
surf = pygame.Surface((W, H))
sc.blit(surf, ((sc.get_width()-W)//2,(sc.get_height()-H)//2))

pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.constants.K_ESCAPE):
            sys.exit()
    sc.fill(BLACK)
    surf.fill(BLACK)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, WHITE,(pos),2)
    pygame.draw.rect(surf, WHITE, (x, y,80,15),2)
    pygame.draw.rect(surf, WHITE, (0, 0,W-2,H-2),1)
    sc.blit(surf, ((sc.get_width()-W)//2,(sc.get_height()-H)//2))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>1: 
        if x-5>0: x -= 5
        else: x=1
    elif keys[pygame.K_RIGHT] and x<W-83:
        if x+5<W-82 : x += 5
        else: x=W-83 
       
    clock.tick(FPS)
