import pygame
from objects import *
from functions import *


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
            15: (Projectile(0, 0, 5, 5),)
        }
        while True:
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
            15: (Projectile(0, 0, 5, 5),)
        }
        while True:
            if tick in projectiles:
                for el in projectiles[tick]:
                    el.is_on_screen = True
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        beat += 1
                        print(beat, ':', tick)
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
        fon = pygame.transform.scale(load_image('gameover.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()
        key_pressed = False
        while True:
            if key_pressed:
                break
            for event in pygame.event.get():
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

    #fon = pygame.transform.scale(load_image('lvl1.jpg'), (WIDTH, HEIGHT))
    #screen.blit(fon, (0, 0))
    #pygame.display.flip()
    #clock.tick(1)
    #lvl1()

    fon = pygame.transform.scale(load_image('lvl2.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    clock.tick(1)
    lvl2()

    fon = pygame.transform.scale(load_image('win.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    pygame.display.flip()


main()
