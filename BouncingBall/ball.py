import pygame
from pygame.locals import *
import os
os.environ['SDL_AUDIODRIVER'] = 'directx'
import math

"""
TODO:

1. Add a pygame window
    a. Make the window size dynamic (use a general purpose "scale" variable)
2. Draw a bounding box and a ball within it.
3. Add physics (gravity, coefficient of restitution, collision detection, change in direction, etc.)
4. Determine what to do upon collision (increase velocity, change ball color, trace ball motion, make sound, etc)

"""

# pygame setup
pygame.init()
dims = pygame.display.Info()
screen = pygame.display.set_mode((dims.current_w*0.9, dims.current_h*0.9))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 1.05
v_init_x = 0.5
v_init_y = 0
radius = 20

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "white", player_pos, radius)

    player_pos.y+=gravity
    player_pos.x+=v_init_x
    gravity+=0.05
    
    # reverse direction if the ball hits either y bounding box
    if math.floor(player_pos.y + radius) >= screen.get_height() or math.floor(player_pos.y - radius) <= 0:
        gravity = gravity*-1

    # reverse direction if the ball hits either x bounding box
    if math.floor(player_pos.y + radius) >= screen.get_height() or math.floor(player_pos.y - radius) <= 0:
        gravity = gravity*-1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()