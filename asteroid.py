from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        vector_1 = self.velocity.rotate(random.uniform(20, 50))
        vector_2 = self.velocity.rotate(-random.uniform(20, 50))
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid_1.velocity = vector_1 * 1.2
        asteroid_2.velocity = vector_2 * 1.2