from clear import clear
from cubeActions import moveCube, getShuffle

def askShuffle():
    shuffle_input = input('Voulez vous mélanger le cube avant de commencer ? ').lower()
    
    if shuffle_input == "yes" or shuffle_input == 'y' or shuffle_input == 'o' or shuffle_input == 'oui':
        try:
            how_many_input = input('Combien de rotations voulez-vous au mélange ? (Défaut = 20) ')
            number_rotations = 20 if how_many_input == "" else int(how_many_input)
            shuffle = getShuffle(number_rotations)

            clear()
            moveCube(shuffle, 0.1)
        except:
            print("Il y a eu une erreur, le cube n'a pas été mélanger")
            input("Entrée pour continuer...")
            clear()
    clear()