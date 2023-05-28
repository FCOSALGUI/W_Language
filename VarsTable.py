### Tabla de variables ###
from Var import *

class VarsTable:
    def __init__(self):
        #Diccionario para buscar y acceder a las variables
        self.table = {}
        '''Contador de variables de cada tipo
        self.int = 0
        self.float = 0
        self.string = 0
        self.char = 0
        self.bool = 0'''

    def addVar(self, name, address):
        newVar = Var(name, address)

        if name in self.table:
            print("Variable " + name + " has already been declared")
            exit()
            
        else:
            self.table[name] = newVar
    
    def addConstant(self, name, address):
        newVar = Var(name, address)
        if name not in self.table:
            self.table[name] = newVar
        
    def searchVar(self, name):
        if name in self.table:
            return self.table[name]
            
        else:
            print("Variable " + name + " has not been declared")
            exit()
            return None