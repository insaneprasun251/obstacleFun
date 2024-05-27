import pygame
from sys import exit

# Function for score
# 
def displayScore():
    global score
    global score_rect
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score.get_rect(center = (400, 40))
    screen.blit(score, score_rect)

# initiating pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Trebuchet MS", 25)
font_big = pygame.font.SysFont("Trebuchet MS", 50)

# Creating sky and ground
sky_surface = pygame.image.load("images/sky.png").convert()
ground_surface = pygame.image.load("images/ground.png").convert()

# Game over and restart
gameOver = font_big.render("Game Over", False, (64, 64, 64))
gameOver_rect = gameOver.get_rect(center = (400, 200))
restart = font.render("Press SPACE to restart", False, (64, 64, 64))
restart_rect = restart.get_rect(center = (400, 370))

# creating the game characters
snail = pygame.image.load("images/snail.png").convert_alpha()
snail_rect = snail.get_rect(topleft = (800, 265))
player = pygame.image.load("images/player.png").convert_alpha()
player_rect = player.get_rect(topleft = (50, 196))

# Common game variables
player_gravity = 0
game_active = True
start_time = 0

# Main game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 316:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

    # Logic of the game
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        displayScore()

        snail_rect.x -= 4.5
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail, snail_rect)

        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom >= 316: player_rect.bottom = 316
        screen.blit(player, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(score, score_rect)
        screen.blit(gameOver, gameOver_rect)
        screen.blit(restart, restart_rect)

    pygame.display.update()
    clock.tick(60)