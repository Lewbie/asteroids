import pygame
from constants import *
from player import *

def main():
    pygame.init
    gameloop = True
    dt = 0
    clock = pygame.time.Clock()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    while(gameloop):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()