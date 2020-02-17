# Functions

# Initialize modules the first thing as program won't work otherwise
import pygame
import random
import time
pygame.init()

# MAIN FUNCTIONS: Flowchart format

# Displays the mainmenu image and based on the user click determines what to do.
def displaymenu(prevscreen):

    # This determines whether displaymenu needs to start music again or not. It also means that user
    # has already played and won / exitted so the tokens need to be reset.
    if prevscreen == "play":
        # Plays music
        pygame.mixer.music.load("can't.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        # Resets all token to starting position - Line: 840
        resettokens()

    # Starts a while loop so that the program is constantly looking for user clicks / interaction.
    while True:

        # Displays menu image and updates program.
        screen.blit(menu, (0, 0))
        pygame.display.update()
        
        # Gets the mouse clicks using the getmouseclicks function - Line: 61
        clickx, clicky = getmouseclicks("menu", None)

        # Checks if the click is in the co-ordinates of play:
        if clickx >= 185 and clickx <= 413:
            if clicky >= 255 and clicky <= 350:
                # If yes changes screen to the ludobackground using changescreens - Line: 578
                changescreens(menu, ludobackground, 300, 400)
                # Then proceeds to set up the game by setting up tokens and dice - Line: 124
                setupgame(True, None)

        # Checks if the click is in the co-ordinates of rules:
        if clickx >= 155 and clickx <= 443:
            if clicky >= 370 and clicky <= 460:
                # If yes changes screen to rules using changescreens - Line: 578
                changescreens(menu, rulesimage, 300, 400)
                # Calls rules function using rules - Line: 98
                rules("menu", None, True)

        # Checks if the click is in the co-ordinates of quit.
        if clickx >= 185 and clickx <= 410:
            if clicky >= 485 and clicky <= 580:
                # Confirms if they want to quit using quitmessage - Line: 657
                booleanforquit = quitmessage(largequitimage, "menu", None)
                # The quitmessage function returns whether the user wants to quit (T) or no (F):
                if booleanforquit == True:
                    # If yes, it ends the game and closes the window.
                    pygame.quit()
                    exit()

# Gets the x and y co-ordinates of the pointer every time the mouse is clicked.
def getmouseclicks(prevscreen, roll):
    # Introduces a while loops so keeps getting events done by user.
    while True:
        # Initializes event using a pygame method.
        for event in pygame.event.get():
            # If there was a mouse click:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Plays the sound of a mouseclick - to let user know about their click.
                pygame.mixer.Sound.play(mouseclicksound)
                # Uses a pygame method to get the x and y co-ordinates of the click.
                clickx, clicky = pygame.mouse.get_pos()
                # returns the the x and y clicks.
                return clickx, clicky

            # If the event was the user clicking top left
            elif event.type == pygame.QUIT:
                # Plays the sound of a mouseclick - to let user know about their click.
                pygame.mixer.Sound.play(mouseclicksound)
                # Uses a pygame method to get the x and y co-ordinates of the click.
                clickx, clicky = pygame.mouse.get_pos()
                # If quit was called during the game:
                if prevscreen == "play":
                    # If yes, confirms whether the user is sure using the quitimage as the message - Line: 657
                    booleanforquit = quitmessage(quitimage, prevscreen, roll)
                
                else:
                    # If no, then it must come so shows the quitmessage with largequitimage as the
                    # message - Line: 657
                    booleanforquit = quitmessage(largequitimage, prevscreen, roll)

                # If user chooses Yes to quit then the quitmessage will return True and in that case:
                if booleanforquit == True:
                    # End the program.
                    pygame.quit()
                    exit()

# If user chooses 'Rules' from main menu or the bottom menu during the game, this displays 
# the rules and then returns to the menu or game upon clicking 'Back'.
def rules(prevscreen, roll, alreadymoved):
    while True:
        # If called from play then:
        if prevscreen != "menu":
            # Plays the music as if it came from meny music is already playing.
            pygame.mixer.music.load("can't.mp3")
            pygame.mixer.music.play(-1)
    
        # Gets mouse clicks from the user using getmouseclicks - Line: 61
        clickx, clicky = getmouseclicks("rules", None)
        
        # If the 'Back' option is clicked:
        if clickx >= 17 and clickx <= 118:
            if clicky >= 13 and clicky <= 67:
                
                # Sends the user back to where they came from:
                if prevscreen == "menu":
                    # Changes screens - Line: 578, and Displays menu - Line: 11
                    changescreens(rulesimage, menu, 300, 400)
                    displaymenu("rules")
                else:
                    # Set's up the game again using setupgame - Line: 124
                    setupgame(alreadymoved, roll)

# If user clicks, 'Play' from main menu or 'Back' from rules, this blits (displays) all
# the pieces of the game back where they were or restarts if a new game.
def setupgame(alreadymoved, roll):
    while True:
        # Stops music
        pygame.mixer.music.stop()

        # Shows the ludo board as well the bottom menu image.
        screen.blit(ludobackground, (0, 0))
        screen.blit(bottom, (0, 600))

        # Blits all 16 tokens to their position
        for x in range(len(alltoken)):
            screen.blit(alltoken[x], (allroutes[x // 4][alltokenpos[x]]))

        # Blits the star at red's corner
        screen.blit(star, (starroute[starpos]))
        # Blits the rollimage
        screen.blit(dice, (256, 256))
        
        # Updates pygame
        pygame.display.update()
    
        while True:
            # Once all necessary images are set the game begins by calling playgame - Line: 151
            playgame(alreadymoved, roll)

# This function is called after the game is set up and ready for the user to play.
def playgame(alreadymoved, roll):
    # Makes turnpos a global variable.
    global turnpos

    # Roll is not displayed to the user right now.
    rolldisplay = False

    while True:
        # Gets mouse clicks - Line: 209
        clickx, clicky = bottommenu(roll, alreadymoved)

        # If roll is not displayed:
        if rolldisplay == False:
            # See if they clicked on the rollimage
            if clickx >= 223 and clickx <= 343:
                if clicky >= 223 and clicky <= 343:
                    # If yes, calls Dice() to roll dice - Line: 250
                    roll, rollimage = Dice(alreadymoved, roll)
                    # Roll is shown so rolldisplay = True and token has not moved, 
                    # so alreadymoved = False
                    rolldisplay = True
                    alreadymoved = False


        else:
            # If roll is already displayed then based on whose turn it is, figures out
            # whether the user clicked on any of that teams tokens or not - Line: 270
            boolean, token = getsquare(clickx, clicky, turnpos)
            if boolean == True:
                # If true, returns token and checks if moving it would cause a token to 
                # step on another - Line: 297
                samecolourstepping, steppedon = checkdoubles(token, roll)
                # If it's not stepping on it's own token:
                if samecolourstepping == False:
                    # Changes position of token - Line: 411
                    changepos(token, roll, rollimage)
                    # Appends to Tracking Doc what token was moved by the user - Line: 865
                    index = alltoken.index(token)
                    appendtodoc("token: ", index, alltokenstr)
                    # As token is moved and roll is not displayed for the next round.
                    alreadymoved = True                    
                    rolldisplay = False

                    # If roll is 6 or the user stepped on another users token the turn doesn't change
                    # it stays the same.
                    if roll == 6 or steppedon ==  True:
                        pass

                    else:
                        # Moves star to appropriate corner - Line: 598
                        newstarpos = movestar()
                        # If it was last players turn it starts over at first or increases by 1.
                        if turnpos == 3:
                            turnpos = 0
                        else:
                            turnpos += 1

# This function is called in the previous function to show the menu at the botton while game
# is being played.
def bottommenu(rolls, alreadymoved):
    # Gets mouse click - Line: 61
    clickx, clicky = getmouseclicks("play", rolls)

    # If the cilck is in the co-ordinates of 'Menu':
    if clickx >= 43 and clickx <= 180.5:
        if clicky >= 637.5 and clicky <= 697:
            # Asks for quitmessage - Line: 657
            booleanforsure = quitmessage(menureturnimage, "play", rolls)
            if booleanforsure == True:
                # If user wants to go to menu, changes sreens - Line: 578, resets all tokens - Line: 840, 
                # And Displays menu again by calling displaymenu again - Line: 11
                changescreens(bottom, menu, 300, 400)
                resettokens()
                displaymenu("play")

    # If user click is in the co-ordinates of 'Rules':
    elif clickx >= 231 and clickx <= 369.75:
        if clicky >= 637.5 and clicky <= 697:
            # Changes screens to rules using changescreens - Line: 578
            changescreens(ludobackground, rulesimage, 300, 400)
            # Calls the rules function to show the rules - Line: 98
            rules("play", rolls, alreadymoved)
            
    else:
        # User has clicked 'Quit'
        if clickx >= 424 and clickx <= 545:
            if clicky >= 637.5 and clicky <= 697:
                # Shows quitmessage and asks if they are sure to quit - Line: 657
                booleanforquit = quitmessage(quitimage, "play", rolls)
                # If user is sure:
                if booleanforquit == True:
                    # End the program
                    pygame.quit()
                    exit()

    # If neither one was clicked returns the x and y click co-ordinates.
    return clickx, clicky

# This function is called in playgame() and it generates a random roll and displays the corresponding
# roll image.
def Dice(alreadymoved, roll):
    # If the token is already moved, then produces a new roll or else sticks to the old roll.
    if alreadymoved == True:
        # Creates a random roll and appends the roll to the Tracking Doc - Line: 865
        roll = random.randint(1, 6)
        appendtodoc("roll: ", (roll - 1), allroll)

    # Based on the roll, figures out what rollimage to use to show the user their roll
    for x in range(1, len(dicelist) + 1):
        if roll == x:
            screen.blit(dicelist[x - 1], (256, 256))
            # Once figured out, assigns that image to the variable - rollimage
            rollimage = dicelist[x - 1]
            # Updates pygame
            pygame.display.update()
            # Returns the roll and the rollimage
            return roll, rollimage

# A function that gets the square co-ordinates a user must click within during a particular 
# colours turn. It gets the current click and the turnpos which lets the function know whose
# turn it is.
def getsquare(clickx, clicky, turnpos):
    # Based on the click and the turnpos, thsi function only loops through the 4 tokens
    # the user is allowed to click.
    for x in range(len(alltoken[(turnpos * 4) : ((turnpos + 1) * 4)])):
        # Gets tokenpos - Line: 641
        tokenpos = tokentopos(alltoken[x + (4 * turnpos)])
        # Gets route of the token - Line: 628
        route = getroute(alltoken[x + (4 * turnpos)])
        coordinates = route[tokenpos]
        xmin = coordinates[0]
        # The width of our iamge is 40
        xmax = xmin + 40
        ymin = coordinates[1]
        # THe height of our iamge is 40
        ymax = ymin + 40

        if clickx >= xmin and clickx <= xmax:
            if clicky >= ymin and clicky <= ymax:
                # If it was clicked on one of those, return T for moving it and what token was clicked.
                return True, alltoken[x + (4 * turnpos)]

    # If none of them were clicked then return F for moving and token is None/
    return False, None 

# Before the next function is called which moves the token, this function is called in playgame()
# in order to check whether a token is stepping on their own token or another teams'.
# NOTE: First value it returns is whether or not a token stepped on a token of its own colour, and the 
      # second value is whether or not it stepped on someone else's token.
def checkdoubles(token, rolls):
    tokenpos = tokentopos(token) # Line: 641
    route = getroute(token) # Line: 628

    # Finds new index. If the first three tokens then they need to go to index 3 first and then move
    # the rolls/
    for x in range(3):
        if tokenpos == x:
            valuetobeadded = 3 - x
            tokenpos += valuetobeadded

    # Adds their current position to rolls
    newindex = tokenpos + rolls

    # If new index is smaller than the route, it is not a homescore.
    if newindex < len(route):
        # New values is the current co-ordinates
        newvalues = route[newindex]
        
        # Checks through every token and their value to see if the new place would be the same as any tokens
        # current position.
        for x in range(len(alltoken)):
            test = alltoken[x]
            testpos = tokentopos(test) # Line: 641
            testroute = getroute(test) # Line: 628
            alreadythere = testroute[testpos] # Current values of the test token
    
            # If they new value will be the same as a tokens current value:
            if alreadythere == newvalues:
                if test != token:
                    # If their routes are same then its same colour:
                    if testroute == route:
                        # Plays error sound.
                        pygame.mixer.Sound.play(steponownsound)
                        # Displays a popup that shows the user an error - Line: 738
                        displaypopup(False, ownstep, rolls, None)
                        # Returns True for same colour stepping and False for stepping on another colour's token.
                        return True, False
    
                    # If their routes are different then it's not stepping on a token of it's own colour.
                    else:
                        # Colour 1 is the beater and Colour 2 is the one being beaten
                        colour1 = allroutes.index(route)
                        colour2 = allroutes.index(testroute)
                        # This determines what image needs to be used for the popup - Line: 802
                        image = steppingimage(turn[colour1], turn[colour2]) 

                        # Plays beating / stepping on sound.
                        pygame.mixer.Sound.play(steppedonsound)
                        # Displays pop up - Line: 738
                        displaypopup(False, image, rolls, None)
                        # Changes the position of the token back to its original value - Line: 365
                        changesteppingpos(test, testroute)
                        # Returns False for samecolourstepping and True for stepped on.
                        return False, True
        
        # If no values were similar to the new values of the token, then both samecolourstepping
        # and stepped is False
        return False, False

    else:
        # If it will be a homescore (tokenpos is longer than the len of it's route) then returns False for both.
        return False, False

# If a colour steps on another token, then it changes the position of the token and send its back to 
# its original position it had at the beginning of the game.
def changesteppingpos(test, route):
    testpos = tokentopos(test) # Line: 641

    # Gets the center co-ordinates od the token using getcenter - Line: 707
    centerx, centery = getcenter(test)
    # Gets rectangle co-ordinates using pygame method
    position = test.get_rect(center = (centerx, centery))
    screen.blit(test, position)
    pygame.display.update()
    
    # Puts background over where the image used to be.
    screen.blit(ludobackground, position, position)
    # Gets the x and y change, the token needs to move from get stepped on - Line: 391
    x_change, y_change, originalindex = getsteppedon(test)
    # Moves it.
    position = position.move(x_change, y_change)
    screen.blit(test, position)
    pygame.display.update()

    # Changes the tokens position aka the tokenpos
    for x in range(len(alltoken)):
        if test == alltoken[x]:
            alltokenpos[x] = originalindex

# In order to move it back fromn it's current position to it's original position, this function helps
# determine the x and y change.
def getsteppedon(token):
    route = getroute(token) # Line: 628
    tokenpos = tokentopos(token) # Line: 641
    currentposition = route[tokenpos]

    # Tells what quarter the token is in. 
    position = alltoken.index(token)
    # As we know that every colour had 4, you find out its original index by % 4.
    originalposition = position % 4
    # New co-ordinates
    newposition = route[originalposition]

    # Calculates the x and y change
    x_change = newposition[0] - currentposition[0]
    y_change = newposition[1] - currentposition[1]

    return x_change, y_change, originalposition

# Based on the dice rolled and after confirming that it is not stepping on any token this function erased
# the old image, figures out where the new one would be, and how much to move it in the x and y direction
# to make it re-appear at the right spot. It also changes the token's position after it is moved.
def changepos(token, rolls, rollimage):
    route = getroute(token) # Line: 628
    centerx, centery = getcenter(token) # Line: 707
    position = token.get_rect(center = (centerx, centery))
    screen.blit(token, position)
    tokenpos = tokentopos(token) # Line: 641
    pygame.display.update()
    
    # Displays background where once there used to be the token.
    screen.blit(ludobackground, position, position)
    # Calculates the x and y change, tells the new co-ordinates token is at and whether or not
    # the token reached home or not - Line: 455
    booleanforhome, x_change, y_change, currentpositions = slopechange(token, route, rolls)

    # If it hasn't reached home:
    if booleanforhome == False:
        # Moves it to it's new position
        position = position.move(x_change, y_change)
        screen.blit(token, position)
        pygame.display.update()
            
    # Regardless, of it has gone to home or not:
    for x in range(len(alltokenpos)):
        # Finds the token from alltoken list
        if token == alltoken[x]:
            # Makes sure it is not at home
            if booleanforhome == False:
                # If yes, new index is the current + rolls
                newindex = currentpositions + rolls
                # Updates the tokenpos
                alltokenpos[x] = newindex
            else:
                # If at home, new index is % 4 as it tells what index it was originally at
                # at the beginning of the game.
                originalindex = (alltokenpos.index(tokenpos) % 4)
                # Updates it 
                alltokenpos[x] = originalindex
        
    # Removed the dice image - Line: 490
    removerollimage(rollimage)

# This function is called in the previous function to identify the x and y change that the token needs
# to go through in order for it to go from current position to new position based on the roll.
def slopechange(token, route, rolls):
    tokenpos = tokentopos(token) # Line: 641
    oldvalues = route[tokenpos]

    # If the token is not star:
    if route != starroute:
        for x in range(3):
            # Checks if the token is at the first three home spaces, it needs to reach index 3 before you
            # add rolls to it as otherwise it will go from one home space to another.
            if tokenpos == x:
                # If yes, add the difference between current index and three.
                valuetobeadded = 3 - x
                tokenpos += valuetobeadded

    # If the token is star then, once it finishes green (4th colours) turn, this moves it back to
    # the first index (aka at reds corner again.)
    elif starpos == 3:
        rolls = -3
    
    # Checks if the new index will be longer than the number of values in the route:
    if (tokenpos + rolls) >= len(route):
        # If yes, then calls homescore as this shows that the token went home.
        homescore(token, rolls) # Line: 503
        return True, None, None, None
    
    else:
        # If no, the finds the newvalues and does x2 - x1 and y2 - y1 to find x and y change.
        newvalues = route[tokenpos + rolls]
        x_change = newvalues[0] - oldvalues[0]
        y_change = newvalues[1] - oldvalues[1]
        
        return False, x_change, y_change, tokenpos

# After the token is moved, this function is called in playgame() to remove the dice image so the user
# click on the dice to roll image.
def removerollimage(rollimage):
    # Gets rectangle co-ordinates
    position = rollimage.get_rect(center = (301, 301))
    screen.blit(rollimage, position)
    pygame.display.update()

    # Shows the ludo background and then the diceimage on top of that.
    screen.blit(ludobackground, position, position)
    screen.blit(dice, (256, 256))
    pygame.display.update()

# Every time change pos is called and the new index value for the token is larger then the length of it's 
# route (which means it's at home) it will call homescore() indicate that a token got a home point.
def homescore(token, rolls):
    route = getroute(token) # Line: 628
    centerx, centery = getcenter(token) # Line: 707
    position = token.get_rect(center = (centerx, centery)) # Rectangle co-ordinates
    screen.blit(token, position)
    pygame.display.update()
    tokenpos = tokentopos(token) # Line: 641

    # Removes token by showing the background on top of it.
    screen.blit(ludobackground, position, position)
    pygame.display.update()

    # Figures out what team got a token
    index = (alltoken.index(token) // 4)
    # Adds one to their index in the number of home token list
    teamhometokens[index] += 1

    # Calls displayscore to show the user they got a token at home - Line: 548
    displayscore(teamhometokens[index], token)

    # Figues out what message to display
    for x in range(len(teamhometokens)):
        if token == alltoken[x]:
            index = (alltoken.index(token)) // 4
            # Based on which team won displays appropriate message from the list of all homescore messages.
            message = allhomescores[index]
            # Plays the sound of user getting a token at home.
            pygame.mixer.Sound.play(tokenhomesound)
            # Displays the popup - Line: 738
            displaypopup(False, message, rolls, token)
    
    # Checks if any player now has 4 at home.
    for winningteam in range(len(teamhometokens)):
        if teamhometokens[winningteam] == 4:
            # If yes, then plays the sound of a player winning.
            pygame.mixer.Sound.play(winsound)
            # Displays the winning image - Line: 823
            displaywinningimage(winningteam)
            # Changes the screen back to the menuimage - Line: 578
            changescreens(ludobackground, menu, 300, 400)
            # Calls display menu to start the game all over again - Line: 11
            displaymenu("play")

# This function let's the user know how many of their tokens have reached home. The counter only appears after 
# one token enters home. Later, based on how many tokens they get, the counter updates.
def displayscore(numberoftokens, token):
    route = getroute(token) # Line: 628
    routeindex = allroutes.index(route) # gets what route it is and also what colour got a token at home.
    image = hometokenscoreimg[numberoftokens - 1] # Figues ourt image to display
    imagepos = (showhometokens[routeindex]) # And where would it be blitted

    # If its their first one you only need to blit it, so it does that
    if numberoftokens == 1:
        screen.blit(image, imagepos)

    # If not, then this removes the old image and displays new one.
    else:
        previmage = hometokenscoreimg[numberoftokens - 2]
        # Current x and y
        currentx = imagepos[0]
        currenty = imagepos[1]

        # Center co-ordinates of the current x and y. You add 13 to x as width is 26 and add 20 tp y as height is 40.
        centerx = currentx + 13
        centery = currenty + 20
        
        position = previmage.get_rect(center = (centerx, centery))
        screen.blit(ludobackground, position, position) # Shows background
        screen.blit(image, imagepos) # And then the new image
        pygame.display.update() # Updates the screen.

# EXTRA FUNCTIONS: Functions that are needed to make the game better and Main Functions work.

# Everytime the user wants to switch from either menu, rules, or play to any one of the other ones
# this function is called which basically displays the new screen.
def changescreens(oldimage, newimage, centerx, centery):
    # Blits the new image on top of it
    screen.blit(newimage, (0, 0))
    position = oldimage.get_rect(center = (centerx, centery))
    # Then removes the old one.
    screen.blit(oldimage, position)
    pygame.display.update()
    # And blits the new one again
    screen.blit(newimage, position, position)

    # If the new image is the ludobackground
    if newimage == ludobackground:
        # Then it also displays the bottom menu image under the board
        screen.blit(bottom, (0, 600))

    # Updates the screen
    pygame.display.update()

# This function is used to move the star which indicates to the user what colour's turn it is. It 
# removes old star, finds slopechange and also displays it at the new place..
def movestar():
    # Makes variable starpos global so any changes made in the function to this variable are global
    global starpos

    centerx, centery = getcenter(star) # Line: 707
    position = star.get_rect(center = (centerx, centery))
    screen.blit(star, position)

    # Removes the star and display the background on top of it
    screen.blit(ludobackground, position, position)

    # Finds the new co-ordinates it needs to be at
    coordinates = starroute[starpos]
    # Calculates the slope change to move the star - Line: 455
    booleanforhome, x_change, y_change, currentpositions = slopechange(star, starroute, 1)
    # Moves the image
    position = position.move(x_change, y_change)
    screen.blit(star, position)
    pygame.display.update() # Updates the screen

    # If star is at green, for the next time it needs to go back to red
    if starpos == 3:
        starpos = 0

    # If anywhere else, for next time it needs to go to the next one
    else:
        starpos += 1

# A useful function as it will return the route that the token sent in the parameter uses.
def getroute(token):
    for x in range(len(alltoken)):
        # Finds where is the token in alltoken list
        if token == alltoken[x]:
            # Does integer division to find what quarter of the list is it in
            index = x // 4
            # As our list is in groups of 4 with each group being a diff. colour we know what
            # colour it uses and the all routes list is corresponding order so finds the route for
            # that colour.
            route = allroutes[index]
            return route

# Based on the token given this functions' parameter, it determines what the position of token is in
# respective route.
def tokentopos(token):
    if token in alltoken:
        for x in range(len(alltoken)):
                # Finds the index of token in alltoken list
                index = alltoken.index(token)
                # As alltoken and alltokenpos go hand in hand, the position of that token is at the same index in 
                # the alltokenpos list.
                tokenpos = alltokenpos[index]
                return tokenpos

    # If token is not a colours piece and is a star instead then returns the starpos
    else:
        return starpos

# Anytime during the game, the user clicks on the quit from the menu / bottommenu or the window 
# was closed, this function is called which displays a message asking the user whether they are sure, 
# and based on their click (yes / no), it returns back to the screen it was pressed on / ends the 
# program.
def quitmessage(message, prevscreen, rolls):
    while True:
        # If comes from play shows a smaller message at a different place than if coming from 
        # Rules or Menu
        if prevscreen == "play":
            screen.blit(message, (163, 243))
        
        else:
            screen.blit(message, (50, 280))

        pygame.display.update() # Updates

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If user has clicked on the screen, gets the co-ordinates of the click
                clickx, clicky = pygame.mouse.get_pos()
                # If during play:
                if prevscreen == "play":
                    # It looks if in the square where Yes is on the screen if yes returns True,
                    if clickx >= 248 and clickx <= 287 and clicky >= 315.5 and clicky <= 335:
                        return True

                    # If clicked in the square co-ordinates where no is displayed:
                    elif clickx >= 319 and clickx <= 348.5 and clicky >= 315.5 and clicky <= 335:
                        # Removes popup which is called in displaypopup and returns False - Line: 738
                        displaypopup(True, message, rolls, None)
                        return False

                # If coming from Menu or Rules
                else:
                    # Sees if its in the co-ordinates where Yes is displayed then returns True
                    if clickx >= 205 and clickx <= 271 and clicky >= 407 and clicky <= 443:
                        return True
        
                    # If clicked in the square co-ordinates where no is displayed:
                    elif clickx >= 327 and clickx <= 383 and clicky >= 407 and clicky <= 443:
                        # If it is from Menu takes it back to menu by changing screens and if it was
                        # called from Rules then takes it back to Rules - Line: 
                        if prevscreen == "menu":
                            changescreens(largequitimage, menu, 300, 387)
                        else:
                            changescreens(largequitimage, rulesimage, 300, 307)

                        # Returns False
                        return False

# An important function needed everytime an image needs to be removed. Images in pygame need to be specified
# by their center co-ordinates when they need to be removed which means every time a token is moved / removed,
# this function is called to know the current center co-ordinates of the token.
def getcenter(token):
    if token in alltoken:
        # If it's a colours piece then finds its position and route to know current co-ordinates
        for x in range(len(alltoken)):
            tokenpos = tokentopos(token) # Line: 
            route = getroute(token) # Line: 628

            # Current co-ordinates
            currentx = route[tokenpos][0]
            currenty = route[tokenpos][1]

            # What the center values would be. You add 18 as our image is 36 by 36 so you add half of it to get center.
            centerx = currentx + 18
            centery = currenty + 18

            return centerx, centery

    # If token is star then finds the current position it is at.
    elif token == star:
        currentx = starroute[starpos][0]
        currenty = starroute[starpos][1]

        # And then the center co-ordinates, width is 45 so you add half to x and height is 42 so you add half to y.
        centerx = currentx + 22.5 
        centery = currenty + 21

        return centerx, centery

# Everytime there needs to be a message displayed to the user this function is called to blit the message.
def displaypopup(alreadydisplayed, message, rolls, tokenmoved):
    # Pop-up needs to be displayed so True
    popup = True
    while popup == True:
        # If it is not already displayed before the function was called:
        if alreadydisplayed == False:
            # Display the popup message and update.
            screen.blit(message, (163, 243))
            pygame.display.update()
            
            # Waits for a user click and then calls remove popup and breaks while loop - Line: 761
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    removepopup(message, rolls, tokenmoved)
                    popup = False

        # If it is already displayed before the function was called then:
        else:
            # Removes the popup and breaks the while loop - Line: 761
            removepopup(message, rolls, tokenmoved)
            popup = False

# Once the message has been displayed, the program waits for a mouse click and then proceeds,
# to call this function to remove the pop-up.
def removepopup(message, rolls, tokenmoved):
    position = message.get_rect(center = (303, 303)) # Get rectanlge co-ordinates
    screen.blit(ludobackground, position, position) # Shows background again
    pygame.display.update()
    
    # Rolls equal none means that the dice was rolled already so diceimage needs to be blitted.    
    if rolls == None:
        screen.blit(dice, (256, 256))

    # If rolls has a value:
    else:
        # Figures out the image of the roll and displays it and updates screens.
        currentroll = dicelist[rolls - 1]
        screen.blit(currentroll, (256, 256))
        pygame.display.update()

    # Checks if any token is in the co-ordinates where the popup was displayed
    for x in range(len(alltoken)):
        token = alltoken[x]
        tokenpos = tokentopos(token)
        route = getroute(token) # Line: 628
        # any token is in the list that contains the positions the popup covers then:
        if route[tokenpos] in postobeblitted:
            # Sees if the message is a token going to home or a colour wins:
            if message in allhomescores or message in winningimg:
                # Sees if the token moved is the token that's in those co-ordinates
                if token == tokenmoved:
                    # If yes, do nothing.
                    pass
                else:
                    # Else display the token again right where it was.
                    screen.blit(token, (route[tokenpos]))
            else:
                # If in the list to be blitted then, display the token again where it was.
                screen.blit(token, (route[tokenpos]))
        
        # Updates the screen.
        pygame.display.update()

# Every time a token is stepped on and there are about 12 possibilities so this function figures out which 
# one of the 12 images are to be used to show that a colour beat another and then that iamge is displayed
# using displaypopup().
def steppingimage(colour1, colour2):
    for x in range(4):
        # First figures out who is the beater
        if colour1 == turn[x]:
            for y in range(4):
                # Then finds the token that is being beated
                if colour2 == turn[y]:
                    # Their names combines in strings is their colour + "beats" + the colour
                    string = turn[x] + "beats" + turn[y]
                    # And then finds the str in beatingstr list
                    if string in beatingstr:
                        # As beatingstr and beatingimg are related once you find position of str we know
                        # the position of the image that needs to be displayed
                        stringpos = beatingstr.index(string)
                        image = beatingimg[stringpos]
                        # Returns the image that needs to be displayed
                        return image

# This function is called when the there are 4 tokens at home for a team, and it displays a popup
# as to who won.
def displaywinningimage(pos):
    # Popup needs to be shown
    popup = True
    while popup == True:
        # Blits the popup that shows what team won
        screen.blit(winningimg[pos], (163, 243))
        pygame.display.update()

        # If the user clicks any where we neds popup doesn't need to be displayed anymore and breaks 
        # the while loop.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Once pressed breaks loop
                popup = False

# After a game ends / user clicks menu halfway through a game, this function is called to reset
# all tokens and roll and hometoken counter as well as the star position so that the program is
# ready for a new game.
def resettokens():
    # Makes turnpos and starpos global as well, so every change made, is for the whole program.
    global turnpos
    global starpos

    # This for loop resets all the tokenpos for every token back to their original index
    for y in range(len(alltoken)):
        # Goes through every token finds it's current position
        test = alltoken[y]
        testpos = tokentopos(test) # Line: 
        # Finds its original index and changes it in the list as well
        originalindex = y % 4
        alltokenpos[y] = originalindex
 
    # Resets the team hometoken list for all of them to be zero to get it ready for the next game.
    for z in range(len(teamhometokens)):
        teamhometokens[z] = 0

    # turnpos and starpos are set to 0 as it needs to red turn again, and star needs to be ther as well.
    turnpos = 0
    starpos = 0

# This function is called every time the user rolls the dice, and chooses a token to move. This is used 
# to keep track of the user's every move during any game, and was used to find errors.
def appendtodoc(message, thingtoappend, listgiven):
    # Opens the tracking doc
    trackingdoc = open("Tracking Doc", "a")
    # Writes the str message and then from the list given, add the thingtoappend index value after.
    trackingdoc.write(message + str(listgiven[thingtoappend]) + "\n")
    # Close the tracking doc
    trackingdoc.close()

# LOADING: This section of the code initializes variables for screen size, colours, images and sounds.

# Colour used to fill the screen in the beginning.
white = (0, 0, 0)

# Setting up the screen size
width = 600
height = 750
screen = pygame.display.set_mode((width, height))

# Images:
ludobackground = pygame.image.load(r'Board.jpeg')

# Blue tokens
blue1 = pygame.image.load(r'bluecircle.png')
blue2 = pygame.image.load(r'bluecircle.png')
blue3 = pygame.image.load(r'bluecircle.png')
blue4 = pygame.image.load(r'bluecircle.png')

# Red tokens
red1 = pygame.image.load(r'redcircle.png')
red2 = pygame.image.load(r'redcircle.png')
red3 = pygame.image.load(r'redcircle.png')
red4 = pygame.image.load(r'redcircle.png')

# Yellow tokens
yellow1 = pygame.image.load(r'yellowcircle.png')
yellow2 = pygame.image.load(r'yellowcircle.png')
yellow3 = pygame.image.load(r'yellowcircle.png')
yellow4 = pygame.image.load(r'yellowcircle.png')

# Green tokens
green1 = pygame.image.load(r'greencircle.png')
green2 = pygame.image.load(r'greencircle.png')
green3 = pygame.image.load(r'greencircle.png')
green4 = pygame.image.load(r'greencircle.png')

# Dice image and all the roll images
dice = pygame.image.load(r'roll.png')
roll1 = pygame.image.load(r'1.0.jpg')
roll2 = pygame.image.load(r'2.0.jpg')
roll3 = pygame.image.load(r'3.0.jpg')
roll4 = pygame.image.load(r'4.0.jpg')
roll5 = pygame.image.load(r'5.0.jpg')
roll6 = pygame.image.load(r'6.0.jpg')

# All the winning images for each team
redwin = pygame.image.load(r'redwin.png')
yellowwin = pygame.image.load(r'yellowwin.png')
bluewin = pygame.image.load(r'bluewin.png')
greenwin = pygame.image.load(r'greenwin.png')

# Star image.
star = pygame.image.load(r'star.png')

# All the background images for each screen
menu = pygame.image.load(r'menu.png')
bottom = pygame.image.load(r'bottomimage.png')
rulesimage = pygame.image.load(r'rulesimage.png')

# Beating images (every possibility)
redbeatsyellow = pygame.image.load(r'redyellow.png')
redbeatsblue = pygame.image.load(r'redblue.png')
redbeatsgreen = pygame.image.load(r'redgreen.png')
yellowbeatsred = pygame.image.load(r'yellowred.png')
yellowbeatsblue = pygame.image.load(r'yellowblue.png')
yellowbeatsgreen = pygame.image.load(r'yellowgreen.png')
bluebeatsred = pygame.image.load(r'bluered.png')
bluebeatsyellow = pygame.image.load(r'blueyellow.png')
bluebeatsgreen = pygame.image.load(r'bluegreen.png')
greenbeatsred = pygame.image.load(r'greenred.png')
greenbeatsyellow = pygame.image.load(r'greenyellow.png')
greenbeatsblue = pygame.image.load(r'greenblue.png')

# Error message for when user steps on their own token
ownstep = pygame.image.load(r'ownstep.png')

# Each team gets token home image
redhome = pygame.image.load(r'redhome.png')
yellowhome = pygame.image.load(r'yellowhome.png')
bluehome = pygame.image.load(r'bluehome.png')
greenhome = pygame.image.load(r'greenhome.png')

# Image that asks if they are sure they want to quit / return to menu (has a 'Yes' or 'No' option)
quitimage = pygame.image.load(r'quitimage.png')
largequitimage = pygame.image.load(r'largequitimage.png')
menureturnimage = pygame.image.load(r'menureturn.png')

# Counter images to show the user how many tokens they have at home
one = pygame.image.load(r'1.png')
two = pygame.image.load(r'2.png')
three = pygame.image.load(r'3.png')
four = pygame.image.load(r'4.png')

# Initializes the original positions of each token to be at 0-3 indexes.
red1pos = 0
red2pos = 1
red3pos = 2
red4pos = 3

yellow1pos = 0
yellow2pos = 1
yellow3pos = 2
yellow4pos = 3

blue1pos = 0
blue2pos = 1
blue3pos = 2
blue4pos = 3

green1pos = 0
green2pos = 1
green3pos = 2
green4pos = 3

# Initializes the position star starts at = 0 (red) and the turnpos which tells the program it's red's turn.
starpos = 0
turnpos = 0

# Loads sounds that are used during the game.
steponownsound = pygame.mixer.Sound("steponown.wav")
steppedonsound = pygame.mixer.Sound("steppedon.wav")
tokenhomesound = pygame.mixer.Sound("tokenhome.wav")
winsound = pygame.mixer.Sound("win.wav")
mouseclicksound = pygame.mixer.Sound("mouseclick.wav")

# LISTS

# Routes of tokens of the same colour. i.e. all tokens of the same colour follow the same route which is below.
routered = [[43,43] , [163,43] ,[43,163], [163,163], [43, 243], [83, 243], [123, 243], [163, 243], [203, 243], [243, 203], [243, 163], [243, 123], [243, 83], \
            [243, 43], [243, 3], [283, 3], [323, 3], [323, 43], [323, 83], [323, 123], [323, 163], [323, 203], [363, 243], [403, 243], [443, 243], [483, 243], \
            [523, 243], [563, 243], [563, 283], [563, 323], [523, 323], [483, 323], [443, 323], [403, 323], [363, 323], [323, 363], [323, 403], [323, 443], \
            [323, 483], [323, 523], [323, 563], [283, 563], [243, 563], [243, 523], [243, 483], [243, 443], [243, 403], [243, 363], [203, 323], [163, 323], \
            [123, 323], [83, 323], [43, 323], [3, 323], [3, 283], [43, 283], [83, 283], [123, 283], [163, 283], [203, 283]]

routeyellow = [[403,43], [523,43], [403,163],[523,163],[323, 43], [323, 83], [323, 123], [323, 163], [323, 203], [363, 243], [403, 243], [443, 243], [483, 243], \
               [523, 243], [563, 243], [563, 283], [563, 323], [523, 323], [483, 323], [443, 323],[403, 323], [363, 323], [323, 363], [323, 403], [323, 443], \
               [323, 483], [323, 523], [323, 563], [283, 563], [243, 563], [243, 523], [243, 483], [243, 443], [243, 403], [243, 363], [203, 323], [163, 323], \
               [123, 323],[83, 323], [43, 323], [3, 323], [3, 283], [3, 243], [43, 243], [83, 243], [123, 243], [163, 243], [203, 243], [243, 203], [243, 163], \
               [243, 123], [243, 83], [243, 43], [243, 3], [283, 3], [283, 43], [283, 83], [283,123], [283, 163], [283, 203]]

routeblue = [[403,403],  [523,403],[403,523],  [523,523], [523, 323], [483, 323], [443, 323],[403, 323], [363, 323], [323, 363], [323, 403], [323, 443], [323, 483], \
             [323, 523], [323, 563], [283, 563], [243, 563], [243, 523], [243, 483], [243, 443], [243, 403], [243, 363], [203, 323], [163, 323], [123, 323], \
             [83, 323], [43, 323], [3, 323], [3, 283], [3, 243], [43, 243], [83, 243], [123, 243], [163, 243], [203, 243], [243, 203], [243, 163], [243, 123], \
             [243, 83], [243, 43], [243, 3], [283, 3],[323,3],[323, 43], [323, 83], [323, 123], [323, 163], [323, 203], \
             [363, 243], [403, 243], [443, 243], [483, 243], [523, 243], [563, 243], [563, 283],[523,283],[483,283],[443,283],[403,283],[363,283]]

routegreen = [[43,403],[163,403],[43,523],[163,523],[243, 523], [243, 483], [243, 443], [243, 403], [243, 363], [203, 323], [163, 323], [123, 323], [83, 323], \
              [43, 323], [3, 323], [3, 283], [3, 243], [43, 243], [83, 243], [123, 243], [163, 243], [203, 243], [243, 203], [243, 163], [243, 123], [243, 83], \
              [243, 43], [243, 3], [283, 3],[323,3],[323, 43], [323, 83], [323,123], [323, 163], [323, 203], [363, 243], \
              [403, 243], [443, 243], [483, 243], [523, 243], [563, 243], [563, 283],[563, 323], [523, 323], [483, 323], [443, 323],[403, 323], [363, 323], \
              [323, 363], [323, 403], [323, 443], [323, 483], [323, 523], [323, 563], [283, 563], [283, 523], [283, 483], [283, 443], [283, 403], [283, 363]]

# All routes are in one so that it's easier to access it. Note: It is in order of the turns of player.
allroutes = [routered, routeyellow, routeblue, routegreen]

# This is a list of co-ordinates that are affected by the display of the pop-up message so, if any token is on these co-ordinates, 
# it needs to be blitted again.
postobeblitted = [[163, 243], [203, 243], [163, 283], [203, 283], [163, 323], [203, 323], [363, 243], [403, 243], [363, 283], [403, 283], [363, 323], [403, 323]]

# Order or turns list. 1st - Red, 2nd - Yellow etc...
turn = ["red", "yellow", "blue", "green"]

# The route the star follows with every turn change.
starroute = [[-1, -1], [560, -1], [560, 560], [-1, 560]]

# This list is what determines the winner. It contains how many home tokens does each team have.
teamhometokens = [0, 0, 0, 0]

# List of all tokens (images) along with another list as their variable name typed into a string, as it helps with tracking 
# which token user moved. Lastly, all the tokens position (index) in their route. Note: Every tokenpos is at the same index 
# in the alltokenpos as the co-responding tokens index in alltoken. Ex: yellow1pos is at index 4 in alltokenpos so yellow1 
# (token) is at index 4 in alltoken list.
alltoken = [red1, red2, red3, red4, yellow1, yellow2, yellow3, yellow4, blue1, blue2, blue3, blue4, green1, green2, green3, green4]
alltokenstr = ["red1", "red2", "red3", "red4", "yellow1", "yellow2", "yellow3", "yellow4", "blue1", "blue2", "blue3", "blue4", "green1", "green2", "green3", "green4"]
alltokenpos = [red1pos, red2pos, red3pos, red4pos, yellow1pos, yellow2pos, yellow3pos, yellow4pos, blue1pos, blue2pos, blue3pos, blue4pos, green1pos, green2pos, green3pos, green4pos]

# A list of all the varibales contaning the roll image of each roll from 1 - 6. Used to blit the roll when user presses rollimage.
dicelist = [roll1, roll2, roll3, roll4, roll5, roll6]

# These lists are again co-responding. Beatingimg is a list of all imgaes of the beating messages (all possibilities) along with
# the beatingstr list being the names of all the variables in string. Helps figure out what iamge to use when a token is stepped 
# on. 
beatingstr = ["redbeatsyellow", "redbeatsblue", "redbeatsgreen", "yellowbeatsred", "yellowbeatsblue", "yellowbeatsgreen", "bluebeatsred", "bluebeatsyellow", "bluebeatsgreen", \
              "greenbeatsred", "greenbeatsyellow", "greenbeatsblue"]
beatingimg = [redbeatsyellow, redbeatsblue, redbeatsgreen, yellowbeatsred, yellowbeatsblue, yellowbeatsgreen, bluebeatsred, bluebeatsyellow, bluebeatsgreen, greenbeatsred, \
              greenbeatsyellow, greenbeatsblue]

# List of all images that have the message of their respective team winning the game.
winningimg = [redwin, yellowwin, bluewin, greenwin]

# List of all images that have the message of their respective team getting a token at home.
allhomescores = [redhome, yellowhome, bluehome, greenhome]

# A list of all the possible rolls
allroll = [1, 2, 3, 4, 5, 6]

# A list of the images that are the counter for the user to know how mnay tokens they have at home
hometokenscoreimg = [one, two, three, four]

# The co-ordinates that the counter images need to be placed at for every colour.
showhometokens = [[108.5, 95], [468.5, 95], [468.5, 457], [108.5, 457]]

# MAIN

# Adds the time the game began to the tracking doc.
trackingdoc = open("Tracking Doc", "a")
trackingdoc.write("\n" + str(time.ctime()) + "\n")
trackingdoc.close()

# Starts a loop to continue the game forever until user wishes otherwise.
while True:
    # Gets the screen ready and names the window our game's title.
    screen.fill(white)
    pygame.display.set_caption("Preesha & Eraj's Ludo")

    # Plays background music.
    pygame.mixer.music.load("can't.mp3")
    pygame.mixer.music.play(-1)

    # Calls display menu which shows the user the menu and allows user-interaction - Line: 11:
    displaymenu(None)
