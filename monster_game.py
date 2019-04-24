import pygame
import time
import random

class Character(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.speed = 5
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.monster_wait = 0

class Hero(Character):
    def __init__(self,image,x,y):
        super().__init__(image,pos)

class Monster(Character):
    def update(self,width,height):
        randomMove = random.randint(1,8)
        # 1 - North
        # 2 - East
        # 3 - South
        # 4 - West
        # 5 - North East
        # 6 - North West
        # 7 - South West
        # 8 - South East

        # X is EAST WEST
            # east is right +
            # west is left - 
        # Y is NORTH SOUTH
            # north is up - 
            # south is down +

        # made it wait only 60 loops
        if self.monster_wait == 30:
            if randomMove == 1 and (self.y - self.speed) > 0:
                self.y -= self.speed
            elif randomMove == 2 and (self.x + self.speed) < width:
                self.x += self.speed
            elif randomMove == 3 and (self.y + self.speed) < height:
                self.y += self.speed
            elif randomMove == 4 and (self.x - self.speed) > 0:
                self.x -= self.speed
            elif randomMove == 5 and (self.y - self.speed) > 0 and (self.x + self.speed) < width:
                self.y -= self.speed
                self.x += self.speed
            elif randomMove == 6 and (self.y - self.speed) > 0 and (self.x - self.speed) > 0:
                self.y -= self.speed
                self.x -= self.speed
            elif randomMove == 7 and (self.y + self.speed) < height and (self.x - self.speed) > 0:
                self.y += self.speed
                self.x -= self.speed
            elif randomMove == 8 and (self.y + self.speed) < height and (self.x + self.speed) < width:
                self.y += self.speed
                self.x += self.speed
            else:
                print('No move or out of bounds')

            self.monster_wait = 0
            self.rect.center = [self.x,self.y]
        else:
            self.monster_wait += 1
        
        # Monster Moves left to right then right to left 
        # self.x += self.speed
        # self.rect.center = [self.x,self.y]
        # if self.x > width:
        #     self.speed = -5
        # elif self.x < 0:
        #     self.speed = 5

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    # Our Hero
    player = Hero(hero_image, 256, 240)
    monster = Monster(monster_image, 20, 20)

    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        # Game logic
        monster.update(width,height)

        # Draw background
        screen.blit(background_image,[0,0])

        # Game display
        player_group.draw(screen)
        monster_group.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()