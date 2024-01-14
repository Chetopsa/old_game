#import libraries
#pygame library came from https://www.pygame.org/
import pygame

import random


pygame.init()

#import keys form pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT)

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# player object
class Player(pygame.sprite.Sprite):
    GAME_OVER = False
    speed = .23
    up = False
    down = False
    left = False
    right = True

    # the code for the __init__(self) fuction, lines 27-31, came from https://realpython.com/pygame-a-primer/
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def reset(self):
        self.rect.x = 0
        self.rect.y = 0

    def game_over(boolean):
        if boolean == True:
            Player.GAME_OVER = True
    def increase_speed():
        Player.speed += .025

    def get_location(self):
        x = self.rect.x
        y = self.rect.y
        return (x,y)

    def change_direction(direction):
        if direction == "right":
            Player.right = True
            Player.down = False
            Player.up = False
            Player.left = False
        if direction == "down":
            Player.right = False
            Player.down = True
            Player.up = False
            Player.left = False
        if direction == "up":
            Player.right = False
            Player.down = False
            Player.up = True
            Player.left = False
        if direction == "left":
            Player.right = False
            Player.down = False
            Player.up = False
            Player.left = True
    
    def update(self, pressed_keys):
        speed = Player.speed

        if pressed_keys[K_UP]:
            Player.change_direction("up") 
        if pressed_keys[K_DOWN]:
            Player.change_direction("down") 
        if pressed_keys[K_LEFT]:
            Player.change_direction("left") 
        if pressed_keys[K_RIGHT]:
            Player.change_direction("right") 

        if Player.up == True:
            self.rect.move_ip(0, -speed * dt)
        if Player.down == True:
            self.rect.move_ip(0, speed * dt)
        if Player.right == True:
            self.rect.move_ip(speed * dt, 0)
        if player.left == True:
            self.rect.move_ip(-speed * dt, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Item(pygame.sprite.Sprite):

    blit = False

    def random_xy():
        x = random.randint(25, SCREEN_WIDTH-25)
        y = random.randint(25, SCREEN_HEIGHT - 25)
        return (x,y)

    def blit_set(boolean):
        if boolean:
            Item.blit = True
        else:
            Item.blit = False


    # the code for the __init__(self) fuction, lines 116-120, came from https://realpython.com/pygame-a-primer/
    def __init__(self):
        super(Item, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 200))
        self.rect = self.surf.get_rect()
        self.rect.center = Item.random_xy()

class Enemy(pygame.sprite.Sprite):

    blit1 = False
    blit2 = False
    speed = .15

    # the code for the __init__(self) fuction, lines 130-134, came from https://realpython.com/pygame-a-primer/
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.center = Enemy.random_xy()

        
    def get_location(self):
        x = self.rect.x
        y = self.rect.y
        return (x,y)

    def random_xy():
        condition = True
        while condition:
            x = random.randint(25, SCREEN_WIDTH-25)
            y = random.randint(25, SCREEN_HEIGHT - 25)
            
            if abs(player.get_location()[0] - x) > 75 and abs(player.get_location()[1] - y) > 75:
                    condition = False
        return (x,y)



    def increase_speed():
        Enemy.speed += .024

    def direction(objec, player_xy):
        """Determine the direction that the
            enemy will move based off of the 
            players location"""

        
        enemy_xy = objec.get_location()

        playerx = player_xy[0] 
        playery = player_xy[1] 
        enemyx = enemy_xy[0]
        enemyy = enemy_xy[1]
        if enemyx < playerx:
            xdirection = 1
        else:
            xdirection = 0
        if enemyy < playery:
            ydirection = 3
        else:
            ydirection = 2
        if abs(enemyx - playerx) > abs(enemyy - playery):
            return xdirection
        else:
            return ydirection


    def move(self, objec):
        speed = Enemy.speed
        direction = Enemy.direction(objec, player.get_location())

        if direction == 2:
            self.rect.move_ip(0, -speed * dt)
        if direction == 3:
            self.rect.move_ip(0, speed * dt)
        if direction == 1:
            self.rect.move_ip(speed * dt, 0)
        if direction == 0:
            self.rect.move_ip(-speed * dt, 0)

    def blit_set1(boolean):
        if boolean:
            Enemy.blit1 = True
        else:
            Enemy.blit1 = False

    def blit_set2(boolean):
        if boolean:
            Enemy.blit2 = True
        else:
            Enemy.blit2 = False

def high_to_low(lst):
  biggest = 0 
  done = False
  new_lst = []
  updatelst = lst


  if len(lst) > 1:
    while not done:
      for i in updatelst:
        for k in updatelst:
          if i >= k:
            biggest += 1
        if biggest == len(updatelst):
          new_lst.append(i)
          updatelst.remove(i)
        biggest = 0
      if len(updatelst) == 1:
        new_lst.append(updatelst[0])
        done = True
    return(new_lst)
  else:
    return lst



#copied this function call from https://realpython.com/pygame-a-primer/
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#instantiate the player 
player = Player()


#assign game clock to a variable
clock = pygame.time.Clock()

#instantiate variables 
score = 0
counter = 0
speed_counter = 0
QUIT_GAME = False
high_scores = []


# Main loop, for lines 255-274 I used https://realpython.com/pygame-a-primer/ as a guide
while not QUIT_GAME:
    dt = clock.tick(80)
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                QUIT_GAME = True
        elif event.type == QUIT:
            QUIT_GAME = True
    
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    
    # Fill the screen with black
    screen.fill((0, 0, 0))

    #set blit variables to True when the objects will be shown on screen
    if counter == 2:
        item = Item()
        Item.blit_set(1)
    if counter == 1:
        enemy1 = Enemy()
        Enemy.blit_set1(1)
    if speed_counter == 5:
        Player.increase_speed()
        Enemy.increase_speed()
        speed_counter = 0
    if score >= 10 and counter == 2:
        Enemy.blit_set2(1)
        enemy2 = Enemy()


    #detect collisions
    if counter > 2 and player.rect.colliderect(item.rect):
            speed_counter += 1
            score += 1
            counter = 0
            Item.blit_set(0)
    if Enemy.blit1 == True and player.rect.colliderect(enemy1.rect):
        Player.GAME_OVER = True
    if Enemy.blit2 == True and player.rect.colliderect(enemy2.rect):
        Player.GAME_OVER = True


    # Draw blocks on the screen and move them
    screen.blit(player.surf, player.rect)
    if Item.blit == True:
        screen.blit(item.surf, item.rect)

    if Enemy.blit1 == True:
        screen.blit(enemy1.surf, enemy1.rect)
        enemy1.move(enemy1)
        if Enemy.blit2 == True:
            screen.blit(enemy2.surf, enemy2.rect)
            enemy2.move(enemy2)

    #count every frame
    counter += 1

    #reset game if player collides with enemy
    if Player.GAME_OVER == True:
            high_scores.append(score)
            player.reset()
            Enemy.blit_set1(False)
            Enemy.blit_set2(False)
            Item.blit_set(False)
            Player.speed = .23
            Enemy.speed = .15
            score = 0
            counter = 0
            Player.GAME_OVER = False



    #refresh display
    pygame.display.flip()


sorted_scores = high_to_low(high_scores)
print("--------------------------------------------------\n\n\n")
print("\t\tYour High Scores:")
for i in sorted_scores:
    print("\t\t\t" + str(i))

print("\n\n\n--------------------------------------------------")
