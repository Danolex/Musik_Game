import pygame
from functions import *
import random


# Главный цикл
def main():
    # Главный герой
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

    # Проджектайлы
    class Projectile(pygame.sprite.Sprite):
        def __init__(self, image_name, pos_x=0, pos_y=0, speed_x=0, speed_y=0, is_on_screen=False):
            super().__init__(projectile_group, all_sprites)
            try:
                self.image_name = image_name
            except Exception as exc:
                log(exc)
            self.image = load_image(self.image_name, -1)
            self.rect = self.image.get_rect()
            if not pos_x and not pos_y:
                self.rect.x = random.randrange(10, 790)
                self.rect.y = 0
                self.speed_x = random.randrange(-7, 7)
                self.speed_y = random.randrange(7, 12)
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

# Первый уровеь
    def lvl1():
        global mc
        fon = pygame.transform.scale(load_image('lvl1.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(1)
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
            15: (Projectile('projectile.png'),),
            59: (Projectile('projectile.png'),),
            93: (Projectile('projectile.png'),),
            116: (Projectile('projectile.png'),),
            171: (Projectile('projectile.png'),),
            193: (Projectile('projectile.png'),),
            243: (Projectile('projectile.png'),),
            268: (Projectile('projectile.png'),),
            313: (Projectile('projectile.png'),),
            325: (Projectile('projectile.png'),),
            339: (Projectile('projectile.png'),),
            351: (Projectile('projectile.png'),),
            382: (Projectile('projectile.png'),),
            408: (Projectile('projectile.png'),),
            429: (Projectile('projectile.png'),),
            457: (Projectile('projectile.png'),),
            494: (Projectile('projectile.png'),),
            527: (Projectile('projectile.png'),),
            587: (Projectile('projectile.png'),),
            613: (Projectile('projectile.png'),),
            661: (Projectile('projectile.png'),),
            674: (Projectile('projectile.png'),),
            688: (Projectile('projectile.png'),),
            702: (Projectile('projectile.png'),),
            715: (Projectile('projectile.png'),),
            729: (Projectile('projectile.png'),),
            788: (Projectile('projectile.png'),),
            819: (Projectile('projectile.png'),),
            870: (Projectile('projectile.png'),),
            907: (Projectile('projectile.png'),),
            939: (Projectile('projectile.png'),),
            994: (Projectile('projectile.png'),),
            1020: (Projectile('projectile.png'),),
            1069: (Projectile('projectile.png'),),
            1094: (Projectile('projectile.png'),),
            1143: (Projectile('projectile.png'),),
            1154: (Projectile('projectile.png'),),
            1166: (Projectile('projectile.png'),),
            1179: (Projectile('projectile.png'),),
            1209: (Projectile('projectile.png'),),
            1276: (Projectile('projectile.png'),),
            1315: (Projectile('projectile.png'),),
            1350: (Projectile('projectile.png'),),
            1406: (Projectile('projectile.png'),),
            1434: (Projectile('projectile.png'),),
            1485: (Projectile('projectile.png'),),
            1499: (Projectile('projectile.png'),),
            1513: (Projectile('projectile.png'),),
            1528: (Projectile('projectile.png'),),
            1543: (Projectile('projectile.png'),),
            1556: (Projectile('projectile.png'),),
            1568: (Projectile('projectile.png'),),
            1580: (Projectile('projectile.png'),),
            1592: (Projectile('projectile.png'),),
            1604: (Projectile('projectile.png'),),
            1615: (Projectile('projectile.png'),),
            1628: (Projectile('projectile.png'),),
            1640: (Projectile('projectile.png'),),
            1652: (Projectile('true_projectile.png'),),
            1670: (Projectile('true_projectile.png'),),
            1690: (Projectile('true_projectile.png'),),
            1710: (Projectile('true_projectile.png'),),
            1728: (Projectile('true_projectile.png'),),
            1747: (Projectile('true_projectile.png'),),
            1765: (Projectile('true_projectile.png'),),
            1784: (Projectile('true_projectile.png'),),
            1805: (Projectile('true_projectile.png'),),
            1822: (Projectile('true_projectile.png'),),
            1845: (Projectile('true_projectile.png'),),
            1864: (Projectile('true_projectile.png'),),
            1875: (Projectile('true_projectile.png'),),
            1896: (Projectile('true_projectile.png'),),
            1917: (Projectile('true_projectile.png'),),
            1938: (Projectile('true_projectile.png'),),
            1956: (Projectile('true_projectile.png'),),
            1974: (Projectile('true_projectile.png'),),
            1992: (Projectile('true_projectile.png'),),
            2012: (Projectile('true_projectile.png'),),
            2031: (Projectile('true_projectile.png'),),
            2052: (Projectile('true_projectile.png'),),
            2069: (Projectile('true_projectile.png'),),
            2082: (Projectile('true_projectile.png'),),
            2102: (Projectile('true_projectile.png'),),
            2122: (Projectile('true_projectile.png'),),
            2141: (Projectile('true_projectile.png'),),
            2160: (Projectile('true_projectile.png'),),
            2178: (Projectile('true_projectile.png'),),
            2197: (Projectile('true_projectile.png'),),
            2218: (Projectile('true_projectile.png'),),
            2238: (Projectile('true_projectile.png'),),
            2259: (Projectile('true_projectile.png'),),
            2280: (Projectile('true_projectile.png'),),
            2290: (Projectile('true_projectile.png'),),
            2310: (Projectile('true_projectile.png'),),
            2330: (Projectile('true_projectile.png'),),
            2352: (Projectile('true_projectile.png'),),
            2370: (Projectile('true_projectile.png'),),
            2386: (Projectile('true_projectile.png'),),
            2410: (Projectile('true_projectile.png'),),
            2427: (Projectile('true_projectile.png'),),
            2444: (Projectile('true_projectile.png'),),
            2465: (Projectile('true_projectile.png'),),
            2483: (Projectile('true_projectile.png'),),
            2496: (Projectile('true_projectile.png'),),
            2518: (Projectile('true_projectile.png'),),
            2538: (Projectile('true_projectile.png'),),
            2559: (Projectile('true_projectile.png'),),
            2572: (Projectile('true_projectile.png'),),
            2593: (Projectile('true_projectile.png'),),
            2612: (Projectile('true_projectile.png'),),
            2638: (Projectile('true_projectile.png'),),
            2664: (Projectile('true_projectile.png'),),
            2685: (Projectile('true_projectile.png'),),
            2698: (Projectile('true_projectile.png'),),
            2720: (Projectile('true_projectile.png'),),
            2743: (Projectile('true_projectile.png'),),
            2761: (Projectile('true_projectile.png'),),
            2779: (Projectile('true_projectile.png'),),
            2798: (Projectile('true_projectile.png'),),
            2817: (Projectile('true_projectile.png'),),
            2836: (Projectile('true_projectile.png'),),
            2856: (Projectile('true_projectile.png'),),
            2874: (Projectile('true_projectile.png'),),
            2893: (Projectile('true_projectile.png'),),
            2906: (Projectile('true_projectile.png'),),
            2927: (Projectile('true_projectile.png'),),
            2951: (Projectile('true_projectile.png'),),
            2968: (Projectile('true_projectile.png'),),
            2986: (Projectile('true_projectile.png'),),
            3004: (Projectile('true_projectile.png'),),
            3025: (Projectile('true_projectile.png'),),
            3047: (Projectile('true_projectile.png'),),
            3070: (Projectile('true_projectile.png'),),
            3098: (Projectile('true_projectile.png'),),
            3112: (Projectile('true_projectile.png'),),
            3135: (Projectile('true_projectile.png'),),
            3155: (Projectile('true_projectile.png'),),
            3174: (Projectile('true_projectile.png'),),
            3192: (Projectile('true_projectile.png'),),
            3210: (Projectile('true_projectile.png'),),
            3231: (Projectile('true_projectile.png'),),
        }
        while True:
            if tick == 3600:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        mc.speed_up()
                    if event.key == pygame.K_e:
                        print(tick)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        mc.speed_down()
            if tick in projectiles:
                for el in projectiles[tick]:
                    el.is_on_screen = True
            if tick % 15 == 0:
                Projectile('projectile.png', 10, 10, 0, 5, True)
                Projectile('projectile.png', 780, 0, 0, 5, True)
            control()
            tick += 1

# Второй уровень
    def lvl2():
        global mc
        fon = pygame.transform.scale(load_image('lvl2.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        clock.tick(1)
        try:
            mc.kill()
        except Exception as exc:
            log(exc)
        mc = MainCharacter('mc.png')
        mc.rect.x = 400
        mc.rect.y = 500

        try:
            pygame.mixer.init()
            pygame.mixer.music.load('music/music2.mp3')
            pygame.mixer.music.play()
        except Exception as exc:
            log(exc)
        tick = 0
        beat = 0
        projectiles = {
            75: (Projectile("projectile.png"),),
            92: (Projectile("projectile.png"),),
            112: (Projectile("projectile.png"),),
            123: (Projectile("projectile.png"),),
            134: (Projectile("projectile.png"),),
            152: (Projectile("projectile.png"),),
            163: (Projectile("projectile.png"),),
            173: (Projectile("projectile.png"),),
            188: (Projectile("projectile.png"),),
            205: (Projectile("projectile.png"),),
            215: (Projectile("projectile.png"),),
            225: (Projectile("projectile.png"),),
            246: (Projectile("projectile.png"),),
            255: (Projectile("projectile.png"),),
            264: (Projectile("projectile.png"),),
            276: (Projectile("projectile.png"),),
            286: (Projectile("projectile.png"),),
            301: (Projectile("projectile.png"),),
            313: (Projectile("projectile.png"),),
            332: (Projectile("projectile.png"),),
            337: (Projectile("projectile.png"),),
            345: (Projectile("projectile.png"),),
            370: (Projectile("projectile.png"),),
            378: (Projectile("projectile.png"),),
            387: (Projectile("projectile.png"),),
            411: (Projectile("projectile.png"),),
            418: (Projectile("projectile.png"),),
            426: (Projectile("projectile.png"),),
            440: (Projectile("projectile.png"),),
            450: (Projectile("projectile.png"),),
            463: (Projectile("projectile.png"),),
            484: (Projectile("projectile.png"),),
            498: (Projectile("projectile.png"),),
            506: (Projectile("projectile.png"),),
            518: (Projectile("projectile.png"),),
            539: (Projectile("projectile.png"),),
            546: (Projectile("projectile.png"),),
            555: (Projectile("projectile.png"),),
            580: (Projectile("projectile.png"),),
            586: (Projectile("projectile.png"),),
            597: (Projectile("projectile.png"),),
            621: (Projectile("projectile.png"),),
            629: (Projectile("projectile.png"),),
            639: (Projectile("projectile.png"),),
            662: (Projectile("projectile.png"),),
            670: (Projectile("projectile.png"),),
            680: (Projectile("projectile.png"),),
            703: (Projectile("projectile.png"),),
            711: (Projectile("projectile.png"),),
            719: (Projectile("projectile.png"),),
            744: (Projectile("projectile.png"),),
            753: (Projectile("projectile.png"),),
            763: (Projectile("projectile.png"),),
            781: (Projectile("projectile.png"),),
            799: (Projectile("projectile.png"),),
            818: (Projectile("projectile.png"),),
            830: (Projectile("projectile.png"),),
            847: (Projectile("projectile.png"),),
            870: (Projectile("projectile.png"),),
            878: (Projectile("projectile.png"),),
            887: (Projectile("projectile.png"),),
            912: (Projectile("projectile.png"),),
            919: (Projectile("projectile.png"),),
            930: (Projectile("projectile.png"),),
            961: (Projectile("projectile.png"),),
            969: (Projectile("projectile.png"),),
            991: (Projectile("projectile.png"),),
            1011: (Projectile("projectile.png"),),
            1034: (Projectile("projectile.png"),),
            1042: (Projectile("projectile.png"),),
            1053: (Projectile("projectile.png"),),
            1078: (Projectile("projectile.png"),),
            1086: (Projectile("projectile.png"),),
            1106: (Projectile("projectile.png"),),
            1120: (Projectile("projectile.png"),),
            1140: (Projectile("projectile.png"),),
            1163: (Projectile("projectile.png"),),
            1184: (Projectile("projectile.png"),),
            1215: (Projectile("projectile.png"),),
            1239: (Projectile("projectile.png"),),
            1261: (Projectile("projectile.png"),),
            1282: (Projectile("projectile.png"),),
            1292: (Projectile("projectile.png"),),
            1308: (Projectile("projectile.png"),),
            1335: (Projectile("projectile.png"),),
            1354: (Projectile("projectile.png"),),
            1379: (Projectile("projectile.png"),),
            1401: (Projectile("projectile.png"),),
            1420: (Projectile("projectile.png"),),
            1442: (Projectile("projectile.png"),),
            1451: (Projectile("projectile.png"),),
            1462: (Projectile("black_projectile.png"),),
            1475: (Projectile("black_projectile.png"),),
            1492: (Projectile("black_projectile.png"),),
            1512: (Projectile("black_projectile.png"),),
            1548: (Projectile("black_projectile.png"),),
            1571: (Projectile("black_projectile.png"),),
            1593: (Projectile("black_projectile.png"),),
            1608: (Projectile("black_projectile.png"),),
            1617: (Projectile("black_projectile.png"),),
            1629: (Projectile("black_projectile.png"),),
            1642: (Projectile("black_projectile.png"),),
            1660: (Projectile("black_projectile.png"),),
            1679: (Projectile("black_projectile.png"),),
            1710: (Projectile("black_projectile.png"),),
            1721: (Projectile("black_projectile.png"),),
            1740: (Projectile("black_projectile.png"),),
            1761: (Projectile("black_projectile.png"),),
            1774: (Projectile("black_projectile.png"),),
            1783: (Projectile("black_projectile.png"),),
            1794: (Projectile("black_projectile.png"),),
            1817: (Projectile("black_projectile.png"),),
            1835: (Projectile("black_projectile.png"),),
            1869: (Projectile("black_projectile.png"),),
            1880: (Projectile("black_projectile.png"),),
            1904: (Projectile("black_projectile.png"),),
            1926: (Projectile("black_projectile.png"),),
            1940: (Projectile("black_projectile.png"),),
            1949: (Projectile("black_projectile.png"),),
            1960: (Projectile("black_projectile.png"),),
            1973: (Projectile("black_projectile.png"),),
            1994: (Projectile("black_projectile.png"),),
            2010: (Projectile("black_projectile.png"),),
            2038: (Projectile("black_projectile.png"),),
            2049: (Projectile("black_projectile.png"),),
            2069: (Projectile("black_projectile.png"),),
            2088: (Projectile("black_projectile.png"),),
            2099: (Projectile("black_projectile.png"),),
            2112: (Projectile("black_projectile.png"),),
            2125: (Projectile("black_projectile.png"),),
            2138: (Projectile("black_projectile.png"),),
            2153: (Projectile("black_projectile.png"),),
            2175: (Projectile("black_projectile.png"),),
            2205: (Projectile("black_projectile.png"),),
            2219: (Projectile("black_projectile.png"),),
            2237: (Projectile("black_projectile.png"),),
            2257: (Projectile("black_projectile.png"),),
            2270: (Projectile("black_projectile.png"),),
            2280: (Projectile("black_projectile.png"),),
            2292: (Projectile("black_projectile.png"),),
            2304: (Projectile("black_projectile.png"),),
            2324: (Projectile("black_projectile.png"),),
            2341: (Projectile("black_projectile.png"),),
            2373: (Projectile("black_projectile.png"),),
            2385: (Projectile("black_projectile.png"),),
            2405: (Projectile("black_projectile.png"),),
            2426: (Projectile("black_projectile.png"),),
            2437: (Projectile("black_projectile.png"),),
            2449: (Projectile("black_projectile.png"),),
            2460: (Projectile("black_projectile.png"),),
            2489: (Projectile("black_projectile.png"),),
            2508: (Projectile("black_projectile.png"),),
            2539: (Projectile("black_projectile.png"),),
            2553: (Projectile("black_projectile.png"),),
            2574: (Projectile("black_projectile.png"),),
            2595: (Projectile("black_projectile.png"),),
            2611: (Projectile("black_projectile.png"),),
            2621: (Projectile("black_projectile.png"),),
            2634: (Projectile("black_projectile.png"),),
            2659: (Projectile("black_projectile.png"),),
            2680: (Projectile("black_projectile.png"),)
        }
        while True:
            if tick == 3000:
                return
            if tick % 15 == 0:
                Projectile('side_projectile.png', 10, 10, 0, 5, True)
                Projectile('side_projectile.png', 780, 0, 0, 5, True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        mc.speed_up()
                    if event.key == pygame.K_e:
                        print(tick)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        mc.speed_down()
            if tick in projectiles:
                for el in projectiles[tick]:
                    el.is_on_screen = True
            control()
            tick += 1

# Основное управление персонажем и отрисовка экрана
    def control():
        global mc

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mc.move_left()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mc.move_right()
        all_sprites.update()
        screen.fill(bg_color)
        pygame.draw.line(screen, (255, 255, 255), (0, 510), (800, 510), 3)

        all_sprites.draw(screen)
        pygame.draw.line(screen, (0, 0, 0), (0, 0), (800, 0), 58)
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
        pygame.mixer.music.stop()
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

    def main_menu():
        fon = pygame.transform.scale(load_image('main_menu.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        cursor = MainCharacter('mc.png', 200, 240)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        play = True
        exit = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        cursor.rect.x = 200
                        cursor.rect.y = 240
                        play = True
                        exit = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        cursor.rect.x = 200
                        cursor.rect.y = 300
                        play = False
                        exit = True
                    if event.key == pygame.K_SPACE:
                        if exit:
                            terminate()
                        if play:
                            cursor.kill()
                            return
            screen.blit(fon, (0, 0))
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()


    size = WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60
    bg_color = (195, 195, 195)
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    projectile_group = pygame.sprite.Group()
    mc = None

    intro()
    main_menu()

    lvl1()

    lvl2()

    fon = pygame.transform.scale(load_image('win.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    exit()


main()
