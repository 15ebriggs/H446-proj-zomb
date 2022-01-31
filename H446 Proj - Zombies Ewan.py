#--------Importing Libraries -------#
import pygame #Graphical Library for the game.
import random #Used to create random events in game.
import sys    #For clean closing of the application (game).
import math   #Used for calculating angles. 
 
#Tuple colours (R,G,B) for testing.
# Will delete once sprite maps are used. 
RED_Colour   = (255, 0, 0)
GREEN_Colour = (0,255,0)
BLUE_Colour  = (0, 0, 255)
BLACK_Colour = (0, 0, 0)
WHITE_Colour = (255, 255, 255)
 
#--------Defining Classes -------#

#****class PlayerCrosshair Description***#
#PlayerCrosshair Class creates the player crosshair to target
# NPC's. The update method is used to update the posstion of the 
# crosshair depending on where the mouse is pointing.
class PlayerCrosshair(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = pygame.Surface([50, 50]) #Need to replace with sprite image.
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    def update(self):
        #Gets the current x,y mouse positon as an array.
        pos = pygame.mouse.get_pos()
 
        #Setting the crosshair posstion based on the x,y position of
        # the mouse.  pos[0] is x and  pos[1] is y
        # for shooting -25 to point at centre of crosshair image.
        self.rect.x = pos[0]-25                                 
        self.rect.y = pos[1]-25 
 
#****class EnemyNPC Description***#
#Need to write description
# 
class EnemyNPC(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
 
        self.image = pygame.Surface([20, 15]) #Need to replace with sprite image.
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

    def update(self):
        #Need to write code
        print("DEBUG: Update NPC objects")
 
#****class Player Description***#
#Need to write description
# 
class Player(pygame.sprite.Sprite):
    def __init__(self,gameWindowRes_width,gameWindowRes_height,playerMovementSpeed):
        super().__init__()
 
        self.image = pygame.Surface([20, 20]) #Need to replace with sprite image.
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.playerX_pos = gameWindowRes_width /2 #Centre of screen.
        self.playerY_pos = gameWindowRes_height/2 #Centre of screen.
        self.playerMovementSpeed = playerMovementSpeed
 
    def updatePlayerMovement(self):
        #Gets all key pressed and stores in keysPressed for evaluation later.
        keysPressed = pygame.key.get_pressed() 

        #Checks what keys are pressed to see if player postion should be updated.
        if keysPressed[pygame.k_w]: #Move Player UP
            self.playerY_pos  -= self.playerMovementSpeed

        if keysPressed[pygame.k_a]: #Move Player LEFT
            self.playerX_pos  -= self.playerMovementSpeed

        if keysPressed[pygame.k_s]: #Move Player DOWN
            self.uplayerY_pos += self.playerMovementSpeed

        if keysPressed[pygame.k_d]: #Move Player RIGHT
            self.playerX_pos  += self.playerMovementSpeed

    def update(self):
        #Need to write code
        print("DEBUG: Update Player object")

class PlayerBulletPistol(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([5, 5])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def updateBullets(self,playerX,playerY):
       #Bullet movement.
        pos = pygame.mouse.get_pos()
        #self.rect.x =
        #self.rect.y = 

         
#--------Defining Classes -------#
pygame.init() # Initialize Pygame
 
# Setting up the game window resolution (height & width).
gameWindowRes_width  = 800
gameWindowRes_height = 600
gameWindow = pygame.display.set_mode([gameWindowRes_width, gameWindowRes_height])

#Load Images
background_img = pygame.image.load("bg5.jpg")
crosshair_img = pygame.image.load("paternus1.png")

 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(500):
    # This represents a block
    block = Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)

crosshair = Crosshair((235, 117, 147))
all_sprites_list.add(crosshair)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
 
    # --- Draw a frame
 
    # Clear the screen
    gameWindow.fill((214, 114, 196))
    gameWindow.blit(background_img,((0,0)))
 
    # Draw all the spites
    all_sprites_list.draw(gameWindow)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
