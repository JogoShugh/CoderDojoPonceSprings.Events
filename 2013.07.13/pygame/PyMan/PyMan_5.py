# ***** Check for collision and count the pellets ********

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('snake.png', -1)
        self.pellets = 0
        self.x_dist = 5
        self.y_dist = 5

    def move(self, key):
        x = y = 0
        if key == K_RIGHT:
            x = self.x_dist
        elif key == K_LEFT:
            x = -self.x_dist
        elif key == K_UP:
            y = -self.y_dist
        elif key == K_DOWN:
            y = self.y_dist
        self.rect.move_ip(x, y)


class Pellet(pygame.sprite.Sprite):
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('pellet.png', -1)
        if rect != None:
            self.rect = rect


class PyManMain:
    def __init__(self, width=640, height=480):
        pygame.init();
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        self.LoadSprites()

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        pygame.key.set_repeat(500, 30)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if (event.key == K_RIGHT
                       or event.key == K_LEFT
                       or event.key == K_UP
                       or event.key == K_DOWN):
                        self.snake.move(event.key)
            self.screen.blit(self.background, (0, 0))
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #1
            cols = pygame.sprite.spritecollide(self.snake,
                                               self.pellet_sprites,
                                               True)
            self.snake.pellets = self.snake.pellets + len(cols)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv #2
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render('Pellets %s' % self.snake.pellets,
                                    1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.width/2)
                self.screen.blit(text, textpos)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.pellet_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain(self.snake)
        numHorizontal = int(self.width / 64)
        numVertical = int(self.height / 64)
        self.pellet_sprites = pygame.sprite.Group()
        for x in range(numHorizontal):
            for y in range(numVertical):
                self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))


if __name__ == '__main__':
    MainWindow = PyManMain()
    MainWindow.MainLoop()
