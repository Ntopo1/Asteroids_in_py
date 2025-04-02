import pygame
from constants import *
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    print('"Starting Asteroids!"')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create Groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # Create containers
    
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots_group, updatable, drawable)

    # Create player instance in the middle of the screen
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # General Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,1))
        updatable.update(dt)

        #check for collisions
        for asteroid in all_asteroids:
            if player_instance.collisionsCheck(asteroid):
                print('Game Over')
                sys.exit()
            for shot in shots_group:
                if shot.collisionsCheck(asteroid):
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
        

        #Draw all objects
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    
if __name__ == "__main__":
    main()
