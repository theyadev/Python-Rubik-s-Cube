from variables import *

def printAt(x, y, text):
    print(f"\033[{y};{x}H{text}")

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