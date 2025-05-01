import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    """
    Represents an asteroid in a 2D space, inheriting from CircleShape.
    Attributes:
        position (Vector2): The current position of the asteroid.
        radius (float): The radius of the asteroid.
        velocity (Vector2): The velocity vector of the asteroid.
    Methods:
        __init__(x, y, radius):
            Initializes an asteroid with a given position and radius.
        draw(screen):
            Draws the asteroid on the given screen using Pygame.
        update(dt):
            Updates the position of the asteroid based on its velocity and the time delta.
        split():
            Splits the asteroid into two smaller asteroids if its radius is greater than the minimum radius.
    """
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2