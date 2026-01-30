import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))

# TITLE AND ICON
pygame.display.set_caption("SPACE INVADERS")
background=pygame.image.load(r"C:\Users\nigam\Downloads\freepik__a-stylized-space-background-with-geometric-shapes-__90417.png")
#ADDING BACKGROUND IMAGE
# PLAYERS 
playerImg=pygame.image.load(r"C:\Users\nigam\Downloads\002-spaceship-1.png")
playerX=370
PlayerY=480
playerX_change=0 # we have create this variable to increment or decrement its value later in while loop

# ENEMY 
# enemyImg=pygame.image.load(r"C:\Users\nigam\Downloads\005-alien.png")
# enemmyX=random.randint(0,730) # we want enemy to appear at random places but we have to reload the entire screen we have fix this
# enemmyY=random.randint(50,150)
# enemmyX_change=0.2 # the spped of spaceship
# enemmyY_change=40

# for multipke enemies and movement
enemyImg=[]
enemmyX=[] # we want enemy to appear at random places but we have to reload the entire screen we have fix this
enemmyY=[]
enemmyX_change=[] # the spped of spaceship
enemmyY_change=[]
no_of_enemies=6
for i in range(no_of_enemies):   
    enemyImg.append(pygame.image.load(r"C:\Users\nigam\Downloads\005-alien.png"))
    enemmyX.append(random.randint(0,730)) # we want enemy to appear at random places but we have to reload the entire screen we have fix this
    enemmyY.append(random.randint(50,150))
    enemmyX_change.append(0.2) # the spped of spaceship
    enemmyY_change.append(40)

#BULLET
bulletImg=pygame.image.load(r"C:\Users\nigam\Downloads\006-bullet.png")
bulletY=480 # we have written 480 cuz we wanna shoot bullet as top of spaceship where itll be 480 postion
bulletX=0
bulletX_change=0 # bullet will move in y direction do we dont need x direction
bulletY_change=2 # we'll change it to 10 later (cuz we saw the results we directly change it to 2)
bullet_state="ready"

# CREATING A SCORE FOR COLLISION
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
# GAMEOVER TEXT
over_font=pygame.font.Font('freesansbold.ttf',64)

# SCORE
def show_score(x,y):
    score=font.render("score"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# adding game over fuction
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255)) # over font
    screen.blit(over_text,(200,250))

#PLAYERS
def player(x,y): # we will call this fuction in while loop (1234)
    screen.blit(playerImg,(x,y))
# def enemy(x,y): # we will call this fuction in while loop (1235)
#     screen.blit(enemyImg,(x,y)) # there are some cahnges when there will be multiple enemies 
def enemy(x,y,i): 
    screen.blit(enemyImg[i],(x,y))
    
# collision
def isCollision(enemmyX,enemmyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemmyX-bulletX,2))+(math.pow(enemmyY-bulletY,2))) 
    if distance<27:
        return True
    else:
        return False
    
# BULLETS
def fire_bullet(x,y):
    global bullet_state # we made this global inorder to access this
    bullet_state="fire"   
    screen.blit(bulletImg,(x+16,y+10)) #so that bullet appers on screen and (x+16 so that bullet appears to get shot from the top of spaceship middle)
#game loop
running=True
while running:
    screen.fill((0,0,0)) # THIS IS FOR BACKGROUND COLOR IS SHOULD BE IN WHILE LOOP 
    # THIS SHOULD BE ABOVE ALL CUZ the screen is drawn firstly and other characters above it
    # playerX += 0.1 #how that small icon will move(in rhs slowly) we'll comment it later
    # PlayerY -= 0.1 # lhs slowly
    screen.blit(background,(0,0)) # so that background image doesn't disapper  in a bit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-1 # when we press the left key it will move left by 0.3, the value is in -ve cuz we'll sub from x axis to move left(we change the value to 1 after adding background image)
            if event.key==pygame.K_RIGHT:
                playerX_change=1 # when we press the right arrow key it will move right by o.3 speed (we change the value to 1 after adding background image)
                
                # SPACEBAR IS FOR FIRING BULLETS
            if event.key==pygame.K_SPACE: # to fire bullet we will press space bar
                if bullet_state is "ready":# bullet will be fired only when its in ready postion and not continously
                    bulletX=playerX #(1256)
                    fire_bullet(bulletX,bulletY) #(1. the curremt position os spaceship and 2. the y coordinaye of bullet)
                # we 1st made the bulletX= playerX and the change the player x to bulletX (idk why!!??)
                # id think it fixed the issue that bullet should not follow the x direction of spaceship 
                             
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT: #If the released key was either the LEFT arrow key or the RIGHT arrow key…”
                playerX_change=0
            
            
    playerX+=playerX_change
    # Adding Boundaries (1238 algorithm)
    if playerX<=0: # if the ship reaches the y axis the vertical one lhs it will stop at end (when the y coordinate=0)
        playerX=0
    elif playerX>=736: # if the ship reaches the x axis the horizontal one Rhs it will stop at end (when the x coordinate=736)
        playerX=736
        
    # ENEMY MOVEMENT 1238
    # enemmyX+=enemmyX_change
    # if enemmyX<=0:
    #     enemmyX_change=0.3 # i missed this and didnt wrote change so the boundaries didnt formed
    #     enemmyY+=enemmyY_change
    # elif enemmyX>=736:
    #     enemmyX_change=-0.3 # i missed this and didnt wrote change so the boundaries didnt formed
    #     enemmyY+=enemmyY_change # because of this the enemy will move forward towards apceship after hitting boundaries 
    #     # and instead of enemyY i wrote emenyX so bee carefull!!
    # ENEMY WHEN NO OF ENEMY INCREASES (9733)
    for i in range(no_of_enemies):
        
        # GAMEOVER
        if enemmyY[i]>400: # when enemy reaches the 400 pixels (here we are collecting the enemies in other for loop)
            for j in range(no_of_enemies): # when any enemy reaches 200 pixels 
                enemmyY[j]=2000 #  all enemies will go beyond the screen
                game_over_text()
            break # the loop will brea and the enemies 
            
        enemmyX[i]+=enemmyX_change[i]
        if enemmyX[i]<=0:
            enemmyX_change[i]=0.3 
            enemmyY[i]+=enemmyY_change[i]
        elif enemmyX[i]>=736:
            enemmyX_change[i]=-0.3 
            enemmyY[i]+=enemmyY_change[i] # there was this error o forgot to write i in the change one
        collision=isCollision(enemmyX[i],enemmyY[i ],bulletX,bulletY) # we will move the collision inside the for loop and the previous one was only inside the while loop
        if collision:
            bulletY=480
            bullet_state="ready"
            score_value+=1
            
            enemmyX[i]=random.randint(0,730) # for respawing ater the bullet hit it ( the invader)
            enemmyY[i]=random.randint(50,150)   
        enemy(enemmyX[i],enemmyY[i],i)    # this will be added inside the for loop # the fuction will get called inside the for loop
            
    if bulletY<=0: # so we rest the position of bullet once it reach y=0 and (SHOOT MULTIPLE BULLETS)
        bulletY=480
        bullet_state="ready"
        
    # BULLET TO KEEP IT PERSISTENT OTHERWISE IT WILL APPEAR AND DISAPPEAR VERY QUICKLY (BULLET MOVEMENT)
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY) # previously here it was platerX but we chamged it to bulletX (1256)
        bulletY-=bulletY_change # To dec the distance of bullet so it'll move in y direction\
            
            
    #collision
    # IN LAST STEP WE WILL MOVEIT INSIDE THE FOR LOOP (9733)
    
    # collision=isCollision(enemmyX,enemmyY,bulletX,bulletY)
    # if collision:
    #     bulletY=480
    #     bullet_state="ready"
    #     score_value+=1
        
    #     enemmyX=random.randint(0,730) # for respawing ater the bullet hit it ( the invader)
    #     enemmyY=random.randint(50,150)   
        
    show_score(textX,textY)    
    player(playerX,PlayerY) # HERE WE ARE CALLING THI FUNCTION(1234)
    # enemy(enemmyX,enemmyY) # HERE WE ARE CALLING THE FUNCTION(1235)
    pygame.display.update()
