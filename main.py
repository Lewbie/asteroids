import pygame
from constants import *
from Player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init

    #variables

    #pygame variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #setting up groups

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    
    #initialise player and asteroids.
    asteroid_field = AsteroidField()
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    #set up game loop and dt

    dt = 0
    gameloop = True

    #start game

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    while(gameloop):
        #exit button
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                print("Exiting Game")
                return
             
        #update objects  
        for obj in updatable:
            obj.update(dt)    

        #collision detection
        for ast in asteroids:
            if ast.collision(player) == True:
                print("Game Over!")
                return         
            
       #reset screen
        screen.fill("black")

        #draw updated objects on screen object
        for obj in drawable:
            obj.draw(screen)

        #update screen object
        pygame.display.flip()

        #set FPS to 60, and set dt
        dt = clock.tick(60) / 1000
        

    
if __name__ == "__main__":
    main()