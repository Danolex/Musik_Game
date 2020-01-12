import pygame
from objects import *
from functions import *


def lvl1():
    global mc
    mc = MainCharacter('mc.png')
    mc.rect.x = 400
    mc.rect.y = 500
    projectiles = {
        '1': Projectile('projectile.png', 75, 0, 0, 10),
        '30': Projectile('projectile.png', 75, 0, 0, 10),
        '50': Projectile('projectile.png', 75, 0, 0, 10),
    }
    pygame.mixer.init()
    pygame.mixer.music.load('music/music1.mp3')
    pygame.mixer.music.play()
    return projectiles


def lvl2():
    global mc
    mc = MainCharacter('mc.png')
    mc.rect.x = 400
    mc.rect.y = 500
    pygame.mixer.init()
    pygame.mixer.music.load('music/music2.mp3')
    pygame.mixer.music.play()
    start_game()


def start_game():
    global lvl1_proj
    tick = 0
    while True:
        if str(tick) in lvl1_proj:
            lvl1_proj[str(tick)].update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RSHIFT:
                    mc.dash()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mc.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mc.move_right()
        all_sprites.update()
        projectile_group.update()
        screen.fill(bg_color)
        all_sprites.draw(screen)
        projectile_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        tick += 1


def intro():
    fon = pygame.transform.scale(load_image('intro1.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    fon = pygame.transform.scale(load_image('intro2.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    fon = pygame.transform.scale(load_image('intro3.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                fon = pygame.transform.scale(load_image('loading.jpg'), (WIDTH, HEIGHT))
                screen.blit(fon, (0, 0))
                pygame.display.flip()
                return  # начинаем игру


size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
bg_color = (195, 195, 195)
TICK = 0
mc = None
lvl1_proj = lvl1()
