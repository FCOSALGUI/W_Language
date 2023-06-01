### Estructura de un cuadruplo ###
class Quad:
    def __init__(self, operator, lOperand, rOperand, result):
        self.operator = operator

        if (lOperand == None):
            self.lOperand = ""
        else:
            self.lOperand = lOperand
    
        if (rOperand == None):
            self.rOperand = ""
        else:
            self.rOperand = rOperand
        self.result = result
        if (result == None):
            self.result = ""
        else:
            self.result = result
    
    def toString(self):
        Quadruple = f"{self.operator},{self.lOperand},{self.rOperand},{self.result}"
        return Quadruple