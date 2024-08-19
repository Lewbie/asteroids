import pygame
from constants import *

def main():
    pygame.init
    gameloop = True
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(gameloop):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

    
if __name__ == "__main__":
    main()