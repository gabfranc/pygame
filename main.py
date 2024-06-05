import pygame
import time
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beach Fruit")

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (170, 125, 206), player)
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:  # Check if left key is pressed and player is within the left boundary
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:  # Check if right key is pressed and player is within the right boundary
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()  # Call pygame.quit() with parentheses

if __name__ == "__main__":
    main()
