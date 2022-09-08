print (" *** Welcome to Nim *******!")
print ("In this version of Nim, the player goes first and the computer always wins. Game ends when # of stones <=0")
print ("*****************************************************")
# Will start of a bag of 12 stones
stones = 12
 
# of stonesTaken
stonesTaken = 0

while stones > 0:
    print ("There are " + str(stones)+ " in the bag.\nHow mnay would you like to choose? 1, 2, or 3")
    stonesTaken = input()
    stonesTaken = int(stonesTaken)
    
# if the user picks more than 3 stines or less than one
    if stonesTaken > 3 or stonesTaken < 1:
        print ("Not a valid numbver!Try again.")
        stonesTaken = input()
        stonesTaken = int(stonesTaken)
    
    print("You choose "  + str(stonesTaken))
    
    stones = stones - stonesTaken
    print("Threre are now " + str(stones) + " stones. It is the Computer's turn now")
    
    if stones == 0:
        print("*** You Win ***!")
    
        
# Computer's turn by taking always 4 - the player's pick
    stonesTaken = 4 - stonesTaken
    print ("The computer took " + str(stonesTaken))
    
    stones = stones - stonesTaken
    
    if stones == 0:
        print ("*** The Computer Wins ***!")
    
    

     
