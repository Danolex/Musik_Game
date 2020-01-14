import pygame
from objects import *
from functions import *


def lvl1():
    global mc
    mc = MainCharacter('mc.png')
    mc.rect.x = 400
    mc.rect.y = 500
    pygame.mixer.init()
    pygame.mixer.music.load('music/music1.mp3')
    pygame.mixer.music.play()
    start_game(projectiles1)


def lvl2():
    global mc
    mc = MainCharacter('mc.png')
    mc.rect.x = 400
    mc.rect.y = 500
    pygame.mixer.init()
    pygame.mixer.music.load('music/music2.mp3')
    pygame.mixer.music.play()
    start_game(projectiles2)


def start_game(lvl):
    tick = 0
    while True:
        if tick in projectiles1:
            for el in projectiles1[tick]:
                el.rect.x = el.pos_x
                el.rect.y = el.pos_y
                el.is_on_screen = True
        if tick % 15 == 0:
            Projectile(0, 50, 0, 5, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print(tick)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mc.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mc.move_right()
        all_sprites.update()
        screen.fill(bg_color)
        pygame.draw.line(screen, (230, 230, 230), (0, 510), (800, 510), 3)
        all_sprites.draw(screen)
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
mc = None
projectiles1 = {
    45: (Projectile(0, 0, 0, 5), Projectile(750, 0, 0, 5)),
    60: (Projectile(0, 0, 5, 5),),
    75: (Projectile(0, 0, 5, 5),),
    90: (Projectile(0, 0, 5, 5),),
    105: (Projectile(0, 0, 5, 5),),
    120: (Projectile(0, 0, 5, 5),),
    135: (Projectile(0, 0, 5, 5),),
    150: (Projectile(0, 0, 5, 5),),
    165: (Projectile(0, 0, 5, 5),),
}

projectiles2 = {
    30: Projectile(0, 0, 5, 5),
    60: Projectile(0, 0, 5, 5),
    90: Projectile(0, 0, 5, 5),
    120: Projectile(0, 0, 5, 5),
}
