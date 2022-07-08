import sys
import pygame
import random
def rnd(l,r):
    return random.randint(l,r)
def p(image_p, i_p, j_p):
    screen.blit(image_p, (i_p * 32, j_p * 32))
def render_background():
    for i in range(16):
        for j in range(16):
            p(image_background, i, j)
# init image
image_background = pygame.image.load('background.png')
image_gapple = pygame.image.load('gapple.png')
image_head = pygame.image.load('head.png')
image_body = pygame.image.load('body.png')
image_pause = pygame.image.load('pause.png')
image_pause_background = pygame.image.load('pause_background.png')
image_pause_background.set_alpha(150)
# init pygame
# 16 x 16 map
pygame.init()
screen = pygame.display.set_mode((512, 512))
render_background()
pygame.display.set_caption('JamGame')
# main code
# create snake
snake = [(0, 0), (0, 1)]
l = len(snake)
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir = 3
p(image_body, snake[0][1], snake[0][0])
p(image_head, snake[1][1], snake[1][0])
# get gapple
gapple_x = rnd(0,15)
gapple_y = rnd(0,15)
p(image_gapple, gapple_y, gapple_x)
clock = pygame.time.Clock()
pygame.time.wait(500)
over = False
pause = False
while True:
    clock.tick(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = not pause
                if pause:
                    screen.blit(image_pause_background, (0, 0))
                    screen.blit(image_pause, (152, 182))
                else:
                    render_background()
                    p(image_gapple, gapple_y, gapple_x)
                    for i in range(l):
                        if i < l - 1:
                            p(image_body, snake[i][1], snake[i][0])
                        else:
                            p(image_head, snake[i][1], snake[i][0])
            elif event.key == pygame.K_w and not dir == 1:
                dir = 0
            elif event.key == pygame.K_s and not dir == 0:
                dir = 1
            elif event.key == pygame.K_a and not dir == 3:
                dir = 2
            elif event.key == pygame.K_d and not dir == 2:
                dir = 3
    if over or pause:
        pygame.display.update()
        continue
    p(image_body, snake[l - 1][1], snake[l - 1][0])
    print(snake[l - 1])
    newPos = ((snake[l - 1][0] + d[dir][0] + 16) % 16, (snake[l - 1][1] + d[dir][1] + 16) % 16)
    if snake.count(newPos) and newPos != snake[0]:
        over = True
        continue
    snake.append(newPos)
    l += 1
    if snake[l - 2] == (gapple_x, gapple_y):
        while snake.count((gapple_x, gapple_y)):
            gapple_x = rnd(0, 15)
            gapple_y = rnd(0, 15)
        p(image_gapple, gapple_y, gapple_x)
    else:
        p(image_background, snake[0][1], snake[0][0])
        snake.remove(snake[0])
        l -= 1
    p(image_head, snake[l - 1][1], snake[l - 1][0])
    pygame.display.update()