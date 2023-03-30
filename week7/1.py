import pygame, sys, datetime

pygame.init()

display = pygame.display.set_mode((600, 600))

back = pygame.image.load('main-clock.png')
right = pygame.image.load('right-hand.png')
left = pygame.image.load('left-hand.png')

back = pygame.transform.scale(back, (600, 600))
right = pygame.transform.scale(right, (300, 300))
left = pygame.transform.scale(left, (300, 300))

left = pygame.transform.flip(left, 180, 180)


def rot_center(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(300, 300)).center)
    return rotated_image, new_rect

while True:
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x = (-6*min)%360
    y = ((-1)*sec * 6)%360

    rot_right, x = rot_center(right, x)
    rot_left, y = rot_center(left, y)

    display.blit(back, (0, 0))
    display.blit(rot_right, x)
    display.blit(rot_left, y)

    pygame.display.update()
