import pygame
 
FPS = 60
W = 400
H = 700 
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK=(0,0,0)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
 
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2 - 40
y = 600
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT,
                         pygame.K_RIGHT]:
                motion = STOP
 
    sc.fill(BLACK)
    pygame.draw.rect(sc, WHITE, (x, y,80,15),2)
    pygame.display.update()
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 5
    elif keys[pygame.K_RIGHT]:
        x += 5
 
    clock.tick(FPS)