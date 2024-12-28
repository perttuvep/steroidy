from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            new1 = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            new2 = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
            angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(angle) * 1.1
            vel2 = self.velocity.rotate(-angle) * 1.1
            new1.velocity = vel1
            new2.velocity = vel2
            self.kill()
            return (new1,new2)
        else: 
            self.kill()
            return

