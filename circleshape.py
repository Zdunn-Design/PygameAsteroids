import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collision(self, CircleShape):
        status = False
        r1 = self.radius
        r2 = CircleShape.radius
        distance = r1 + r2
        if self.position.distance_to(CircleShape.position) <= distance:
            status = True
        return status
    
