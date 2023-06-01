### Estructura que se encarga de manejar la memoria virtual de la máquina virtual y de guardar los resultados ###

class VirtualMemory:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.quadruples = []
        self.memoryStack = []

    def setValue(self, address, value):
        if (len(self.memoryStack) > 0):
            scope = self.determineScope(int(address))
            if (scope == "local"):
                self.memoryStack[-1][address] = value
            elif (scope == "global"):
                self.variables[address] = value
        else:
            self.variables[address] = value

    def getValue(self, address):
        if address != '':
            if (len(self.memoryStack) > 0):
                scope = self.determineScope(int(address))
                if (scope == "local"):
                    if address in self.memoryStack[-1]:
                        value = self.memoryStack[-1][address]
                        valueType = self.determineVarType(int(address))

                        if(valueType == "int"):
                            return int(value)
                        elif(valueType == "float"):
                            return float(value)
                        elif(valueType == "bool"):
                            if(value.lower() == "true"):
                                return True
                            elif(value.lower() == "false"):
                                return False            
                    else:
                        print(f'Address {address} does not have a value assigned to it \n Make sure all variables have values assigned to them in your code!')
                        exit()

                elif (scope == "global"):
                    if address in self.variables:
                        value = self.variables[address]
                        valueType = self.determineVarType(int(address))

                        if(valueType == "int"):
                            return int(value)
                        elif(valueType == "float"):
                            return float(value)
                        elif(valueType == "bool"):
                            if(value.lower() == "true"):
                                return True
                            elif(value.lower() == "false"):
                                return False            
                    else:
                        print(f'Address {address} does not have a value assigned to it \n Make sure all variables have values assigned to them in your code!')
                        exit()
            else:    
                if address in self.variables:
                    value = self.variables[address]
                    valueType = self.determineVarType(int(address))

                    if(valueType == "int"):
                        return int(value)
                    elif(valueType == "float"):
                        return float(value)
                    elif(valueType == "bool"):
                        if(value.lower() == "true"):
                            return True
                        elif(value.lower() == "false"):
                            return False            
                else:
                    print(f'Address {address} does not have a value assigned to it \n Make sure all variables have values assigned to them in your code!')
                    exit()
        else:
            return ''

    def setFunction(self, address, values:list):
        self.functions[address] = values

    def setQuadruple(self, quadruple:list):
        self.quadruples.append(quadruple)

    def operatorTranslator(self, operator):
        if operator == "1":
            return "<"
        elif operator == "2":
            return ">"
        elif operator == "3":
            return "<="
        elif operator == "4":
            return ">="
        elif operator == "5":
            return "=="
        elif operator == "6":
            return "!="
        elif operator == "7":
            return "+"
        elif operator == "8":
            return "-"
        elif operator == "9":
            return "/"
        elif operator == "10":
            return "*"
        elif operator == "11":
            return "="
        elif operator == "12":
            return "goto"
        elif operator == "13":
            return "gotof"
        elif operator == "14":
            return "gotov"
        elif operator == "15":
            return "read"
        elif operator == "16":
            return "write"
        elif operator == "17":
            return "return"
        elif operator == "18":
            return "endfunc"
        elif operator == "19":
            return "era"
        elif operator == "20":
            return "parameter"
        elif operator == "21":
            return "gosub"
        elif operator == "22":
            return "ver"
        elif operator == "23":
            return "end"
        
    @staticmethod
    def determineVarType(address:int):
        if(((address >= 5000) and (address <= 5999))
        or ((address >= 10000) and (address <= 10999))
        or ((address >= 15000) and (address <= 15999))
        or ((address >= 20000) and (address <= 20999))):
            return "int"
        elif(((address >= 6000) and (address <= 6999))
        or ((address >= 11000) and (address <= 11999))
        or ((address >= 16000) and (address <= 16999))
        or ((address >= 21000) and (address <= 21999))):
            return "float"
        elif(((address >= 7000) and (address <= 7999))
        or ((address >= 12000) and (address <= 12999))
        or ((address >= 17000) and (address <= 17999))
        or ((address >= 22000) and (address <= 22999))):
            return "string"
        elif(((address >= 8000) and (address <= 8999))
        or ((address >= 13000) and (address <= 13999))
        or ((address >= 18000) and (address <= 18999))
        or ((address >= 23000) and (address <= 23999))):
            return "char"
        elif(((address >= 9000) and (address <= 9999))
        or ((address >= 14000) and (address <= 14999))
        or ((address >= 19000) and (address <= 19999))
        or ((address >= 24000) and (address <= 24999))):
            return "bool"
        
    @staticmethod
    def determineScope(address:int):
        if ((address >= 10000) and (address <=19999)):
            return "local"
        else:
            return "global"
        