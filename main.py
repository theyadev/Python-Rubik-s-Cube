import os

os.system('cls')
cube = [
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ],
    [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2],
    ],
    [
        [3, 3, 3],
        [3, 3, 3],
        [3, 3, 3],
    ],
    [
        [4, 4, 4],
        [4, 4, 4],
        [4, 4, 4],
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5],
    ],
    [
        [6, 6, 6],
        [6, 6, 6],
        [6, 6, 6],
    ]
]

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


def turnHorizontal(layer_to_move, nb=1, reverse=False):
    for i in range(nb):
        HORIZONTAL_LAYERS = [(j, cube[j][layer_to_move])
                     for j in range(len(cube)) if j != 0 and j != 5]
        for i in range(len(HORIZONTAL_LAYERS)):
            index = 0
            layer_index, layer = HORIZONTAL_LAYERS[i]

            if reverse == True:
                if layer_index == 4:
                    index = 1
                else:
                    index = layer_index + 1
            else:
                if layer_index == 1:
                    # if i == 0:
                    index = 4
                else:
                    index = layer_index - 1

            cube[index][layer_to_move] = layer

        if layer_to_move == 2:
            if reverse:
                # Corners
                (cube[5][0][0], cube[5][2][0],  cube[5][0][2], cube[5][2][2]) = (
                    cube[5][2][0], cube[5][2][2],  cube[5][0][0], cube[5][0][2])

                # Arrettes
                (cube[5][2][1], cube[5][1][0], cube[5][0][1], cube[5][1][2]) = (
                    cube[5][1][2], cube[5][2][1], cube[5][1][0], cube[5][0][1])
            else:
                # Corners
                (cube[5][2][0], cube[5][2][2],  cube[5][0][0], cube[5][0][2]) = (
                    cube[5][0][0], cube[5][2][0],  cube[5][0][2], cube[5][2][2])

                # Arrettes
                (cube[5][1][2], cube[5][2][1], cube[5][1][0], cube[5][0][1]) = (
                    cube[5][2][1], cube[5][1][0], cube[5][0][1], cube[5][1][2])

        elif layer_to_move == 0:
            if reverse:
                # Corners
                (cube[layer_to_move][2][0], cube[layer_to_move][2][2],  cube[layer_to_move][0][0], cube[layer_to_move][0][2]) = (
                    cube[layer_to_move][0][0], cube[layer_to_move][2][0],  cube[layer_to_move][0][2], cube[layer_to_move][2][2])

                # Arrettes
                (cube[layer_to_move][1][2], cube[layer_to_move][2][1], cube[layer_to_move][1][0], cube[layer_to_move][0][1]) = (
                    cube[layer_to_move][2][1], cube[layer_to_move][1][0], cube[layer_to_move][0][1], cube[layer_to_move][1][2])

            else:
                # Corners
                (cube[layer_to_move][0][0], cube[layer_to_move][2][0],  cube[layer_to_move][0][2], cube[layer_to_move][2][2]) = (
                    cube[layer_to_move][2][0], cube[layer_to_move][2][2],  cube[layer_to_move][0][0], cube[layer_to_move][0][2])

                # Arrettes
                (cube[layer_to_move][2][1], cube[layer_to_move][1][0], cube[layer_to_move][0][1], cube[layer_to_move][1][2]) = (
                    cube[layer_to_move][1][2], cube[layer_to_move][2][1], cube[layer_to_move][1][0], cube[layer_to_move][0][1])


