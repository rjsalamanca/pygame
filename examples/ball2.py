import pygame

class Ball:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.direction = 'left'
        self.speed = speed
        self.radius = radius

    def update(self, width, height):
        self.x += self.speed
        #self.y += self.speed_y
        if self.x - self.radius > width:
            self.speed_x = 0
        if self.x - self.radius < 0:
            self.speed_x = 5


    def display(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ball Example')

    # Game initialization
    ball_list = [
        Ball(50, 50, 5, 50),
        Ball(300, 200, 8, 30),
        Ball(100, 300, 12, 60),
        Ball(200, 200, 2, 40)
    ]
    stop_game = False
    while not stop_game:
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
            ball.display(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
