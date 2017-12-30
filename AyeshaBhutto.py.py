# a program that plays a game of 1-800-VIRUSATTACK 
# the name is very original I know
# TURN UP THE VOLUME FOR BEST EXPERIENCE.
# written by Ayesha Bhutto 

# imports pygame and functions
from pygame import * 
import pygame 
import random 
# imports math - square root functions
from math import sqrt
init() #initializes pygame.
SIZE = 600, 600 #Sets the screen size to 600 x 600.
screen = display.set_mode(SIZE) 
pygame.display.set_caption("1-800-VIRUSATTACK") # names the window of the game
button = 0 # mouse button is set as 0
 
# colours are defined through specific RGB colour  
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0) 
WHITE = (255,255,255)
GREEN = (0, 255, 0)

# fonts are imported from pygame module
FONT = font.SysFont("Times New Roman",25) 	
FONT2 = font.SysFont("comicsansms",100) 
FONT3 = font.SysFont("Monospace",37) 

# music is imported from file and plays throughout the game
fireSound = mixer.Sound("hotlinebling.wav")   
fireSound.play()



# -------------------------------- BALL INFO ---------------------------
BALLX = 0
BALLY = 1
BALLSPEEDX = 2
BALLSPEEDY = 3
COLOUR = 4
radiusOFball = 10


# loads Drake image for cursor
cursor = image.load("drakecursor.png")




def mousefigure(screen, mx, my):    # def statement defining what  the cursor should have
      
    mouse = Rect(mx-10,my,10,10)    # uploads the image for cusor that was defined above
    screen.blit(cursor, mouse) 


    

def initBall():
    ballx = random.randint(0, 600) # randomly setting the x position
    bally = random.randint(0, 600) # randomly setting the y position
    dirx = random.randint(-5,5) # randomly setting the x speed
    diry = random.randint(-5,5) # randomly setting the y speed
    COLOUR = random.choice ([RED, YELLOW]) 
    info = [ballx, bally, dirx, diry, COLOUR] # returning a list with all the info the ball needs
    return info # returning the list



def moveBall(info): # takes in the list of the ball
    info[BALLX] += info[BALLSPEEDX] # increases the position of the ball
    info[BALLY] += info[BALLSPEEDY]

# checks to see if the ball is hitting the walls in the x direction
    if info[BALLX] > 600:
        info[BALLX] = 600
        info[BALLSPEEDX] *= -1
    elif info[BALLX] < 0:
        info[BALLX] = 0
        info[BALLSPEEDX] *= -1
    
# checks to see if the ball is hitting the walls in the y direction
    if info[BALLY] < 0:
        info[BALLY] = 0
        info[BALLSPEEDY] *= -1 
    elif info[BALLY] > 600:
        info[BALLY] = 600
        info[BALLSPEEDY] *= -1
    
    return info # returning the updated list

def ballIsClicked(info, mx, my):    # a def statement defining what happens when you click within the radius of the ball 
    
    if mx >= info[BALLX] - radiusOFball and mx <= info[BALLX] + radiusOFball:
        if my >= info[BALLY] - radiusOFball and my <= info[BALLY] + radiusOFball:
            return True
    
    return False 

def drawScreen(score):  # a def statement that sets up the score each time you click the ball
    text = FONT.render(str(score), 1, (255,255, 255))	# score is set up at the top right
    screen.blit(text, Rect(550,10,200,100))
    

def drawBall(info): # sends a ball to be displayed
    draw.circle(screen, info[COLOUR], (info[BALLX], info[BALLY]), radiusOFball) # describes various attributes of the ball 
    
    



# -------------------------- TITLE SCREEN ---------------------------------

#loads image of the drake background in the main menu
bg = image.load("drakebackground.png")
   
