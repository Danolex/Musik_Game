import pygame
from functions import load_image


GRAVITY = 5
size = WIDTH, HEIGHT = 800, 600
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, image_name, pos_x=0, pos_y=0):
        super().__init__(player_group, all_sprites)
        self.image_name = image_name
        self.image = load_image(self.image_name)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = 5
        self.dash_speed = 20
        self.dash_time = 60
        self.is_dash = False
        self.dash_delay = 0
        self.direction = 'right'

    def move_right(self):
        if self.rect.x < WIDTH - 20:
            self.rect.x += self.speed
            self.direction = 'right'

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'

    def update(self):
        pass


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, speed_x=0, speed_y=0, is_on_screen=False):
        super().__init__(projectile_group, all_sprites)
        self.image = load_image('projectile.png')
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.is_on_screen = is_on_screen

    def update(self):
        if self.is_on_screen:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
                self.kill()
