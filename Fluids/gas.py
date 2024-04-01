import pygame
from pygame.locals import *
import os
os.environ['SDL_AUDIODRIVER'] = 'directx'
import math
import random

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
screen_x = int(dims.current_w*0.9)
screen_y = int(dims.current_h*0.9)
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
colors = list(pygame.colordict.THECOLORS.values())
running = True

#Set up simulation parameters
p_count = 1 #particle count
radius= 50 #particle radius
centers = [] #initialize center array
v_x = [] #initialize x velocity array
v_y = [] #initialize y velocity array
v_min = -5
v_max = 5
colors = list(pygame.colordict.THECOLORS.values())
particles = []

class Particle():
    def __init__(self, center, v_x, v_y, color):
        self.center = center
        self.x = self.center[0]
        self.y = self.center[1]
        self.v_x = v_x
        self.v_y = v_y
        self.angle = math.degrees(math.asin(self.v_y/self.v_x))
        self.color = color

    def update_pos(self):
        self.x += self.v_x
        self.y += self.v_y
        self.center[0] = self.x
        self.center[1] = self.y
        self.angle = math.degrees(math.asin(self.v_y/self.v_x))
        print(self.angle)
        self.check_bounds()

    def check_bounds(self):
        if self.x+radius >= screen_x or self.x-radius <= 0:
            self.v_x*=-1
        if self.y+radius >= screen_y or self.y-radius <= 0:
            self.v_y*=-1
    
    def check_collision(self, index, particles:list):
        for particle in particles:
            if ((self.x-particle.x)**2+(self.y-particle.y)**2)**0.5 <= 2*radius:
                particle.v_x*=-1
                particle.v_y*=-1
                self.v_x*=-1
                self.v_y*=-1


for i in range(p_count):
    particles.append(Particle(
        pygame.Vector2(random.randint(radius, screen_x-radius), random.randint(radius, screen_y-radius)),
        random.random()*random.randint(v_min, v_max),
        random.random()*random.randint(v_min, v_max),
        colors[random.randint(0, len(colors)-1)])
        )
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for index, particle in enumerate(particles):
        particle.check_collision(index, particles)
        particle.update_pos()
        pygame.draw.circle(surface=screen, color=particle.color, center=particle.center, radius=radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()