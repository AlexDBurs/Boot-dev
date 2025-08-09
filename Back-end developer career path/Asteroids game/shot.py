import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)


    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.position += self.velocity * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt