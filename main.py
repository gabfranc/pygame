import pygame
import time
import random

pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beach Fruit")

BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 60

PLAYER_VEL = 5
FRUIT_VEL = 5
FRUIT_WIDTH = 11
FRUIT_HEIGHT = 20

FONT = pygame.font.SysFont("roboto", 40)

def draw(player, elapsed_time, fruits):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"{round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (170, 125, 206), player)

    for fruit in fruits: 
        pygame.draw.rect(WIN, "pink", fruit)

    pygame.display.update()

def draw_game_over():
    lost_text = FONT.render("GAME OVER!", 1, (136, 13, 30))
    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2 - 40))
    
    reset_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2, 200, 50)
    pygame.draw.rect(WIN, (211, 213, 212), reset_button)
    reset_text = FONT.render("RESTART?", 1, (23, 24, 59))
    WIN.blit(reset_text, (reset_button.x + reset_button.width/2 - reset_text.get_width()/2, reset_button.y + reset_button.height/2 - reset_text.get_height()/2))
    
    pygame.display.update()
    return reset_button

def draw_start_screen():
    WIN.blit(BG, (0, 0))
    play_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 - 25, 200, 50)
    pygame.draw.rect(WIN, (59, 66, 159), play_button)
    play_text = FONT.render("Play Game", 1, (240, 235, 216))
    WIN.blit(play_text, (play_button.x + play_button.width/2 - play_text.get_width()/2, play_button.y + play_button.height/2 - play_text.get_height()/2))
    
    pygame.display.update()
    return play_button

def main():
    run = True
    game_over = False
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0
    
    fruit_add_increment = 2000
    fruit_count = 0

    fruits = []
    hit = False

    start_screen = True

    while run:
        if start_screen:
            play_button = draw_start_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button.collidepoint(mouse_pos):
                        start_screen = False
                        start_time = time.time()  # Reset the start time
            continue
        
        fruit_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if fruit_count > fruit_add_increment:
            for _ in range(3):
                fruit_x = random.randint(0, WIDTH - FRUIT_WIDTH)
                fruit = pygame.Rect(fruit_x, -FRUIT_HEIGHT, FRUIT_WIDTH, FRUIT_HEIGHT)
                fruits.append(fruit)

            fruit_add_increment = max(200, fruit_add_increment - 50)
            fruit_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                mouse_pos = pygame.mouse.get_pos()
                if reset_button.collidepoint(mouse_pos):
                    main()  # Restart the game
                    return

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL

            for fruit in fruits[:]:
                fruit.y += FRUIT_VEL
                if fruit.y > HEIGHT:
                    fruits.remove(fruit)
                elif fruit.y + fruit.height >= player.y and fruit.colliderect(player):
                    fruits.remove(fruit)
                    hit = True
                    break

            if hit:
                game_over = True
                reset_button = draw_game_over()

        if not game_over:
            draw(player, elapsed_time, fruits)

    pygame.quit()

if __name__ == "__main__":
    main()
