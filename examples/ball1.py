import pygame
import random

class Ball:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def update(self, width, height):
        randomRadius = random.randint(1,200)
        randomSpeed = random.randint(1,15)
        randomY = random.randint(1,height)
        self.x += self.speed

        if self.x - self.radius > width:
            self.speed = -randomSpeed
            print('first print rad: ' , self.radius)
            self.radius = randomRadius
            print('rand: ' ,randomRadius)
            print('second print rad: ' , self.radius)
            self.y = randomY

        if self.x + self.radius < 0:
            self.speed = randomSpeed
            print('first print rad Less : ' , self.radius)
            self.radius = randomRadius
            print('rand: ' ,randomRadius)
            print('second print radLess: ' , self.radius)
            self.y = randomY


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Simple Example')

    # Put Game Initialization Code Here
    ball_list = [
        Ball(50, 50, 1,1)


    ]
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        # Game logic
        for ball in ball_list:
            ball.update(width, height)

        # Draw background
        screen.fill(blue_color)

        # Game display
        for ball in ball_list:
            ball.render(screen)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
