import pygame, sys, random, time, pygame_menu, os

FPS = 60
FramePerSec = pygame.time.Clock()
score = 0


width = 720
height = 480

pygame.init()
game = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mega Racer')
game.fill((255,255,255))

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

road = pygame.image.load("road.png")

game_is_going = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (150, 240-166)
        self.speed_y = 10
        self.speed_x = self.speed_y
    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if keys[pygame.K_w]:
                self.rect.move_ip(0, -self.speed_y)
        if self.rect.bottom < height:
            if keys[pygame.K_s]:
                self.rect.move_ip(0, self.speed_y)
        if self.rect.left > 0:
            if keys[pygame.K_a]:
                self.rect.move_ip(-self.speed_x, 0)
        if self.rect.right < width:
            if keys[pygame.K_d]:
                self.rect.move_ip(self.speed_x, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.speed = random.randint(5, 10)
        self.rect = self.image.get_rect()
        self.rect.center = (800, random.randint(0+166, 480-166))
    def move(self):
        if self.rect.left > -300:
            self.rect.move_ip(-self.speed, 0)


enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = Player()
enemy = Enemy()

enemies.add(enemy)
all_sprites.add(enemy)
all_sprites.add(player)

text = font.render(str('Mega Racer'), True, (255, 255, 255))

while game_is_going == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    for entity in all_sprites:
        game.fill((255, 255, 255))
        game.blit(road, (0, 0))
        game.blit(text, (200, 40))
        game.blit(enemy.image, enemy.rect)
        game.blit(player.image, player.rect)
        entity.move()

    if enemy.rect.left <= -300:
        score += 1
        all_sprites.remove(enemy)
        enemies.remove(enemy)
        enemy.kill()
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)


    if pygame.sprite.spritecollideany(player, enemies):
        for entity in all_sprites:
            entity.kill()
        game_is_going = False
        menu_lose = pygame_menu.Menu('Проигрыш', 720, 480,
                       theme=pygame_menu.themes.THEME_DARK)

        def restart():
            os.execv(sys.executable, ['python'] + sys.argv)

        def show_controls():
            controls = 'W для передвижения вверх, ' \
                       'A для передвижения влево, ' \
                       'S для передвижения вниз, ' \
                       'D для передвижения вправо ' \


            menu_lose.add.label(controls, max_char=-1, font_size=20)

        menu_lose.add.label(f'Вы проиграли. Ваш счёт: {score}', max_char=-1, font_size=20)
        play = menu_lose.add.button('Заново', restart)
        controls = menu_lose.add.button('Управление', show_controls)
        quit = menu_lose.add.button('Выйти', pygame_menu.events.EXIT)

        menu_lose.mainloop(game)
    
    score_text = font_small.render(f'Очки: {score}', True, (255, 255, 255))
    game.blit(score_text, (10, 10))
    
    pygame.display.update()
    FramePerSec.tick(FPS)
