### Tabla de funciones ###
from Func import Func
from VarsTable import VarsTable
from FuncSize import FuncSize

class FuncTable:
    def __init__(self):
        #Diccionario de funciones
        self.table = {}

    def addFunc(self, name, type, parameters:list, size, varsTable:VarsTable, startAddress):
        if name in self.table:
            print("Function " + name + " has already been declared")
            exit()
        else:
            self.table[name] = Func(name, type, parameters, size, varsTable, startAddress)
    
    # Modifica la direccion inicial de una funcion
    def editFuncAddress(self, name, address):
        self.table[name].startAddress = address

    # Busca una variable en la tabla de variables de cada funcion
    def getVarAddress(self, name, scope):
        if scope in self.table:
            variable = self.table[scope].varsTable.searchVar(name, scope)
            if (variable == -1):
                variable = self.table["main"].varsTable.searchVar(name, "main")
                return variable.address
            else:
                return variable.address
        else:
            print("Scope " + scope + " not declared")
            exit()

    def getArrayDimension(self, name, scope):
        if scope in self.table:
            variable = self.table[scope].varsTable.searchVar(name, scope)
            if (variable == -1):
                variable = self.table["main"].varsTable.searchVar(name, "main")
                return variable.dim1
            else:
                return variable.dim1
        else:
            print("Scope " + scope + " not declared")
            exit()

    def getMatrixDimension(self, name, scope):
        if scope in self.table:
            variable = self.table[scope].varsTable.searchVar(name, scope)
            if (variable == -1):
                variable = self.table["main"].varsTable.searchVar(name, "main")
                return variable.dim2
            else:
                return variable.dim2
        else:
            print("Scope " + scope + " not declared")
            exit()

    def addParameter(self, name, scope):
        if scope in self.table:
            self.table[scope].parameters.append(name)
        else:
            print("Error: When trying to add parameter to list, the scope " + scope + " was not found")
            exit()

    ### Funcion que regresa el tipo de funcion que se envia ###
    def getFuncType(self, scope):
        if scope in self.table:
            funcType = self.table[scope].type
            return funcType
    
    ### Funcion que el size de la funcion
    def addFuncSize(self, scope, size:FuncSize):
        if scope in self.table:
            self.table[scope].size = size

    ### Funcion que busca un parametro y regresa la direccion ###
    def searchParameter(self, name, scope):
        if scope in self.table:
            variable = self.table[scope].varsTable.searchVar(name, scope)
            return variable.address
        else:
            print("Scope " + scope + " not declared in function call for parameter")
            exit()

    ### Funcion que regresa los identificadores de las funciones (su direccion inicial) con el size de todos los elementos que utilizaran ###
    def getAllFunc(self):
        result = []
        for funcName in self.table:
            if (funcName != "main"):
                func = f'{self.table[funcName].startAddress} : {self.table[funcName].size.returnElements()}'
                result.append(func)
            
        return result