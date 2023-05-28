### Estructura de una Funcion ###
from VarsTable import VarsTable

class Func:
    def __init__(self, name, type, parameters, size, varsTable, startAddress):
        self.name = name
        self.type = type
        self.parameters = parameters
        self.size = size
        self.varsTable = varsTable
        self.startAddress = startAddress