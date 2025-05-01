import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    """
    Represents a shot in the game, inheriting from CircleShape.
    Attributes:
        position (Vector2): The position of the shot.
        radius (float): The radius of the shot, defined by SHOT_RADIUS.
        velocity (Vector2): The velocity of the shot.
    Methods:
        __init__(x, y):
            Initializes a Shot instance with a given position (x, y).
        draw(screen):
            Draws the shot on the given screen as a white circle.
        update(dt):
            Updates the position of the shot based on its velocity and the time delta (dt).
    """
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity