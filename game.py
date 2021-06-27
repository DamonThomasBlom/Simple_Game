import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates a variable to keep track of time
clock = pygame.time.Clock()
current_time = 0

# This creates the player,enemies and prize and gives it the image found in this folder

player = pygame.image.load("soldier.png")
enemy = pygame.image.load("Enemy (1).png")
enemy2 = pygame.image.load("Enemy (2).png")
enemy3 = pygame.image.load("Enemy (3).png")
prize = pygame.image.load("gold-medal.png")

# Get the width and height of the images in order to do boundary detection

# player
image_height = player.get_height()
image_width = player.get_width()

# enemy 1
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

# enemy 2
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

# enemy 3
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# prize
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player,enemies and prize as variables so that you can change them later.

playerXPosition = 400
playerYPosition = 280

# Make the enemies start off screen and at a random y or x position.
# enemy 1
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

# enemy 2
enemy2XPosition = random.randint(0, screen_width - enemy2_width)
enemy2YPosition = 0 - enemy2_height

# enemy 3
enemy3XPosition = 0 - enemy_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

# The prize will also start off the screen
prizeXPosition = 0 - prize_width
prizeYPosition = 0 - prize_height

# This checks if the up,down,left or right key is pressed.
# Right now they are not so make them equal to the boolean value of False.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# ============== Game loop starts here ================

while 1: # This is a looping structure that will loop the indented code until you tell it to stop

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))  # This draws the player image to the screen at the postion specfied.
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()  # This updates the screen.
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:  # This makes sure that the user does not move the player over the left of the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:  # This makes sure that the user does not move the player over the right of the window.
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding box for the enemy 2:

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Bounding box for the enemy 3:

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        # Display winning status to the user:
        prizeCollide = True
        print("You Win!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    # If the player does not collide with the prize they lose so we check if the prize is off screen
    if prizeYPosition > screen_height + prize_height:
        # Display losing status to the user:

        print("You Lose!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    # We store the current time in this variable so that we can perform certain actions at different times
    current_time = pygame.time.get_ticks()
    
    # Make enemy approach the player.
    # I change certain enemy speeds so they don't all move at the same speed and become predictable
    enemyXPosition -= 0.2          # enemy 1 will start moving at the beginning of the game
    enemyYPosition -= 0.05
    if current_time > 8000:        # enemy 2 will start moving at 8 seconds
        enemy2YPosition += 0.25
        enemy2XPosition += 0.05

    if current_time > 12000:        # enemy 3 will start moving at 12 seconds
        enemy3XPosition += 0.35
        enemy3YPosition -= 0.05

    # Make the prize move

    if current_time > 16000:        # prize will start moving at 16 seconds
        prizeXPosition += 0.35
        prizeYPosition += 0.25

    
    # ================The game loop logic ends here. =============