import pygame
from constants import *
from Player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init

    #variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    gameloop = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    
    asteroid_field = AsteroidField()
    
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    dt = 0


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

       

    while(gameloop):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                print("Exiting Game")
                return
             
        for obj in updatable:
            obj.update(dt)
       
        screen.fill("black")
    
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000
        

    
if __name__ == "__main__":
    main()