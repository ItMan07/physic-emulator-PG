import sys
from random import randint
from config import *
import numpy as np

pos = np.array([WIDTH // 2, HEIGHT // 2])
gravity = np.array([0, 1])
velocity = np.array([randint(0, 10), 0])

running = 1
while running:
    clock.tick(FPS)

    velocity += gravity
    pos += velocity

    # print(f"Speed: {0}\nVelocity: {0}\nPosition: {pos}\n")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("[LOG] Завершение цикла программы...")
            pygame.quit()
            sys.exit()

    if pos[0] + RADIUS >= WIDTH:
        velocity[0] *= DAMP
        velocity[0] = -velocity[0]
        pos[0] = WIDTH - RADIUS
    if pos[0] <= RADIUS:
        velocity[0] *= DAMP
        velocity[0] = -velocity[0]
        pos[0] = RADIUS

    if pos[1] + RADIUS >= HEIGHT:
        velocity[1] *= DAMP
        velocity[1] = -velocity[1]
        pos[1] = HEIGHT - RADIUS
    if pos[1] <= RADIUS:
        velocity[1] *= DAMP
        velocity[1] = -velocity[1]
        pos[1] = RADIUS

    screen.fill((220, 220, 220))
    pygame.draw.circle(screen, RED, (pos[0], pos[1]), RADIUS)

    pygame.display.flip()
