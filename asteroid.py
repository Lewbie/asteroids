from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
        self.rotation = 0
                         
    def draw(self, screen):
        pos_x = int(self.position.x)
        pos_y = int(self.position.y)
        pygame.draw.circle(screen,"white", self.position , self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
