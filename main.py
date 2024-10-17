import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #creates screen
    
    clock = pygame.time.Clock()
    dt = 0

    #setting up groups for ease of object manipulation
    asteroid = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) #creates player in the middle of the screen
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #checks if user exited window and closes if so
                return
        
        screen.fill("black")  #fills screen with black
          
        for obj in drawable: #draws all objects in groups to screen
            obj.draw(screen)
        
        for obj in updateable:
            obj.update(dt)

        pygame.display.flip() #updates screen   
        dt = clock.tick(60)/1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()