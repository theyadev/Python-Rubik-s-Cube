from variables import *
from Colors import BackgroundColors

def printAt(x, y, text):
    print(f"\033[{y};{x}H{text}")

def printCube():
    for z in range(len(cube)):
        for y in range(len(cube[z])):
            row = ""
            for x in range(len(cube[z][y])):
                if cube[z][y][x] == 6:
                    row += f"{BackgroundColors.WHITE}  {BackgroundColors.RESET}"
                elif cube[z][y][x] == 2:
                    row += f"{BackgroundColors.RED}  {BackgroundColors.RESET}"
                elif cube[z][y][x] == 3:
                    row += f"{BackgroundColors.GREEN}  {BackgroundColors.RESET}"
                elif cube[z][y][x] == 4:
                    row += f"{BackgroundColors.MAGENTA}  {BackgroundColors.RESET}"
                elif cube[z][y][x] == 5:
                    row += f"{BackgroundColors.BLUE}  {BackgroundColors.RESET}"
                elif cube[z][y][x] == 1:
                    row += f"{BackgroundColors.YELLOW}  {BackgroundColors.RESET}"

            if z == 0:
                printAt(8, 1 + y, row)
            elif z == 5:
                printAt(8, 9 + y, row)
            else:
                printAt((z - 1) * 7 + 1, 5 + y, row)