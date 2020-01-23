import pygame
from objects import *
from functions import *
import random


def main():
    class MainCharacter(pygame.sprite.Sprite):
        def __init__(self, image_name, pos_x=0, pos_y=0):
            super().__init__(player_group, all_sprites)
            self.image_name = image_name
            try:
                self.image = load_image(self.image_name)
            except Exception as exc:
                log(exc)
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y
            self.speed = 5
            self.direction = 'right'

        def move_right(self):
            if self.rect.x < WIDTH - 20:
                self.rect.x += self.speed
                self.direction = 'right'

        def move_left(self):
            if self.rect.x > 0:
                self.rect.x -= self.speed
                self.direction = 'left'

        def speed_up(self):
            self.speed += 5

        def speed_down(self):
            self.speed -= 5

        def update(self):
            if pygame.sprite.spritecollideany(self, projectile_group):
                self.kill()
                game_over()

    class Projectile(pygame.sprite.Sprite):
        def __init__(self, pos_x=0, pos_y=0, speed_x=0, speed_y=0, is_on_screen=False):
            super().__init__(projectile_group, all_sprites)
            try:
                self.image_name = 'projectile.png'
            except Exception as exc:
                log(exc)
            self.image = load_image(self.image_name, -1)
            self.rect = self.image.get_rect()
            if not pos_x and not pos_y:
                self.rect.x = random.randrange(10, 790)
                self.rect.y = 0
                self.speed_x = random.randrange(-10, 10)
                self.speed_y = random.randrange(2, 10)
            else:
                self.rect.x = pos_x
                self.rect.y = pos_y
                self.speed_x = speed_x
                self.speed_y = speed_y
            self.is_on_screen = is_on_screen

        def update(self):
            if self.is_on_screen:
                self.rect.x += self.speed_x
                self.rect.y += self.speed_y
                if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
                    self.kill()

    def lvl1():
        global mc
        try:
            mc = MainCharacter('mc.png')
            mc.rect.x = 400
            mc.rect.y = 500
        except Exception as exc:
            log(exc)
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('music/music1.mp3')
            pygame.mixer.music.play()
        except Exception as exc:
            log(exc)
        tick = 0
        projectiles = {
            15: (Projectile(),),
            59: (Projectile(),),
            93: (Projectile(),),
            116: (Projectile(),),
            171: (Projectile(),),
            193: (Projectile(),),
            243: (Projectile(),),
            268: (Projectile(),),
            313: (Projectile(),),
            325: (Projectile(),),
            339: (Projectile(),),
            351: (Projectile(),),
            382: (Projectile(),),
            408: (Projectile(),),
            429: (Projectile(),),
            457: (Projectile(),),
            494: (Projectile(),),
            527: (Projectile(),),
            587: (Projectile(),),
            613: (Projectile(),),
            661: (Projectile(),),
            674: (Projectile(),),
            688: (Projectile(),),
            702: (Projectile(),),
            715: (Projectile(),),
            729: (Projectile(),),
            788: (Projectile(),),
            819: (Projectile(),),
            870: (Projectile(),),
            907: (Projectile(),),
            939: (Projectile(),),
            994: (Projectile(),),
            1020: (Projectile(),),
            1069: (Projectile(),),
            1094: (Projectile(),),
            1143: (Projectile(),),
            1154: (Projectile(),),
            1166: (Projectile(),),
            1179: (Projectile(),),
            1209: (Projectile(),),
            1276: (Projectile(),),
            1315: (Projectile(),),
            1350: (Projectile(),),
            1406: (Projectile(),),
            1434: (Projectile(),),
            1485: (Projectile(),),
            1499: (Projectile(),),
            1513: (Projectile(),),
            1528: (Projectile(),),
            1543: (Projectile(),),
            1556: (Projectile(),),
            1568: (Projectile(),),
            1580: (Projectile(),),
            1592: (Projectile(),),
            1604: (Projectile(),),
            1615: (Projectile(),),
            1628: (Projectile(),),
            1640: (Projectile(),),
            1652: (Projectile(),),
            1670: (Projectile(),),
            1690: (Projectile(),),
            1710: (Projectile(),),
            1728: (Projectile(),),
            1747: (Projectile(),),
            1765: (Projectile(),),
            1784: (Projectile(),),
            1805: (Projectile(),),
            1822: (Projectile(),),
            1845: (Projectile(),),
            1864: (Projectile(),),
            1875: (Projectile(),),
            1896: (Projectile(),),
            1917: (Projectile(),),
            1938: (Projectile(),),
            1956: (Projectile(),),
            1974: (Projectile(),),
            1992: (Projectile(),),
            2012: (Projectile(),),
            2031: (Projectile(),),
            2052: (Projectile(),),
            2069: (Projectile(),),
            2082: (Projectile(),),
            2102: (Projectile(),),
            2122: (Projectile(),),
            2141: (Projectile(),),
            2160: (Projectile(),),
            2178: (Projectile(),),
            2197: (Projectile(),),
            2218: (Projectile(),),
            2238: (Projectile(),),
            2259: (Projectile(),),
            2280: (Projectile(),),
            2290: (Projectile(),),
            2310: (Projectile(),),
            2330: (Projectile(),),
            2352: (Projectile(),),
            2370: (Projectile(),),
            2386: (Projectile(),),
            2410: (Projectile(),),
            2427: (Projectile(),),
            2444: (Projectile(),),
            2465: (Projectile(),),
            2483: (Projectile(),),
            2496: (Projectile(),),
            2518: (Projectile(),),
            2538: (Projectile(),),
            2559: (Projectile(),),
            2572: (Projectile(),),
            2593: (Projectile(),),
            2612: (Projectile(),),
            2638: (Projectile(),),
            2664: (Projectile(),),
            2685: (Projectile(),),
            2698: (Projectile(),),
            2720: (Projectile(),),
            2743: (Projectile(),),
            2761: (Projectile(),),
            2779: (Projectile(),),
            2798: (Projectile(),),
            2817: (Projectile(),),
            2836: (Projectile(),),
            2856: (Projectile(),),
            2874: (Projectile(),),
            2893: (Projectile(),),
            2906: (Projectile(),),
            2927: (Projectile(),),
            2951: (Projectile(),),
            2968: (Projectile(),),
            2986: (Projectile(),),
            3004: (Projectile(),),
            3025: (Projectile(),),
            3047: (Projectile(),),
            3070: (Projectile(),),
            3098: (Projectile(),),
            3112: (Projectile(),),
            3135: (Projectile(),),
            3155: (Projectile(),),
            3174: (Projectile(),),
            3192: (Projectile(),),
            3210: (Projectile(),),
            3231: (Projectile(),),
        }
        while True:
            if tick == 3600:
                return
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        print(tick)
            if tick in projectiles:
                for el in projectiles[tick]:
                    el.is_on_screen = True
            if tick % 15 == 0:
                Projectile(0, 0, 0, 5, True)
                Projectile(793, 0, 0, 5, True)
            control()
            tick += 1

    def lvl2():
        global mc
        try:
            mc = MainCharacter('mc.png')
            mc.rect.x = 400
            mc.rect.y = 500
        except Exception as exc:
            log(exc)
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('music/music2.mp3')
            pygame.mixer.music.play()
        except Exception as exc:
            log(exc)
        tick = 0
        beat = 0
        projectiles = {
            15: (Projectile(0, 0, 5, 5),),
            60: (Projectile(),),
            75: (Projectile(),),
            92: (Projectile(),),
            112: (Projectile(),),
            123: (Projectile(),),
            134: (Projectile(),),
            152: (Projectile(),),
            163: (Projectile(),),
            173: (Projectile(),),
            188: (Projectile(),),
            205: (Projectile(),),
            215: (Projectile(),),
            225: (Projectile(),),
            246: (Projectile(),),
            255: (Projectile(),),
            264: (Projectile(),),
            276: (Projectile(),),
            286: (Projectile(),),
            301: (Projectile(),),
            313: (Projectile(),),
            332: (Projectile(),),
            337: (Projectile(),),
            345: (Projectile(),),
            370: (Projectile(),),
            378: (Projectile(),),
            387: (Projectile(),),
            411: (Projectile(),),
            418: (Projectile(),),
            426: (Projectile(),),
            440: (Projectile(),),
            450: (Projectile(),),
            463: (Projectile(),),
            484: (Projectile(),),
            498: (Projectile(),),
            506: (Projectile(),),
            518: (Projectile(),),
            539: (Projectile(),),
            546: (Projectile(),),
            555: (Projectile(),),
            580: (Projectile(),),
            586: (Projectile(),),
            597: (Projectile(),),
            621: (Projectile(),),
            629: (Projectile(),),
            639: (Projectile(),),
            662: (Projectile(),),
            670: (Projectile(),),
            680: (Projectile(),),
            703: (Projectile(),),
            711: (Projectile(),),
            719: (Projectile(),),
            744: (Projectile(),),
            753: (Projectile(),),
            763: (Projectile(),),
            781: (Projectile(),),
            799: (Projectile(),),
            818: (Projectile(),),
            830: (Projectile(),),
            847: (Projectile(),),
            870: (Projectile(),),
            878: (Projectile(),),
            887: (Projectile(),),
            912: (Projectile(),),
            919: (Projectile(),),
            930: (Projectile(),),
            961: (Projectile(),),
            969: (Projectile(),),
            991: (Projectile(),),
            1011: (Projectile(),),
            1034: (Projectile(),),
            1042: (Projectile(),),
            1053: (Projectile(),),
            1078: (Projectile(),),
            1086: (Projectile(),),
            1106: (Projectile(),),
            1120: (Projectile(),),
            1140: (Projectile(),),
            1163: (Projectile(),),
            1184: (Projectile(),),
            1215: (Projectile(),),
            1239: (Projectile(),),
            1261: (Projectile(),),
            1282: (Projectile(),),
            1292: (Projectile(),),
            1308: (Projectile(),),
            1335: (Projectile(),),
            1354: (Projectile(),),
            1379: (Projectile(),),
            1401: (Projectile(),),
            1420: (Projectile(),),
            1442: (Projectile(),),
            1451: (Projectile(),),
            1462: (Projectile(),),
            1475: (Projectile(),),
            1492: (Projectile(),),
            1512: (Projectile(),),
            1548: (Projectile(),),
            1571: (Projectile(),),
            1593: (Projectile(),),
            1608: (Projectile(),),
            1617: (Projectile(),),
            1629: (Projectile(),),
            1642: (Projectile(),),
            1660: (Projectile(),),
            1679: (Projectile(),),
            1710: (Projectile(),),
            1721: (Projectile(),),
            1740: (Projectile(),),
            1761: (Projectile(),),
            1774: (Projectile(),),
            1783: (Projectile(),),
            1794: (Projectile(),),
            1817: (Projectile(),),
            1835: (Projectile(),),
            1869: (Projectile(),),
            1880: (Projectile(),),
            1904: (Projectile(),),
            1926: (Projectile(),),
            1940: (Projectile(),),
            1949: (Projectile(),),
            1960: (Projectile(),),
            1973: (Projectile(),),
            1994: (Projectile(),),
            2010: (Projectile(),),
            2038: (Projectile(),),
            2049: (Projectile(),),
            2069: (Projectile(),),
            2088: (Projectile(),),
            2099: (Projectile(),),
            2112: (Projectile(),),
            2125: (Projectile(),),
            2138: (Projectile(),),
            2153: (Projectile(),),
            2175: (Projectile(),),
            2205: (Projectile(),),
            2219: (Projectile(),),
            2237: (Projectile(),),
            2257: (Projectile(),),
            2270: (Projectile(),),
            2280: (Projectile(),),
            2292: (Projectile(),),
            2304: (Projectile(),),
            2324: (Projectile(),),
            2341: (Projectile(),),
            2373: (Projectile(),),
            2385: (Projectile(),),
            2405: (Projectile(),),
            2426: (Projectile(),),
            2437: (Projectile(),),
            2449: (Projectile(),),
            2460: (Projectile(),),
            2489: (Projectile(),),
            2508: (Projectile(),),
            2539: (Projectile(),),
            2553: (Projectile(),),
            2574: (Projectile(),),
            2595: (Projectile(),),
            2611: (Projectile(),),
            2621: (Projectile(),),
            2634: (Projectile(),),
            2659: (Projectile(),),
            2680: (Projectile(),),
        }
        while True:
            if tick == 3000:
                return
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        beat += 1
                        print(beat, ':', tick)
            if tick in projectiles:
                for el in projectiles[tick]:
                    el.is_on_screen = True
            control()
            tick += 1

    def control():
        global mc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    mc.speed_up()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    mc.speed_down()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mc.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mc.move_right()
        all_sprites.update()
        screen.fill(bg_color)
        pygame.draw.line(screen, (255, 255, 255), (0, 510), (800, 510), 3)

        all_sprites.draw(screen)
        pygame.draw.line(screen, (195, 195, 195), (0, 0), (800, 0), 10)
        pygame.display.flip()
        clock.tick(fps)

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

    def game_over():
        pygame.mixer.stop()
        fon = pygame.transform.scale(load_image('gameover.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        key_pressed = False
        while True:
            if key_pressed:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        key_pressed = True
        restart()

    def restart():
        main()

    size = WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60
    bg_color = (195, 195, 195)
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    projectile_group = pygame.sprite.Group()
    mc = None

    # intro()

    # fon = pygame.transform.scale(load_image('lvl1.jpg'), (WIDTH, HEIGHT))
    # screen.blit(fon, (0, 0))
    # pygame.display.flip()
    # clock.tick(1)
    # lvl1()

    fon = pygame.transform.scale(load_image('lvl2.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    lvl2()

    fon = pygame.transform.scale(load_image('win.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()


main()