def mainmenu(screen):
    drake = Rect(0,0,600,600) # displays image that was uploaded
    screen.blit(bg, drake) 
              
    draw.rect(screen, WHITE,(150, 125, 330, 100))  # creates a box and text for the start button   on main menu
    text = FONT3.render("Start Program" , 1, (RED))	
    screen.blit(text, Rect(175,150,400,100))
   
    
    draw.rect(screen, WHITE,(150, 275, 330, 100))  # creatse a box and text for the instructions button on main menu
    text1 = FONT3.render("Instructions" , 1, (RED))	
    screen.blit(text1, Rect(175,300,400,100)) 

    
    draw.rect(screen, WHITE,(150, 425, 330, 100))  # creates a box and text for the quit game button on main menu
    text2 = FONT3.render("Exit Game" , 1, (RED))
    screen.blit(text2, Rect(200,450,400,100)) 



    display.flip() # displays image

def instructions(screen):        
    draw.rect(screen, RED,(150, 125, 330, 400)) # creates red box for the intructions menu

    # following lines displays text for the intructions screen with given positions
    text = FONT.render("Oh no! Viruses have taken", 1, WHITE)
    screen.blit(text, Rect(160, 125, 100, 400)) 
    text = FONT.render("over Drake's computer!", 1, WHITE) 
    screen.blit(text, Rect(160, 150, 100, 400))
    text = FONT.render("He needs your help", 1, WHITE) 
    screen.blit(text, Rect(160, 175, 100, 400))
    text = FONT.render("getting rid of them.", 1, WHITE) 
    screen.blit(text, Rect(160, 200, 100, 400))
    
    text = FONT.render("Click on the red viruses to get", 1, WHITE)
    screen.blit(text, Rect(160, 255, 100, 400))
    text = FONT.render("rid of them. Be aware,", 1, WHITE) 
    screen.blit(text, Rect(160, 275, 100, 400))
    text = FONT.render("You only have one min.", 1, WHITE) 
    screen.blit(text, Rect(160, 295, 100, 400))
    text = FONT.render("to get rid of as much as", 1, WHITE)
    screen.blit(text, Rect(160, 315, 100, 400))
    text = FONT.render("you can. If you click", 1, WHITE) 
    screen.blit(text, Rect(160, 335, 100, 400))
    text = FONT.render("the yellow viruses, your", 1, WHITE)
    screen.blit(text, Rect(160, 355, 100, 400))
    text = FONT.render("score will be 0! ", 1, WHITE)
    screen.blit(text, Rect(160, 375, 100, 400)) 
    text = FONT.render("Good luck!", 1, WHITE)
    screen.blit(text, Rect(160, 395, 100, 400))     
    
    
    
    text = FONT.render("Use right click to go", 1, WHITE) 
    screen.blit(text, Rect(160, 455, 100, 400))
    text = FONT.render("back to the main menu.", 1, WHITE) 
    screen.blit(text, Rect(160, 485, 100, 400))

    display.flip()
    
background_list = [] # creates empty list for background
for i in range(50):  # creates a range for the moving star background to be displayed
    x = random.randrange(0, 600)
    y = random.randrange(0, 600)
    background_list.append([x,y])
     
    
    

myClock = time.Clock() # for controlling the frames per second

balls = [] # creates an empty list for ball
score = 0 # score is set as 0 in the beginning


clock = pygame.time.Clock() # for controlling the frames per second on another loop

font = pygame.font.Font(None, 25) # a font is once again uploaded for the timer
 
 
# following lines are for the timer so that it can display minutes:seconds 
frameCount = 0
frameRate = 60
startTime = 60

for i in range(0,10): 
    balls.append(initBall()) # initializing the ball



x,y = mouse.get_pos() # gets mouse position

gameover = image.load("drakegameover.png") 


state = 0   # the main menu is set at 0 
mx = my = 0 # defines mouse positions as 0
running = True


# ------------------------------------------------------ GAME LOOP --------------------------------------------
while running:
    button = 0
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN: # check all events that happen when mouse button is clicked
            mx, my = evnt.pos          
            button = evnt.button
            
            
           
