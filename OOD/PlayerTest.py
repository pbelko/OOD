__author__ = 'Pat'


# import Player
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