__author__ = 'Pat'

import random
import math

#global variables
playerList = []
rockCut = .3
paperCut = .6
total = 10
me = ""

#finds a player and his information
def findPlayer(person):
    foundPlayer = False
    player = [person,0,0,0]

    for i in range(0,len(playerList)):
        if(playerList[i][0] == person):
            player = playerList[i]
            foundPlayer = True
            break

    if(not foundPlayer):
        playerList.append(player)

    return player

#gets the data for who I am playing against
#sets my odds to play against his pattern
def mePlayingAgainst(person):
    player = findPlayer(person)
    global total, rockCut, paperCut

    rockCount = player[1]
    paperCount = player[2]
    scissorCount = player[3]
    total = rockCount + paperCount + scissorCount

    if(total >= 5):
        rockCut = rockCount/total
        paperCut = paperCount/total

#keeps track of what a player picks
def matchResults(person, played):
    player = findPlayer(person)

    if(played == "rock"):
        player[1] = player[1] + 1
    elif(played == "paper"):
        player[2] = player[2] +1
    elif(played == "scissors"):
        player[3] = player[3] + 1

#implementing observer method
#string checks will need to change to what messages actually will be
def notify(msg):
    splitMsg = (""+msg).split(" ")

    if(splitMsg[1] == "picked"):
        matchResults(splitMsg[0].lower(),splitMsg[2].lower())
    elif(splitMsg[1] == "playing"):
        if(splitMsg[0] == me):
            mePlayingAgainst(splitMsg[2].lower())
        else:
            mePlayingAgainst(splitMsg[0].lower())

#returns my move, based on what the other player chooses most often
def getMove():
    weight = random.random()

    if(weight < paperCut):
        return "scissors"
    elif((weight-paperCut) < rockCut):
        return "paper"
    else:
        return "rock"


#####################################################################
#Testing methods
playerTestList = ['Tony', 'Collin', 'Baliga', 'Dan']
playerChoiceTestList = ['Rock', 'Paper', 'Scissors']

def generateTestResults1():

    for i in range(0,50):
        player1 = playerTestList[math.floor(random.random()*100)%4]
        player2 = playerTestList[math.floor(random.random()*100)%4]

        while(player1 == player2):
            player2 = playerTestList[math.floor(random.random()*100)%4]

        notify(player1+" playing "+player2)
        notify(player1+" picked "+playerChoiceTestList[math.floor(random.random()*100)%3])
        notify(player2+" picked "+playerChoiceTestList[math.floor(random.random()*100)%3])

def generateTestResults2():
    player1 = "Tony"
    player2 = "Collin"

    for i in range(0,50):
        notify(player1+" playing "+player2)
        notify(player1+" picked "+playerChoiceTestList[math.floor(random.random()*100)%3])
        notify(player2+" picked scissors")

generateTestResults1()
me = "Pat"
other = playerTestList[math.floor(random.random()*100)%2]
notify(me+" playing "+other)
myPick = getMove()

print("Playing against: "+other)
print("Odds: ")
print("\t Rock: "+str(rockCut))
print("\t Paper: "+str(paperCut))
print("\t Scissors: "+str(1-rockCut-paperCut))
print("I picked: "+getMove())

print(playerList)