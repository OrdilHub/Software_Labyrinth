from Services.ILabyrinth import ILabyrinth
from Implementations.Cell import Cell
from Implementations.CellTypes import CellTypes
from Implementations.SideTypes import SideTypes
from random import *


class Labyrinth(ILabyrinth):

    def __init__(self, size: int):
        self._size = size
        self._rooms = dict()
        self._specialRooms = list(map(CellTypes, CellTypes))
        self._specialRoomsIndex = []
        randomGenerationList = []
        randomValue = randint(0, size - 1)
        if randint(0, 1) == 0:
            if randint(0, 1) == 0:
                self._specialRoomsIndex.append((0, randomValue))
            else:
                self._specialRoomsIndex.append((size - 1, randomValue))
        elif randint(0, 1) == 0:
            self._specialRoomsIndex.append((randomValue, 0))
        else:
            self._specialRoomsIndex.append((randomValue, size - 1))

        for i in range(len(self._specialRooms) - 2):
            testAlreadyUsed = self._specialRoomsIndex[-1]
            while testAlreadyUsed in self._specialRoomsIndex:
                testAlreadyUsed = (randint(0, size - 1), randint(0, size - 1))
            self._specialRoomsIndex.append(testAlreadyUsed)
        for iteratorX in range(size):
            for iteratorY in range(size):

                cellType = CellTypes.FREE
                sideS = SideTypes.WALL
                sideN = SideTypes.WALL
                sideE = SideTypes.WALL
                sideO = SideTypes.WALL

                if (iteratorX, iteratorY) in self._specialRoomsIndex:
                    cellType = self._specialRooms[self._specialRoomsIndex.index((iteratorX, iteratorY)) + 1]

                if iteratorX == 0:
                    sideN = SideTypes.END
                if iteratorX == size - 1:
                    sideS = SideTypes.END
                if iteratorY == 0:
                    sideO = SideTypes.END
                if iteratorY == size - 1:
                    sideE = SideTypes.END

                self._rooms[(iteratorX, iteratorY)] = Cell(iteratorX,iteratorY,cellType, iteratorX * size + iteratorY, sideN, sideO, sideE,
                                                           sideS)
                randomGenerationList.append(iteratorX * size + iteratorY)
        listRoomLineView=[]
        for i in range (self._size):
            for j in range (self._size):
                listRoomLineView.append(self._rooms[(i,j)].get_monolith())
        while len(randomGenerationList) > 1:
            actualRoom = choice(randomGenerationList)
            listRooms = []
            for key, value in self._rooms.items():
                if value.get_valueGeneration() == actualRoom:
                    listRooms.append(key)

            found = 0
            visitor = 0
            while found != 1 and visitor<len(listRooms):

                testCellWall = self._rooms[listRooms[visitor]].get_wall()
                listRoomLineView=[]
                for i in range(self._size):
                    for j in range (self._size):
                        listRoomLineView.append(self._rooms[(i,j)].get_wall())
                indexWall = []

                for i in range(len(testCellWall)):
                    if testCellWall[i]:
                        indexWall.append(i)

                if len(indexWall) > 0:

                    whichWall = choice(indexWall)

                    if whichWall == 0:
                        delValueGeneration = self._rooms[
                            (listRooms[visitor][0]-1, listRooms[visitor][1])].get_valueGeneration()
                        if delValueGeneration != actualRoom:
                            randomGenerationList.remove(delValueGeneration)
                            found += 1
                            self._rooms[listRooms[visitor]].set_sideN(SideTypes.NONE)
                            self._rooms[(listRooms[visitor][0]-1, listRooms[visitor][1])].set_sideS(SideTypes.NONE)
                            for key, value in self._rooms.items():
                                if value.get_valueGeneration() == delValueGeneration:
                                    self._rooms[key].set_valueGeneration(actualRoom)

                    if whichWall == 1:
                        delValueGeneration = self._rooms[
                            (listRooms[visitor][0], listRooms[visitor][1]-1)].get_valueGeneration()
                        found += 1
                        if delValueGeneration != actualRoom:
                            randomGenerationList.remove(delValueGeneration)
                            self._rooms[listRooms[visitor]].set_sideO(SideTypes.NONE)
                            self._rooms[(listRooms[visitor][0], listRooms[visitor][1]-1)].set_sideE(SideTypes.NONE)
                            for key, value in self._rooms.items():
                                if value.get_valueGeneration() == delValueGeneration:
                                    self._rooms[key].set_valueGeneration(actualRoom)

                    if whichWall == 2:
                        delValueGeneration = self._rooms[
                            (listRooms[visitor][0] , listRooms[visitor][1]+1)].get_valueGeneration()
                        if delValueGeneration != actualRoom:
                            randomGenerationList.remove(delValueGeneration)
                            found += 1
                            self._rooms[listRooms[visitor]].set_sideE(SideTypes.NONE)
                            self._rooms[(listRooms[visitor][0], listRooms[visitor][1]+1)].set_sideO(SideTypes.NONE)
                            for key, value in self._rooms.items():
                                if value.get_valueGeneration() == delValueGeneration:
                                    self._rooms[key].set_valueGeneration(actualRoom)

                    if whichWall == 3:
                        delValueGeneration = self._rooms[
                            (listRooms[visitor][0]+1, listRooms[visitor][1])].get_valueGeneration()
                        if delValueGeneration != actualRoom:
                            randomGenerationList.remove(delValueGeneration)
                            found += 1
                            self._rooms[listRooms[visitor]].set_sideS(SideTypes.NONE)
                            self._rooms[(listRooms[visitor][0]+1, listRooms[visitor][1])].set_sideN(SideTypes.NONE)
                            for key, value in self._rooms.items():
                                if value.get_valueGeneration() == delValueGeneration:
                                    self._rooms[key].set_valueGeneration(actualRoom)

                visitor += 1
            # self._specialRoomsIndex().index((iteratorX,iteratorY))+1

    def get_size(self):
        return self._size

    def get_entry(self):
        return self.get_specialRoomsIndex()[0]

    def get_listRooms(self):
        return self._rooms

    def get_Room(self,posX,posY):
        return  self._rooms[(posX,posY)]

    def get_TypedRoom(self,type:CellTypes):
        if type==CellTypes.TP1:
            return self.get_Room(self.get_specialRoomsIndex()[2][0],self.get_specialRoomsIndex()[2][1])
        if type==CellTypes.TP2:
            return self.get_Room(self.get_specialRoomsIndex()[3][0],self.get_specialRoomsIndex()[3][1])
        if type==CellTypes.TP3:
            return self.get_Room(self.get_specialRoomsIndex()[4][0],self.get_specialRoomsIndex()[4][1])
        if type==CellTypes.TP4:
            return self.get_Room(self.get_specialRoomsIndex()[5][0],self.get_specialRoomsIndex()[5][1])
        if type==CellTypes.TP5:
            return self.get_Room(self.get_specialRoomsIndex()[6][0],self.get_specialRoomsIndex()[6][1])
        if type==CellTypes.R1:
            return self.get_Room(self.get_specialRoomsIndex()[7][0],self.get_specialRoomsIndex()[7][1])
        if type==CellTypes.R2:
            return self.get_Room(self.get_specialRoomsIndex()[8][0],self.get_specialRoomsIndex()[8][1])
        if type==CellTypes.R3:
            return self.get_Room(self.get_specialRoomsIndex()[9][0],self.get_specialRoomsIndex()[9][1])

    def get_specialRooms(self):
        return self._specialRooms

    def get_specialRoomsIndex(self):
        return self._specialRoomsIndex

    def view(self):
        viewTotal=""
        for i in range (self._size):
            listRoomLineView=[]
            for j in range (self._size):
                listRoomLineView.append(self._rooms[(i,j)].view())
            subListRoomLine1=""
            subListRoomLine2=""
            subListRoomLine3=""
            for i in listRoomLineView:
                subListRoomLine1 +=str(i[0:3])
                subListRoomLine2 +=str(i[3:6])
                subListRoomLine3 +=str(i[6:9])
            viewTotal+=subListRoomLine1+"\n"+subListRoomLine2+"\n"+subListRoomLine3+"\n"
        return viewTotal