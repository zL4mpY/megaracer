import pygame, pygame_menu, os, sys

pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Mega Racer')

menu = pygame_menu.Menu('Mega Racer', 720, 480,
                       theme=pygame_menu.themes.THEME_BLUE)

mainloop = True

while mainloop == True:

    def start_the_game():
        pygame.quit()
        os.system('python libs\game.py')

    def show_controls():
        controls = 'W для передвижения вверх, ' \
                   'A для передвижения влево, ' \
                   'S для передвижения вниз, ' \
                   'D для передвижения вправо ' \


        menu.add.label(controls, max_char=-1, font_size=20)

    play = menu.add.button('Играть', start_the_game)
    controls = menu.add.button('Управление', show_controls)
    quit = menu.add.button('Выйти', pygame_menu.events.EXIT)

    menu.mainloop(screen)
