from Implementations.Labyrinth import Labyrinth
from Implementations.Player import Player
from random import *
from Implementations.Aventure import Aventure

if __name__ == "__main__":
    print("LABYRINTH")
    user_input=0
    while int(user_input)>10 or int(user_input)<4:
        print("Choose the size of the Labyrinth (between 4 and 10):")
        user_input = input()
    newAventure=Aventure(int(user_input))
    newAventure.__start__()


