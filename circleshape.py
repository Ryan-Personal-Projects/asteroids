import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """
    CircleShape is a base class for creating circular shapes in a game using Pygame. 
    It inherits from `pygame.sprite.Sprite` and provides basic functionality for 
    positioning, movement, collision detection, and rendering.

    Attributes:
        position (pygame.Vector2): The position of the circle in 2D space.
        velocity (pygame.Vector2): The velocity of the circle in 2D space.
        radius (float): The radius of the circle.

    Methods:
        __init__(x, y, radius):
            Initializes a CircleShape instance with a given position and radius.
        collision_check(other_shape):
            Checks for collision with another CircleShape instance.
        draw(screen):
            Abstract method to draw the circle on the screen. Must be overridden by subclasses.
        update(dt):
            Abstract method to update the circle's state. Must be overridden by subclasses.
    """
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision_check(self, other_shape):
        collision_distance = self.radius + other_shape.radius
        cur_distance = self.position.distance_to(other_shape.position)
        return cur_distance <= collision_distance

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass