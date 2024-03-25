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
colors = list(pygame.colordict.THECOLORS.values())
dt = 0
cor = 0.94
g_init = 10
x_init = screen.get_width() / 2
y_init = screen.get_height() / 2
gravity = g_init
v_x = 50
v_y = 0

#Thickness of the bounding circle
t_bound = 10
#Radius of the bounding circle
r_bound = (y_init)

#Ball radius
radius = 10
contact_count = 0

player_pos = pygame.Vector2(x_init, y_init)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    color = colors[contact_count]
    #Bounding circle outside edge
    pygame.draw.circle(screen, "white", (x_init, y_init), r_bound)
    #Bounding circle inside edge
    pygame.draw.circle(screen, "black", (x_init, y_init), y_init-t_bound)

    #bouncing ball
    pygame.draw.circle(screen, color, player_pos, radius)

    player_pos.y+=gravity
    player_pos.x+=v_x
    
    # reverse direction if the ball hits either y bounding box
    if math.ceil((player_pos.y-y_init+radius)**2 + (player_pos.x-x_init+radius)**2)>= (r_bound-t_bound)**2:
        gravity = gravity*-1*cor
        v_x = v_x*-1*cor
        contact_count+=1

    gravity += g_init*dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()