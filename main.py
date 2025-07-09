import pygame
from player import *
from circleshape import *
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ### initialise game
    pygame.init()
    #
    clock = pygame.time.Clock()
    # init player
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
     

    ### game loop
    running = True
    while running != False:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), (0, 0, 1280, 720))
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()


