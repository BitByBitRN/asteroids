import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawn
    asteroids = pygame.sprite.Group() #all asteroids

    Player.containers = (updatable, drawable) #place Player into updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable) #asteroids are asteroids, drawable and updatable
    AsteroidField.containers = (updatable) #asteroidfield is only updatable (not an asteroid itself)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #screen object
    clock = pygame.time.Clock() #clock object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #player object
    asteroid_field = AsteroidField()
    
    dt = 0 #delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for object in asteroids:
            if object.check_collision(player):
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
