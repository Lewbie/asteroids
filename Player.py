import pygame
from circleshape import *
from constants import *
from Shot import Shot

class Player(CircleShape):
    def __init__(self,x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def rotate(self ,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
        else:
            self.cooldown = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            left = dt - (dt * 2)
            self.rotate(left)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            up = dt
            self.move(up)      
        if keys[pygame.K_s]:
            down = dt - (dt * 2)
            self.move(down)
        if keys[pygame.K_SPACE]:
            if self.cooldown == 0:
                self.shoot()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = velocity
        self.cooldown = 0.5
        #shot.velocity.rotate(self.rotation)
        