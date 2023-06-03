### Tabla de variables ###
from Var import *

class VarsTable:
    def __init__(self):
        #Diccionario para buscar y acceder a las variables
        self.table = {}

    def addVar(self, name, address):
        newVar = Var(name, address, None, None)

        if name in self.table:
            print("Variable " + name + " has already been declared")
            exit()
            
        else:
            self.table[name] = newVar

    def addArray(self, name, initialAddress, dim1):
        newArray = Var(name, initialAddress, dim1, None)

        if name in self.table:
            print("Array " + name + " has already been declared")
            exit()
            
        else:
            self.table[name] = newArray

    def addMatrix(self, name, initialAddress, dim1, dim2):
        newArray = Var(name, initialAddress, dim1, dim2)

        if name in self.table:
            print("Matrix " + name + " has already been declared")
            exit()
            
        else:
            self.table[name] = newArray
    
    def addConstant(self, name, address):
        newVar = Var(name, address, None, None)
        if name not in self.table:
            self.table[name] = newVar
        
    def searchVar(self, name, scope):
        if (scope == "main"):
            if name in self.table:
                return self.table[name]
                
            else:
                print("Variable " + name + " has not been declared")
                exit()
        
        else:
            if name in self.table:
                return self.table[name]
            else:
                return -1
    
    ### Funcion que regresa una lista de constantes en formato string para ser escritas en el archivo obj ###
    def getConstants(self):
        result = []
        for var in self.table:
            result.append(f'{self.table[var].address} : {var}')

        return result
