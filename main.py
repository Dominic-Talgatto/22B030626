import pygame
import random
from sys import exit


def Pipes(pipes_rec):
    if pipes_rec:
        for p_rec in pipes_rec:
            p_rec.x -= 5
            if p_rec.colliderect(bird_rec):
                exit()
            if p_rec.right <= -100:
                pipes_rec.remove(p_rec)
            if 200 <= p_rec.bottom <= 600:
                screen.blit(pipe_down, p_rec)
            else:
                screen.blit(pipe, p_rec)
        return pipes_rec
    else:
        return []


pygame.init()
screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (1280, 960))

bird = pygame.image.load('bird.png').convert_alpha()
bird_rec = bird.get_rect(midbottom=(200, 700))

pipe = pygame.image.load('pipe.png').convert_alpha()
pipe = pygame.transform.scale(pipe, (120, 700))
pipe_rec = pipe.get_rect(midbottom=(1000, 1200))

pipe_down = pygame.image.load('pipedown.png').convert_alpha()
pipe_down = pygame.transform.scale(pipe_down, (120, 700))
pipe_down_rec = pipe_down.get_rect(midtop=(900, 100))

pipes = []

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 1800)

gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = -15
        if event.type == pipe_timer:
            num = random.randint(0, 2)
            if num == 0: pipes.append(pipe.get_rect(midbottom=(random.randint(1300, 1500), random.randint(1100, 1200))))
            else: pipes.append(pipe_down.get_rect(midbottom=(random.randint(1300, 1500), random.randint(400, 600))))

    bird_rec.y += gravity
    gravity += 1

    if bird_rec.top <= 0:
        bird_rec.top = 0
        gravity = 0
        gravity += 1
    elif bird_rec.bottom >= 960:
        bird_rec.bottom = 960

    screen.blit(background, (0, 0))
    screen.blit(bird, bird_rec)
    pipes = Pipes(pipes)
    # screen.blit(pipe, pipe_rec)
    # screen.blit(pipe_down, pipe_down_rec)

    pygame.display.update()
    clock.tick(60)
