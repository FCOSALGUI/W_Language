### Tabla de funciones ###
from Func import Func
from VarsTable import VarsTable

class FuncTable:
    def __init__(self):
        #Diccionario de funciones
        self.table = {}

    def addFunc(self, name, type, parameters, size, varsTable, startAddress):
        if name in self.table:
            print("Function " + name + " has already been declared")
            exit()
        else:
            self.table[name] = Func(name, type, parameters, size, varsTable, startAddress)
    
    # Modifica la direccion inicial de una funcion
    def editFuncAddress(self, name, address):
        self.table[name].startAddress = address

    # Busca una variable en la tabla de variables de cada funcion
    # //TODO: Agregar funcionalidad para buscar en otros scopes (de forma local) para luego buscar en variables globales
    def searchVar(self, name, scope):
        if(scope == "main"):
            variable = self.table[scope].varsTable.searchVar(name)
            return variable.address




