### Estructura que alberga cuadruplos antes de ser escritos en archivo objeto ###
from Quad import Quad

class QuadList:
    def __init__(self):
        self.list = []

    def addQuad(self, operator, lOperand, rOperand, result):
        Quadruple = Quad(self.operatorTranslator(operator), lOperand, rOperand, result)
        self.list.append(Quadruple)
        
    
    # Transforma los operadores en numeros que luego la maquina virtual usara para resolver los cuadruplos
    @staticmethod
    def operatorTranslator(operator):
        if operator == "goto":
            return 12
    
    # Funcion que completa el cuadruplo de Goto cuando sabe a que direccion ir
    def editQuadGoto(self, address, jumpTo):
        self.list[address].result = jumpTo
