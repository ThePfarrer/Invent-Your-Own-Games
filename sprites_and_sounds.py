import pygame
import sys
import time
import random
from pygame.locals import *

# Set up pygame.
pygame.init()
main_clock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# Set up the colors.
WHITE = (255, 255, 255)

# Set up the block data structure.
player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load('player.png')
player_stretched_image = pygame.transform.scale(player_image, (40, 40))
food_image = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20),
                             random.randint(0, WINDOWHEIGHT - 20), 20, 20))

food_counter = 0
NEWFOOD = 40

# Set up movement variables.
move_left = False
move_right = False
move_up = False
move_down = False

MOVESPEED = 6

# Set up the music.
pick_up_sound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
music_playing = True

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True
            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_playing = not music_playing

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(
                event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    food_counter += 1
    if food_counter >= NEWFOOD:
        # Add new food.
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20),
                                 random.randint(0, WINDOWHEIGHT - 20), 20, 20))

    # Draw the white background onto the surface.
    window_surface.fill(WHITE)

    # Move the player.
    if move_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if move_up and player.top > 0:
        player.top -= MOVESPEED
    if move_left and player.left > 0:
        player.left -= MOVESPEED
    if move_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the block onto the surface.
    window_surface.blit(player_stretched_image, player)

    # Check whether the block has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top,
                                 player.width + 2, player.height + 2)
            player_stretched_image = pygame.transform.scale(
                player_image, (player.width, player.height))
            if music_playing:
                pick_up_sound.play()

    # Draw the food.
    for food in foods:
        window_surface.blit(food_image, food)

    # Draw the window onto the screen.
    pygame.display.update()
    main_clock.tick(40)
