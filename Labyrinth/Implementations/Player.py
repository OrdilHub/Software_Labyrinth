from Implementations.Cell import Cell
from Implementations.CellTypes import CellTypes
from Implementations.Labyrinth import Labyrinth
from Implementations.SideTypes import SideTypes
from Services.IPlayer import IPlayer
from random import *


class Player(IPlayer):

    def __init__(self,posCell:Cell):
        self._posCell=posCell
        self._loot=[]
        self._hp=2

    def get_Inventory(self):
        return self._loot

    def add_Loot(self, item:str):
        self._loot.append(item)

    def haveMap(self):
        return "map" in self.get_Inventory()


    def get_Room(self):
        return self._posCell

    def set_Room(self, destination):
        self._posCell=destination

    def get_Hp(self):
        return self._hp

    def take_Damage(self):
        self._hp=self.get_Hp()-1

    def north(self, labyrinth:Labyrinth):
        if self.get_Room().get_sideN()==SideTypes.NONE:
            self.set_Room(labyrinth.get_Room(self.get_Room().get_posX()-1,self.get_Room().get_posY()))
            return "You walk carrefuly in the dark ... and found:"+str(self.get_Room().get_cellType())
        elif self.get_Room().get_sideN()==SideTypes.END:
            return "You touch some monolith, find an other way!"
        else:
            return "Certainly, there is a wall here!"

    def west(self, labyrinth:Labyrinth):
        if self.get_Room().get_sideO()==SideTypes.NONE:
            self.set_Room(labyrinth.get_Room(self.get_Room().get_posX(),self.get_Room().get_posY()-1))
            return "You walk carrefuly in the dark ... and found:"+str(self.get_Room().get_cellType())
        elif self.get_Room().get_sideO()==SideTypes.END:
            return "You touch some monolith, find an other way!"
        else:
            return "Certainly, there is a wall here!"

    def east(self, labyrinth:Labyrinth):
        if self.get_Room().get_sideE()==SideTypes.NONE:
            self.set_Room(labyrinth.get_Room(self.get_Room().get_posX(),self.get_Room().get_posY()+1))
            return "You walk carrefuly in the dark ... and found:"+str(self.get_Room().get_cellType())
        elif self.get_Room().get_sideE()==SideTypes.END:
            return "You touch some monolith, find an other way!"
        else:
            return "Certainly, there is a wall here!"

    def south(self, labyrinth:Labyrinth):
        if self.get_Room().get_sideS()==SideTypes.NONE:
            self.set_Room(labyrinth.get_Room(self.get_Room().get_posX()+1,self.get_Room().get_posY()))
            return "You walk carrefuly in the dark ... and found:"+str(self.get_Room().get_cellType())
        elif self.get_Room().get_sideS()==SideTypes.END:
            return "You touch some monolith, find an other way!"
        else:
            return "Certainly, there is a wall here!"

    def research(self, labyrinth:Labyrinth):
        if self.get_Room().get_cellType()==CellTypes.EXIT:
            if self.get_Inventory().count("Treasure")==1:
                return "You see sunlight in front of you, and your treasure is shining!"
            else:
                return "You see sunlight in front of you, but you cannot give up now! "
        elif self.get_Room().get_cellType()==CellTypes.LOOT:
            self.add_Loot("Treasure")
            return "Here is the Jackpot!!! You take this wonder in your bag"
        elif self.get_Room().get_cellType()==CellTypes.TP1:
            self.set_Room(labyrinth.get_TypedRoom(CellTypes.TP2))
            return "WORMHOLE!!!"
        elif self.get_Room().get_cellType()==CellTypes.TP2:
            self.set_Room(labyrinth.get_TypedRoom(CellTypes.TP3))
            return "WORMHOLE!!!"
        elif self.get_Room().get_cellType()==CellTypes.TP3:
            self.set_Room(labyrinth.get_TypedRoom(CellTypes.TP4))
            return "WORMHOLE!!!"
        elif self.get_Room().get_cellType()==CellTypes.TP4:
            self.set_Room(labyrinth.get_TypedRoom(CellTypes.TP5))
            return "WORMHOLE!!!"
        elif self.get_Room().get_cellType()==CellTypes.TP5:
            self.set_Room(labyrinth.get_TypedRoom(CellTypes.TP1))
            return "WORMHOLE!!!"
        else:
            return "There is noting for sure"

    def randomMove(self, labyrinth:Labyrinth):
        random=randint(0, 4) ;
        if random==0:
            return self.north(labyrinth)
        elif random==1:
            return self.south(labyrinth)
        elif random==2:
            return self.east(labyrinth)
        elif random==3:
            return self.west(labyrinth)
        else:
            return self.research(labyrinth)