# --------------------------- Main Menu -------------------------------------------           
            # the following lines are set so mouse position can click only the in between the main menu boxes drawn
    if state == 0:
        if mx > 150 and mx < 480 and my > 125 and my < 225:
            state = 1   # when the first box is clicked, state changes to start program screen
        elif mx > 150 and mx < 480 and my > 275 and my < 375:
            state = 2   # when second box is clicked, state changes to the change instructions screen     
        elif mx > 150 and mx < 480 and my > 425 and my < 525:
            state = 3 # when third box is clicked, the screen exits
        else:
            state = 0 # if clicked anywhere outside of the box, the main menu will still be displayed and nothing will happen 
# --------------------------------- START PROGRAM ---------------------------------                   
    elif state == 1: # following lines describe what happens when start button is clicked
        if button==1:     
            for i in range(20): # the bullet above drakes head on the cursor is displaeyed in an ongoing loop   
                bullet = draw.circle(screen,GREEN,(mx+15,my-i), 2)
                pygame.display.flip()         
            for ball1 in balls: # describes what happens when red ball is clicked
                if ballIsClicked(ball1, mx, my) and ball1[COLOUR] == RED:
                    balls[balls.index(ball1)] = initBall() # initliazes the ball
                    score += 1 # score goes up by one
                    break # breaks the loop, the ball will disappear
                if ballIsClicked (ball1, mx, my) and ball1[COLOUR] == YELLOW:
                    balls[balls.index(ball1)] = initBall() 
                    score = 0 # score automatically turns 0
                    break # breaks the loop, the yellow ball will disappear
                            
    
        screen.fill(BLACK)
           
        # ------------------- Background -----------------------------
        for i in range(len(background_list)):
            pygame.draw.circle(screen, WHITE, background_list[i], 2) # displays little white dots in the moving background
            background_list[i][1] += 1 # counts up by one each time
      
            if background_list[i][1] > 600: # defines what happens when the list goes to 600
                y = random.randrange(-50, -10) 
                background_list[i][1] = y
                x = random.randrange(0, 600)
                background_list[i][0] = x
                
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1] 
      
        myClock.tick(60) # waits long enough to have 60 frames per second

          
                
    elif state == 2: #instructions screen is displayed
        if button == 3:# by clicking the right mouse, you can go back where state will be 0 again (the main menu) 
            state = 0 
             
                                    

    if state == 0: # when state equals 0, the main menu will be displayed
        mainmenu(screen)
    
    elif state == 1: 
        drawScreen(score) # displays the balls moving
           
        for i in range(0,len(balls)): # repeats the cycle of the ongoing balls
            drawBall(balls[i])
            balls[i] = moveBall(balls[i])
            
        # ------------------------ Timer ----------------------------- 
        total_seconds = startTime - (frameCount // frameRate)
        
        if total_seconds < 0:
            total_seconds = 0
     
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use (remainder) to get seconds
        seconds = total_seconds % 60
     
        # use python string formatting to format in leading zeros
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
     
        # blit to the screen
        text = FONT.render(output_string, True, WHITE)
        screen.blit(text, [10, 15])
    
        frameCount += 1
        # limit frames per second
        clock.tick(frameRate)  
        
        if total_seconds == 0: # when the timer runs out, the game over screen will be displayed
                       
            blackscreen = pygame.draw.rect(screen, BLACK, (0,0,600,600)) 
            drakegameover = Rect(0,0,600,600)
            screen.blit(gameover, drakegameover)      # uploads game over screen with score being displayed           	
            text = FONT.render(str(score), 1, (255,255, 255))	
            screen.blit(text, Rect(300,250,400,400)) 
            
            display.flip()
            
        mousefigure(screen, x, y) # displays the cursor in the start button         
        display.flip()

        
    
    elif state == 2: # when state equals 2, the instructions screen will be displayed
        instructions(screen)
        
    elif state == 3: # the quit box is set to end the game 
        running == False # everything stops working when quit is clicked 
        quit()


quit() # quits when the x button on the window is clicked

