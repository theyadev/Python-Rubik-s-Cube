import os
from time import sleep
from random import randint

os.system('cls')
cube = [[
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
], [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2],
], [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3],
], [
    [4, 4, 4],
    [4, 4, 4],
    [4, 4, 4],
], [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5],
], [
    [6, 6, 6],
    [6, 6, 6],
    [6, 6, 6],
]]

format_prefix = "\033["
position_suffix = "H"


def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")


class BackgroundColors:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[49m'
    RESET_ALL = '\033[0m'

def rotateCorners(face, reverse=False):
    if reverse:
        (cube[face][2][0], cube[face][2][2], cube[face][0][0],
            cube[face][0][2]) = (cube[face][0][0], cube[face][2][0],
                                cube[face][0][2], cube[face][2][2])
    else:
        (cube[face][0][0], cube[face][2][0], cube[face][0][2],
            cube[face][2][2]) = (cube[face][2][0], cube[face][2][2], cube[face][0][0],
                            cube[face][0][2])
def rotateArrets(face, reverse=False):
    if reverse:
        (cube[face][1][2], cube[face][2][1],
            cube[face][1][0],
            cube[face][0][1]) = (cube[face][2][1],
                                        cube[face][1][0],
                                        cube[face][0][1],
                                        cube[face][1][2])
    else:
        (cube[face][2][1], cube[face][1][0], cube[face][0][1],
            cube[face][1][2]) = (cube[face][1][2], cube[face][2][1], cube[face][1][0],
                            cube[face][0][1])


def turnHorizontal(layer_to_move, nb=1, reverse=False):
    for loop in range(nb):
        HORIZONTAL_LAYERS = [(j, cube[j][layer_to_move])
                             for j in range(len(cube)) if j != 0 and j != 5]
        for i in range(len(HORIZONTAL_LAYERS)):
            index = 0
            layer_index, layer = HORIZONTAL_LAYERS[i]

            if reverse:
                if layer_index == 4:
                    index = 1
                else:
                    index = layer_index + 1
            else:
                if layer_index == 1:
                    index = 4
                else:
                    index = layer_index - 1

            cube[index][layer_to_move] = layer

        if layer_to_move == 2:
            rotateCorners(5, reverse)
            rotateArrets(5,reverse)

        elif layer_to_move == 0:
            rotateCorners(layer_to_move, reverse)
            rotateArrets(layer_to_move, reverse)


def turnVertical(layer_to_move, nb=1, reverse=False):
    for loop in range(nb):
        VERTICAL_LAYERS = [(j, [cube[j][k][layer_to_move] for k in range(len(cube[j]))]) for j in range(len(cube)) if j != 1 and j != 3 and j != 4 and j != 0 and j != 5]
        
        VERTICAL_LAYERS.append((4, [
            cube[4][2][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1], cube[4][1][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1],cube[4][0][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1]
        ]))
            
        VERTICAL_LAYERS.append((0, [
            cube[0][0 if reverse else 2][layer_to_move], cube[0][1][layer_to_move],
            cube[0][2 if reverse else 0][layer_to_move]
        ]))
        
        VERTICAL_LAYERS.append((5, [
            cube[5][2 if reverse else 0][layer_to_move], cube[5][1][layer_to_move],
            cube[5][0 if reverse else 2][layer_to_move]
        ]))

        for D in range(len(VERTICAL_LAYERS)):
            index = 0
            layer_index, layer = VERTICAL_LAYERS[D]

            if layer_index == 0:
                index = 2 if reverse else 4
            elif layer_index == 2:
                index = 5 if reverse else 0
            elif layer_index == 4:
                index = 0 if reverse else 5
            elif layer_index == 5:
                index = 4 if reverse else 2

            for k in range(len(layer)):
                cube[index][k][0 if index == 4 and layer_to_move ==
                               2 else 2 if index == 4 and layer_to_move ==
                               0 else layer_to_move] = layer[k]

        if layer_to_move == 2:
            rotateCorners(layer_to_move + 1, reverse)
            rotateArrets(layer_to_move + 1,reverse)

        elif layer_to_move == 0:
            rotateCorners(layer_to_move + 1, not reverse)
            rotateArrets(layer_to_move + 1, not reverse)


def turnFront(layer_to_move, nb=1, reverse=False):
    for loop in range(nb):
        FRONT_LAYERS = [
            (0, [cube[0][2 if layer_to_move == 0 else 0 if layer_to_move == 2 else 1][k] for k in range(len(cube[0]))]),
            (1, [cube[1][k][2 if layer_to_move == 0 else 0 if layer_to_move == 2 else 1] for k in range(len(cube[0]))]),
            (3, [cube[3][k][0 if layer_to_move == 0 else 2 if layer_to_move == 2 else 1] for k in range(len(cube[0]))]),
            (5, [cube[5][0 if layer_to_move == 0 else 2 if layer_to_move == 2 else 1][k] for k in range(len(cube[0]))])
        ]

        for D in range(len(FRONT_LAYERS)):
            index = 0
            layer_index, layer = FRONT_LAYERS[D]

            if layer_index == 0:
                index = 3 if not reverse else 1
            elif layer_index == 1:
                index = 0 if not reverse else 5
            elif layer_index == 3:
                index = 5 if not reverse else 0
            elif layer_index == 5:
                index = 1 if not reverse else 3

            for k in range(len(layer)):
                if index == 0 :
                    cube[index][2 if layer_to_move == 0 else 0 if layer_to_move == 2 else 1][k] = layer[k] if reverse else layer[::-1][k] 
                elif index == 1 :
                    cube[index][k][2 if layer_to_move == 0 else 0 if layer_to_move == 2 else 1] = layer[::-1][k] if reverse else layer[k] 
                elif index == 3 :
                    cube[index][k][0 if layer_to_move == 0 else 2 if layer_to_move == 2 else 1] = layer[::-1][k] if reverse else layer[k] 
                elif index == 5 :
                    cube[index][0 if layer_to_move == 0 else 2 if layer_to_move == 2 else 1][k] = layer[k] if reverse else layer[::-1][k]

        if layer_to_move == 2:
            rotateCorners(4, not reverse)
            rotateArrets(4, not reverse)

        elif layer_to_move == 0:
            rotateCorners(2, reverse)
            rotateArrets(2, reverse)

def printCube():
    for z in range(len(cube)):
        for y in range(len(cube[z])):
            row = ""
            for x in range(len(cube[z][y])):
                if cube[z][y][x] == 6:
                    row += f"🔳"
                elif cube[z][y][x] == 2:
                    row += f"🟥"
                elif cube[z][y][x] == 3:
                    row += f"🟩"
                elif cube[z][y][x] == 4:
                    row += f"🟧"
                elif cube[z][y][x] == 5:
                    row += f"🟦"
                elif cube[z][y][x] == 1:
                    row += f"🟨"

            if z == 0:
                printAt(8, 1 + y, row)
            elif z == 5:
                printAt(8, 9 + y, row)
            else:
                printAt((z - 1) * 7 + 1, 5 + y, row)

def shuffleCube(length_shuffle = 25):  
    moves = "UDERLMFBS"

    shuffle = ""

    for i in range(length_shuffle):
        number = "2" if randint(0,2) == 1 else ""
        prime = "'" if number == "" and randint(0,1) == 1 else ""
        letter = moves[randint(0,len(moves)-1)]
        shuffle += letter + number + prime
       
    return shuffle



def moveCube(alg, speed):
    for i,turn in enumerate(alg):
        if turn == "'" or turn == "2":
            continue

        try:
            if alg[i+1] == "'":
                turn += "'"
            elif alg[i+1] == "2":
                turn += "2"
        except:
            pass

        if turn == "U":
            turnHorizontal(0)
        elif turn == "U'":
            turnHorizontal(0, reverse=True)
        elif turn == "U2":
            turnHorizontal(0, 2)
        elif turn == "D":
            turnHorizontal(2, reverse=True)
        elif turn == "D'":
            turnHorizontal(2)
        elif turn == "D2":
            turnHorizontal(2, 2)
        elif turn == "E":
            turnHorizontal(1, reverse=True)
        elif turn == "E'":
            turnHorizontal(1)
        elif turn == "E2":
            turnHorizontal(1, 2)
        elif turn == "R":
            turnVertical(2)
        elif turn == "R'":
            turnVertical(2, reverse=True)
        elif turn == "R2":
            turnVertical(2, 2)
        elif turn == "L":
            turnVertical(0, reverse=True)
        elif turn == "L'":
            turnVertical(0)
        elif turn == "L2":
            turnVertical(0, 2)
        elif turn == "M":
            turnVertical(1, reverse=True)
        elif turn == "M'":
            turnVertical(1)
        elif turn == "M2":
            turnVertical(1, 2)
        elif turn == "F":
            turnFront(0)
        elif turn == "F'":
            turnFront(0, reverse=True)
        elif turn == "F2":
            turnFront(0,2)
        elif turn == "B":
            turnFront(2, reverse=True)
        elif turn == "B'":
            turnFront(2)
        elif turn == "B2":
            turnFront(2,2)
        elif turn == "S":
            turnFront(1)
        elif turn == "S'":
            turnFront(1, reverse=True)
        elif turn == "S2":
            turnFront(1,2)

        printCube()
        sleep(speed)
        
shuffle = shuffleCube(10)
moveCube(shuffle, 0.1)
printCube()

while True:
    print("\n" + shuffle)
    algo = input('\nQue voulez vous tourner ? \033[K').upper().replace(' ', "")
    moveCube(algo, 0.2)