import pygame
import random
from constants import *
from circleshape import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt, shots):
        self.position += self.velocity * dt
    def split(self):
        from asteroidfield import AsteroidField
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_asteroid_vel = self.velocity.rotate(angle)
            second_asteroid_vel = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_position = self.position.copy()
            AsteroidField.spawn(self, new_radius, new_position, (first_asteroid_vel * 1.2))
            AsteroidField.spawn(self, new_radius, new_position, (second_asteroid_vel * 1.2))
            

            

            

