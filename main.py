import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Shot.containers = (updatable,drawable,shots)
    Player.containers = (updatable,drawable) # pyright: ignore
    Asteroid.containers = (asteroids,updatable,drawable) #pyright: ignore
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField.containers =(updatable) #pyright: ignore
    asteroidfield = AsteroidField()

    updatable.add(asteroids)
    while True:

        screen.fill(color="black")

        for item in updatable:
            item.update(dt)

        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if ast.collision(shot):
                    shot.kill()
                    ast.split()
                    break

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
