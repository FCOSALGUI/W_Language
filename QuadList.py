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
        if operator == "<":
            return 1
        
        elif operator == ">":
            return 2
        
        elif operator == "<=":
            return 3
        
        elif operator == ">=":
            return 4
        
        elif operator == "==":
            return 5
        
        elif operator == "!=":
            return 6
        
        elif operator == "+":
            return 7
        
        elif operator == "-":
            return 8
        
        elif operator == "/":
            return 9
        
        elif operator == "*":
            return 10
        
        elif operator == "=":
            return 11

        elif operator == "goto":
            return 12
    
    # Funcion que completa el cuadruplo de Goto cuando sabe a que direccion ir
    def editQuadGoto(self, address, jumpTo):
        self.list[address].result = jumpTo
