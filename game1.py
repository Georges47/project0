# Import library
import pygame
from pygame.locals import *

# Initialize game
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game 1")
keys = [False, False, False, False]  # WASD
playerPosition = [100, 100]

# Load resources
player = pygame.image.load("/home/dimi/Desktop/dim")
player = pygame.transform.scale(player, (100, 100))
background = pygame.image.load("/home/dimi/Desktop/grass")

# Loop game
while 1:
    # Clear screen before drawing again
    screen.fill((0, 0, 0))
    # Draw elements in screen
    for x in range(int(width / background.get_width()) + 1):
        for y in range(int(height / background.get_height()) + 1):
            screen.blit(background, (x * background.get_width(), y * background.get_height()))
    screen.blit(player, playerPosition)
    # Update screen
    pygame.display.flip()

    # Loop events
    for event in pygame.event.get():
        # Check if event is the X button in window
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    # Move player
    if keys[0] & (playerPosition[1] > 0):
        playerPosition[1] -= 1  # move up
    if keys[2] & (playerPosition[1] < height - 100):
        playerPosition[1] += 1  # move down
    if keys[1] & (playerPosition[0] > 0):
        playerPosition[0] -= 1  # move left
    if keys[3] & (playerPosition[0] < width - 100):
        playerPosition[0] += 1  # move right
