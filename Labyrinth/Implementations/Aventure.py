import sys
from random import randint

from Implementations.Player import Player
from Implementations.Labyrinth import Labyrinth

class Aventure:

    def __init__(self,size:int):
        self._labyrinth=Labyrinth(size)
        self._player=Player(self._labyrinth.get_listRooms()[(randint(0,size-1),randint(0,size-1))])
        self._bear=Player(self._labyrinth.get_listRooms()[(randint(0,size-1),randint(0,size-1))])

    def get_Labyrinth(self):
        return self._labyrinth

    def get_Player(self):
        return self._player

    def get_Bear(self):
        return self._bear

    def combat(self):
        if str((self.get_Bear().get_Room().get_posX(),self.get_Bear().get_Room().get_posY()))==str((self.get_Player().get_Room().get_posX(),self.get_Bear().get_Room().get_posY())):
            self.get_Player().take_Damage()
            trying=self.get_Player().north(self.get_Labyrinth())
            if trying=="Certainly, there is a wall here!" or trying=="You touch some monolith, find an other way!":
                trying==self.get_Player().south(self.get_Labyrinth())
            if trying=="Certainly, there is a wall here!" or trying=="You touch some monolith, find an other way!":
                trying==self.get_Player().west(self.get_Labyrinth())
            if trying=="Certainly, there is a wall here!" or trying=="You touch some monolith, find an other way!":
                trying==self.get_Player().east(self.get_Labyrinth())
            print("You After attack"+str((self.get_Player().get_Room().get_posX(),self.get_Player().get_Room().get_posY())))
            if self.get_Player().get_Hp()<=0:
                print("You bleed to much ...")
                print("GAME OVER x|")
                return 1
        else:
            print("Your hear the bear's growling, but your are safe .. for now")
        return 0

    def __start__(self):

        finished=0
        print("Welcome to the Labyrinth!")
        print("Find the treasure and escape of this place")
        print("###----Let's Play-----###")

        while finished != 1 and self.get_Player().get_Hp()!=0:
            print("Choose a command")
            print("Inventory")
            print("Forward")
            print("Backward")
            print("Left")
            print("Right")
            print("Skip")
            print("TypeOfRoom")
            print("Quit")
            user_input = input()

            if user_input == "Quit":
                print("CLOSING GAME")
                finished = 1
            else:
                description = user_input.split( )
                if description[0] == "Forward":
                    print(self.get_Player().south(self.get_Labyrinth()))
                    self.combat()
                    print("Bear is moving around")
                    self.get_Bear().randomMove(self.get_Labyrinth())
                    self.combat()
                elif description[0]=="Inventory":
                    print(self.get_Player().get_Inventory())
                elif description[0] == "Backward":
                    print(self.get_Player().north(self.get_Labyrinth()))
                    self.combat()
                    print("Bear is moving around")
                    self.get_Bear().randomMove(self.get_Labyrinth())
                    self.combat()
                elif description[0] == "Left":
                    print(self.get_Player().west(self.get_Labyrinth()))
                    self.combat()
                    print("Bear is moving around")
                    self.get_Bear().randomMove(self.get_Labyrinth())
                    self.combat()
                elif description[0] == "Right":
                    print(self.get_Player().east(self.get_Labyrinth()))
                    self.combat()
                    print("Bear is moving around")
                    self.get_Bear().randomMove(self.get_Labyrinth())
                    self.combat()
                elif description[0] == "Skip":
                    output=self.get_Player().research(self.get_Labyrinth())
                    print(output)
                    if output=="You see sunlight in front of you, and your treasure is shining!":
                        print("Congratulations you defeated the terrible Labyrinth! \n Thanks for Playing :)\n")
                        finished=1
                    self.combat()
                    print("Bear is moving around")
                    self.get_Bear().randomMove(self.get_Labyrinth())
                    self.combat()
                elif description[0] == "Cheat0":
                    print("You"+str((self.get_Player().get_Room().get_posX(),self.get_Player().get_Room().get_posY())))
                elif description[0] == "Cheat1":
                    print("Exit"+str(self.get_Labyrinth().get_specialRoomsIndex()[0]))
                elif description[0] == "Cheat2":
                    print("Loot"+str(self.get_Labyrinth().get_specialRoomsIndex()[1]))
                elif description[0]=="Cheat4":
                    print("Bear:"+str((self.get_Bear().get_Room().get_posX(),self.get_Bear().get_Room().get_posY())))
                elif description[0] == "Cheat3":
                    self.get_Player().set_Room(self.get_Labyrinth().get_Room(self.get_Bear().get_Room().get_posX(),self.get_Bear().get_Room().get_posY()))
                elif description[0] == "Cheat5":
                    print(self.get_Player().get_Hp())
                elif description[0] == "TypeOfRoom":
                    print(self.get_Player().get_Room().get_cellType())
                elif description[0]== "AddMap":
                    self.get_Player().add_Loot("map")
                elif description[0]=="Map":
                    if self.get_Player().haveMap():
                        print(self.get_Labyrinth().view())
                    else:
                        print("You need a map for that action")

                else:
                    print("Incorrect input")
        print("------------------------------------------------------------------------\n")