import rotations as rotate

from variables import *

def Horizontal(layer_to_move, nb=1, reverse=False):
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
            rotate.Corners(5, reverse)
            rotate.Edges(5,reverse)

        elif layer_to_move == 0:
            rotate.Corners(layer_to_move, reverse)
            rotate.Edges(layer_to_move, reverse)


def Vertical(layer_to_move, nb=1, reverse=False):
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
            rotate.Corners(layer_to_move + 1, reverse)
            rotate.Edges(layer_to_move + 1,reverse)

        elif layer_to_move == 0:
            rotate.Corners(layer_to_move + 1, not reverse)
            rotate.Edges(layer_to_move + 1, not reverse)


def Front(layer_to_move, nb=1, reverse=False):
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
            rotate.Corners(4, not reverse)
            rotate.Edges(4, not reverse)

        elif layer_to_move == 0:
            rotate.Corners(2, reverse)
            rotate.Edges(2, reverse)