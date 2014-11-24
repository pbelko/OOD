__authors__ = 'Pat and Tony'

import random

class rpsPlayer(Player):
    #self variables
    playerList = []
    rockCut = .3
    paperCut = .6
    total = 10
    name = None

    #finds a player and his information
    def find_player(self, person):
        found_player = False
        player = [person,0,0,0]

        for i in range(0,len(self.playerList)):
            if(self.playerList[i][0] == person):
                player = self.playerList[i]
                found_player = True
                break

        if(not found_player):
            self.playerList.append(player)

        return player

    #gets the data for who I am playing against
    #sets my odds to play against his pattern
    def me_playing_against(self, person):
        player = self.find_player(person)
        global total, rockCut, paperCut

        rockCount = player[1]
        paperCount = player[2]
        scissorCount = player[3]
        total = rockCount + paperCount + scissorCount

        if(total >= 5):
            rockCut = rockCount/total
            paperCut = paperCount/total

    #keeps track of what a player picks
    def match_results(self, person, played):
        player = self.find_player(person)

        if(played == "rock"):
            player[1] = player[1] + 1
        elif(played == "paper"):
            player[2] = player[2] + 1
        elif(played == "scissors"):
            player[3] = player[3] + 1

    #implementing observer method
    #string checks will need to change to what messages actually will be
    def notify(self, msg):
        splitMsg = (""+msg).split(" ")

        if(splitMsg[1] == "picked"):
            self.match_results(splitMsg[0].lower(),splitMsg[2].lower())
        elif(splitMsg[1] == "playing"):
            if(splitMsg[0] == self.name):
                self.me_playing_against(splitMsg[2].lower())
            else:
                self.me_playing_against(splitMsg[0].lower())

    #returns my move, based on what the other player chooses most often
    def play(self, position=None):
        weight = random.random()

        if(weight < paperCut):
            return 2
        elif((weight-paperCut) < rockCut):
            return 1
        else:
            return 0

    def get_name(self):
        return self.name