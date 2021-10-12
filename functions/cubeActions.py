import turns as turn

from variables import *
from random import randint
from prints import printCube
from time import sleep
from random import randint

def getShuffle(length_shuffle = 25):  
    moves = "UDERLMFBS"

    shuffle = ""

    for loop in range(length_shuffle):
        number = "2" if randint(0,2) == 1 else ""
        prime = "'" if number == "" and randint(0,1) == 1 else ""
        letter = moves[randint(0,len(moves)-1)]
        shuffle += letter + number + prime
       
    return shuffle



def moveCube(alg, speed):
    for i,letter in enumerate(alg):
        if letter == "'" or letter == "2":
            continue

        try:
            if alg[i+1] == "'":
                letter += "'"
            elif alg[i+1] == "2":
                letter += "2"
        except:
            pass

        if letter == "U":
            turn.Horizontal(0)
        elif letter == "U'":
            turn.Horizontal(0, reverse=True)
        elif letter == "U2":
            turn.Horizontal(0, 2)
        elif letter == "D":
            turn.Horizontal(2, reverse=True)
        elif letter == "D'":
            turn.Horizontal(2)
        elif letter == "D2":
            turn.Horizontal(2, 2)
        elif letter == "E":
            turn.Horizontal(1, reverse=True)
        elif letter == "E'":
            turn.Horizontal(1)
        elif letter == "E2":
            turn.Horizontal(1, 2)
        elif letter == "R":
            turn.Vertical(2)
        elif letter == "R'":
            turn.Vertical(2, reverse=True)
        elif letter == "R2":
            turn.Vertical(2, 2)
        elif letter == "L":
            turn.Vertical(0, reverse=True)
        elif letter == "L'":
            turn.Vertical(0)
        elif letter == "L2":
            turn.Vertical(0, 2)
        elif letter == "M":
            turn.Vertical(1, reverse=True)
        elif letter == "M'":
            turn.Vertical(1)
        elif letter == "M2":
            turn.Vertical(1, 2)
        elif letter == "F":
            turn.Front(0)
        elif letter == "F'":
            turn.Front(0, reverse=True)
        elif letter == "F2":
            turn.Front(0,2)
        elif letter == "B":
            turn.Front(2, reverse=True)
        elif letter == "B'":
            turn.Front(2)
        elif letter == "B2":
            turn.Front(2,2)
        elif letter == "S":
            turn.Front(1)
        elif letter == "S'":
            turn.Front(1, reverse=True)
        elif letter == "S2":
            turn.Front(1,2)

        printCube()
        sleep(speed)