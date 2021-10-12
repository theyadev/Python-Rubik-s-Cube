from variables import *

def Corners(face, reverse=False):
    if reverse:
        (cube[face][2][0], cube[face][2][2], cube[face][0][0],
            cube[face][0][2]) = (cube[face][0][0], cube[face][2][0],
                                cube[face][0][2], cube[face][2][2])
    else:
        (cube[face][0][0], cube[face][2][0], cube[face][0][2],
            cube[face][2][2]) = (cube[face][2][0], cube[face][2][2], cube[face][0][0],
                            cube[face][0][2])
                            
def Arrets(face, reverse=False):
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