import pygame
import sys
from player import *
from circleshape import *
from constants import *
from asteroids import *
from asteroidfield import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ### initialise game
    pygame.init()
    #
    clock = pygame.time.Clock()
    dt = 0
    # groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    # init player and asteroids 
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    ### game loop
    running = True
    while running != False:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), (0, 0, 1280, 720))
        for drawable_object in drawable:
            drawable_object.draw(screen)
        updatable.update(dt, shots)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()



if __name__ == "__main__":
    main()


