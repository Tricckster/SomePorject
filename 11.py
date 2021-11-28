# library
import pygame
import random
pygame.init()

music = random.randint(1, 4)
if music == 1:
    pygame.mixer.music.load('DVRST - Close Eyes (Slowed Reverb).mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
if music == 2:
    pygame.mixer.music.load('hxvrmxn-headlights-flashes.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
if music == 3:
    pygame.mixer.music.load('Perturbator_-_Future_Club.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
if music == 4:
    pygame.mixer.music.load('prxsxnt-fxture-tokyo-drift.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

W, H, FPS = 608, 1000, 60
# collors
white = (255, 255, 255)
blue = (0, 70, 225)
green = (70, 255, 0)
red = (255, 0, 0)
BLACK = (0, 0, 0)
# plf settings
plf_w, plf_h = 100, 20
plf_speed = 15
plf = pygame.Rect(W // 2 - plf_w // 2, 800, plf_w, plf_h)
# ball settings
ball_radius = 10
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
# blocks settings
block_list = [pygame.Rect(5 + 60 * i, 7 + 30 * j, 55, 26) for i in range(10) for j in range(7)]
color_list = [(random.randrange(30, 256), random.randrange(30, 256), random.randrange(30, 256)) for i in range(10) for j
              in range(7)]

pygame.init()
sc = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surf = pygame.Surface((W, H))
sc.blit(surf, ((sc.get_width() - W) // 2, (sc.get_height() - H) // 2))

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
            exit()

    surf.fill(BLACK)
    sc.fill(BLACK)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, white, (pos), 2)
    # drawing world
    [pygame.draw.rect(surf, color_list[color], block, 2) for color, block in enumerate(block_list)]
    pygame.draw.rect(surf, white, plf, 2)
    pygame.draw.circle(surf, pygame.Color('white'), ball.center, ball_radius, 2)
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

    # win, game over
    if ball.bottom > H:
        surf.fill(BLACK)
        sc.fill(BLACK)
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('GAME OVER', True, white)
        sc.blit(text1, (870, 540))
        pygame.display.update()
        pygame.time.delay(100)
    elif not len(block_list):
        surf.fill(BLACK)
        sc.fill(BLACK)
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('WIN', True, white)
        sc.blit(text1, (870, 540))
        pygame.display.update()
        pygame.time.delay(100)

    pygame.draw.rect(surf, white, (0, 0, W, H), 1)
    sc.blit(surf, ((sc.get_width() - W) // 2, (sc.get_height() - H) // 2))

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and plf.left > 0:
        plf.left -= plf_speed
    if key[pygame.K_RIGHT] and plf.right < W - 1:
        plf.right += plf_speed
    # update screen
    pygame.display.flip()
    clock.tick(FPS)
