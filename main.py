import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

updateble = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updateble, drawable)
Asteroid.containers = (asteroids, updateble, drawable)
AsteroidField.containers = (updateble)

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        updateble.update(dt)
        for i in asteroids:
            if player.collision(i):
                print("Game over!")
                sys.exit()
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()