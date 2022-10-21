import pygame

# константы
WIDTH = 640
HEIGHT = 480
FPS = 60
DAMP = 0.9
RADIUS = 30

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создаем игру и окно
pygame.init()
# pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physic emulator")
pygame.display.set_icon(pygame.image.load("icon.png"))

clock = pygame.time.Clock()