def turnVertical(layer_to_move, nb=1, reverse=False):
    for i in range(nb):
        VERTICAL_LAYERS = [(j, [cube[j][k][layer_to_move] for k in range(len(cube[j]))])
                       for j in range(len(cube)) if j != 1 and j != 3 and j != 4 and j != 0]
        if reverse == True:
            VERTICAL_LAYERS.append((4, [cube[4][0][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1], cube[4][1][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1],cube[4][2][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1]]))
            VERTICAL_LAYERS.append((0, [cube[0][0][layer_to_move], cube[0][1][layer_to_move],cube[0][2][layer_to_move]]))
        else:
            VERTICAL_LAYERS.append((4, [cube[4][2][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1], cube[4][1][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1], cube[4][0][0 if layer_to_move == 2 else 2 if layer_to_move == 0 else 1]]))
            VERTICAL_LAYERS.append(
                (0, [cube[0][2][layer_to_move], cube[0][1][layer_to_move], cube[0][0][layer_to_move]]))

        for D in range(len(VERTICAL_LAYERS)):
            index = 0
            layer_index, layer = VERTICAL_LAYERS[D]

            if reverse:
                if layer_index == 0:
                    index = 2
                elif layer_index == 2:
                    index = 5
                elif layer_index == 4:
                    index = 0
                elif layer_index == 5:
                    index = 4
            else:
                if layer_index == 0:
                    index = 4
                elif layer_index == 2:
                    index = 0
                elif layer_index == 4:
                    index = 5
                elif layer_index == 5:
                    index = 2

            for k in range(len(layer)):
                cube[index][k][0 if index == 4 and layer_to_move == 2 else 2 if index==4 and layer_to_move == 0 else layer_to_move] = layer[k]

        if layer_to_move == 0:
            if reverse:
                # Corners
                (cube[layer_to_move+1][0][0], cube[layer_to_move+1][2][0],  cube[layer_to_move+1][0][2], cube[layer_to_move+1][2][2]) = (
                    cube[layer_to_move+1][2][0], cube[layer_to_move+1][2][2],  cube[layer_to_move+1][0][0], cube[layer_to_move+1][0][2])

                # Arrettes
                (cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1], cube[layer_to_move+1][1][2]) = (
                    cube[layer_to_move+1][1][2], cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1])
            else:
                # Corners
                (cube[layer_to_move+1][2][0], cube[layer_to_move+1][2][2],  cube[layer_to_move+1][0][0], cube[layer_to_move+1][0][2]) = (
                    cube[layer_to_move+1][0][0], cube[layer_to_move+1][2][0],  cube[layer_to_move+1][0][2], cube[layer_to_move+1][2][2])

                # Arrettes
                (cube[layer_to_move+1][1][2], cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1]) = (
                    cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1], cube[layer_to_move+1][1][2])

        elif layer_to_move == 2:
            if reverse:
                # Corners
                (cube[layer_to_move+1][2][0], cube[layer_to_move+1][2][2],  cube[layer_to_move+1][0][0], cube[layer_to_move+1][0][2]) = (
                    cube[layer_to_move+1][0][0], cube[layer_to_move+1][2][0],  cube[layer_to_move+1][0][2], cube[layer_to_move+1][2][2])

                # Arrettes
                (cube[layer_to_move+1][1][2], cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1]) = (
                    cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1], cube[layer_to_move+1][1][2])

            else:
                # Corners
                (cube[layer_to_move+1][0][0], cube[layer_to_move+1][2][0],  cube[layer_to_move+1][0][2], cube[layer_to_move+1][2][2]) = (
                    cube[layer_to_move+1][2][0], cube[layer_to_move+1][2][2],  cube[layer_to_move+1][0][0], cube[layer_to_move+1][0][2])

                # Arrettes
                (cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1], cube[layer_to_move+1][1][2]) = (
                    cube[layer_to_move+1][1][2], cube[layer_to_move+1][2][1], cube[layer_to_move+1][1][0], cube[layer_to_move+1][0][1])


while True:
    for z in range(len(cube)):
        for y in range(len(cube[z])):
            row = ""
            for x in range(len(cube[z][y])):
                if cube[z][y][x] == 6:
                    row += f"{BackgroundColors.WHITE}[]{BackgroundColors.RESET}"
                elif cube[z][y][x] == 2:
                    row += f"{BackgroundColors.RED}[]{BackgroundColors.RESET}"
                elif cube[z][y][x] == 3:
                    row += f"{BackgroundColors.GREEN}[]{BackgroundColors.RESET}"
                elif cube[z][y][x] == 4:
                    row += f"{BackgroundColors.MAGENTA}[]{BackgroundColors.RESET}"
                elif cube[z][y][x] == 5:
                    row += f"{BackgroundColors.BLUE}[]{BackgroundColors.RESET}"
                elif cube[z][y][x] == 1:
                    row += f"{BackgroundColors.YELLOW}[]{BackgroundColors.RESET}"

            if z == 0:
                printAt(8, 1+y, row)
            elif z == 5:
                printAt(8, 9+y, row)
            else:
                printAt((z-1)*7+1, 5+y, row)

    turn = input('\nQue voulez vous tourner ? \033[K').upper()

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
    elif turn == "S":
        turnHorizontal(1, reverse=True)
    elif turn == "S'":
        turnHorizontal(1)
    elif turn == "S2":
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
