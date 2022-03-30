import pygame
import random
import sys

pygame.init()

# Constant values.
HEIGHT, WIDTH = 400, 400
FONT = pygame.font.Font(None, 24)
FPS = 60
SIZE = 20

# Colours.
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE = 255, 255, 255


# Pygame variables.
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Asteroid Clone')
clock = pygame.time.Clock()


class PlayerShip:
    def __init__(self, posx, posy, VEL, direction):
        self.VEL = VEL
        self.direction = direction
        self.rect = pygame.Rect(posx, posy, SIZE, SIZE)


# This creates the FPS counter at the top left.
def fps_counter():
    count = str(int(clock.get_fps()))
    fps_txt = FONT.render(count, True, WHITE)
    ROOT.blit(fps_txt, (fps_txt.get_width() - fps_txt.get_width()//2, fps_txt.get_height() - fps_txt.get_height()//2))


def check_events():
    keys = pygame.key.get_pressed()
    if keys == pygame.K_LEFT:
        pass
    if keys == pygame.K_RIGHT:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            pass


def draw_root(player_obj):
    ROOT.fill(BLACK)
    pygame.draw.rect(ROOT, WHITE, player_obj.rect)
    fps_counter()
    pygame.display.update()


def main():
    while True:
        player_obj = PlayerShip(WIDTH - WIDTH / 2 - SIZE / 2, HEIGHT - HEIGHT / 2 - SIZE / 2, 8, 0)
        draw_root(player_obj)
        check_events()
        clock.tick(FPS)


if __name__ == '__main__':
    main()