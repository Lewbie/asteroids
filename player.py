from circleshape import *
from constants import *

class player(CircleShape):
    def __init__(self,x, y):
        self.position = pygame.Vector2(x,y)
        self.rotation = 50
        self.radius = 10

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
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            left = dt - (dt * 2)
            self.rotate(left)
        if keys[pygame.K_d]:
            self.rotate(dt)