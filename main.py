import sys
sys.path.append("./functions")

from clear import clear
from prints import printCube
from cubeActions import moveCube
from userActions import askShuffle        

if __name__ == "__main__":
    clear()
    askShuffle()
    printCube()

    while True:
        print('\n\033[K'*10)
        print("\033[10A")
        algo = input('\nQue voulez vous tourner ? \033[K').upper().replace(' ', "")

        moveCube(algo, 0.2)