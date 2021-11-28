# library
import pygame
import sys
from random import randrange as rnd

W,H,FPS=400,700,60
# collors
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK=(0,0,0)
# plf settings
plf_w,plf_h = 80,15
plf_speed = 15
plf = pygame.Rect(W // 2 - plf_w // 2,600, plf_w, plf_h)
# ball settings
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
# blocks settings
block_list = [pygame.Rect(7 + 40 * i, 7 + 40 * j, 38, 38) for i in range(10) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]

pygame.init()
sc = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
surf = pygame.Surface((W, H))
sc.blit(surf, ((sc.get_width()-W)//2,(sc.get_height()-H)//2))
sc.fill(BLACK)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.constants.K_ESCAPE):
            sys.exit()
    
    surf.fill(BLACK)

    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, WHITE,(pos),2)
    # drawing world
    [pygame.draw.rect(surf, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(surf, pygame.Color('darkorange'), plf)
    pygame.draw.circle(surf, pygame.Color('white'), ball.center, ball_radius)
    # ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    # collision left right
    if ball.centerx < ball_radius or ball.centerx > W - ball_radius:
        dx = -dx
    # collision top
    if ball.centery < ball_radius:
        dy = -dy
    # collision plf
    if ball.colliderect(plf) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, plf)
    # collision blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)
        # special effect
        hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
        pygame.draw.rect(sc, hit_color, hit_rect)
        FPS += 2
    # win, game over
    if ball.bottom > H:
        print('GAME OVER!')
        exit()
    elif not len(block_list):
        print('WIN!!!')
        exit()

    pygame.draw.rect(surf, WHITE, (0, 0,W-2,H-2),1)
    sc.blit(surf, ((sc.get_width()-W)//2,(sc.get_height()-H)//2))
    pygame.display.update()
    
        # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and plf.left > 0:
        plf.left -= plf_speed
    if key[pygame.K_RIGHT] and plf.right < W:
        plf.right += plf_speed
    # update screen
    pygame.display.flip()
    clock.tick(FPS)
