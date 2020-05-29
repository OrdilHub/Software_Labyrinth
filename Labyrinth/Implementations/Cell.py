from Services.ICell import ICell
from Implementations.CellTypes import CellTypes
from Implementations.SideTypes import SideTypes

class Cell(ICell):

    def __init__(self,posX:int,posY:int,cellType:CellTypes,valueGeneration:int, sideN:SideTypes, sideO:SideTypes, sideE:SideTypes, sideS:SideTypes):
        self._posX=posX
        self._posY=posY
        self._cellType=cellType
        self._valueGeneration=valueGeneration
        self._sideS=sideS
        self._sideN=sideN
        self._sideE=sideE
        self._sideO=sideO

    def get_posX(self):
        return self._posX
    def get_posY(self):
        return self._posY
    def get_cellType(self):
        return self._cellType
    def get_valueGeneration(self):
        return self._valueGeneration
    def get_sideS(self):
        return self._sideS
    def get_sideN(self):
        return self._sideN
    def get_sideE(self):
        return self._sideE
    def get_sideO(self):
        return self._sideO

    def is_Equal(self,destinationx,destinationy):
        return (self.get_posX()==destinationx and self.get_posY()==destinationy)

    def set_sideN(self,type:SideTypes):
        self._sideN=type
    def set_sideO(self,type:SideTypes):
        self._sideO=type
    def set_sideE(self,type:SideTypes):
        self._sideE=type
    def set_sideS(self,type:SideTypes):
        self._sideS=type
    def set_valueGeneration(self,newValue:int):
        self._valueGeneration=newValue

    def get_wall(self):
        listWall=[]
        listWall.append(self.get_sideN()==SideTypes.WALL)
        listWall.append(self.get_sideO()==SideTypes.WALL)
        listWall.append(self.get_sideE()==SideTypes.WALL)
        listWall.append(self.get_sideS()==SideTypes.WALL)
        return listWall

    def get_monolith(self):
        listMonolith=[]
        listMonolith.append(self.get_sideN()==SideTypes.END)
        listMonolith.append(self.get_sideO()==SideTypes.END)
        listMonolith.append(self.get_sideE()==SideTypes.END)
        listMonolith.append(self.get_sideS()==SideTypes.END)
        return listMonolith

    def view(self):
        printed=""
        if self.get_sideN()==SideTypes.NONE:
            printed=printed+"- -"
        if self.get_sideN()==SideTypes.END:
            printed=printed+"-#-"
        if self.get_sideN()==SideTypes.WALL:
            printed=printed+"-x-"



        if self.get_sideO()==SideTypes.END:
            printed=printed+"#"
        if self.get_sideO()==SideTypes.WALL:
            printed=printed+"x"
        if self.get_sideO()==SideTypes.NONE:
            printed=printed+" "

        if self.get_cellType()==CellTypes.FREE:
            printed=printed+" "
        if self.get_cellType()==CellTypes.EXIT:
            printed=printed+"%"
        if self.get_cellType()==CellTypes.LOOT:
            printed=printed+"ø"
        if self.get_cellType()==CellTypes.TP1 or self.get_cellType()==CellTypes.TP2 or self.get_cellType()==CellTypes.TP3 or self.get_cellType()==CellTypes.TP4 or self.get_cellType()==CellTypes.TP5:
            printed=printed+"@"

        if self.get_sideE()==SideTypes.END:
            printed=printed+"#"
        if self.get_sideE()==SideTypes.WALL:
            printed=printed+"x"
        if self.get_sideE()==SideTypes.NONE:
            printed=printed+" "

        if self.get_sideS()==SideTypes.END:
            printed=printed+"-#-"
        if self.get_sideS()==SideTypes.WALL:
            printed=printed+"-x-"
        if self.get_sideS()==SideTypes.NONE:
            printed=printed+"- -"
        return printed


