### Máquina Virtual que ejecuta el código objeto ###
from VirtualMemory import VirtualMemory
import re

obj = open("obj.a", "r")
text = obj.read().split()
memory = VirtualMemory()
counter = 0
# Se encarga de guardar las constantes
while(text[counter] != "%%"):
    address = text[counter]
    counter += 2
    if (text[counter] == f'"'):
        value = ""
        counter += 1
        while(text[counter] != f'"'):
            value += text[counter] + " "
            counter += 1

        memory.setValue(address, value)
        counter +=2
    else:
        value = text[counter]
        memory.setValue(address, value)
        counter +=2
counter += 1
# Se encarga de guardar las funciones
while(text[counter] != "%%"):
    address = text[counter]
    counter += 2
    size = text[counter].split(",")
    memory.setFunction(address, size)
    counter += 2

counter += 1
# Se encarga de guardar los cuadruplos
while(text[counter] != "%%"):
    quadruple = text[counter].split(",")
    memory.setQuadruple(quadruple)
    counter += 1

### Correr instrucciones ###
# Instruction pointer
ip = 0
ipStack = []
function = ""
while(memory.quadruples[ip][0] != "23"):
    operator = memory.operatorTranslator(memory.quadruples[ip][0])
    # Aplica la excepción de agrega la dirección base con el resultado de la operación del arreglo
    if (operator == "+dirb"):
        baseAddress = memory.quadruples[ip][2]
        leftO = memory.getValue(memory.quadruples[ip][1])
        result = memory.quadruples[ip][3]
        memory.setValue(result, (leftO + int(baseAddress)))
        ip += 1
    
    else:
        if ((memory.quadruples[ip][1] != '') and (int(memory.quadruples[ip][1]) >= 25000)):
            leftO = memory.getValue(memory.getValue(memory.quadruples[ip][1]))
        else:
            leftO = memory.getValue(memory.quadruples[ip][1])

        if ((memory.quadruples[ip][2] != '') and (int(memory.quadruples[ip][2]) >= 25000)):
            rightO = memory.getValue(memory.getValue(memory.quadruples[ip][2]))
        else:
            rightO = memory.getValue(memory.quadruples[ip][2])
        
        if ((memory.quadruples[ip][3] != '') and (int(memory.quadruples[ip][3]) >= 25000)):
            result = memory.getValue(memory.quadruples[ip][3])
        else:
            result = memory.quadruples[ip][3]

        if operator == "<":
            memory.setValue(result, str(leftO < rightO))
            ip += 1

        elif operator == ">":
            memory.setValue(result, str(leftO > rightO))
            ip += 1

        elif operator == "<=":
            memory.setValue(result, str(leftO <= rightO))
            ip += 1

        elif operator == ">=":
            memory.setValue(result, str(leftO >= rightO))
            ip += 1

        elif operator == "#=":
            memory.setValue(result, str(leftO == rightO))
            ip += 1

        elif operator == "!=":
            memory.setValue(result, str(leftO != rightO))
            ip += 1

        elif operator == "+":
            memory.setValue(result, str(leftO + rightO))
            ip += 1
        
        elif operator == "-":
            memory.setValue(result, str(leftO - rightO))
            ip += 1

        elif operator == "/":
            memory.setValue(result, str(leftO / rightO))
            ip += 1

        elif operator == "*":
            memory.setValue(result, str(leftO * rightO))
            ip += 1

        elif operator == "=":
            memory.setValue(result, str(leftO))
            ip += 1

        elif operator == "goto":
            ip = int(result)
        
        elif operator == "gotof":
            if not leftO:
                ip = int(result)
            else:
                ip += 1
        
        elif operator == "gotov":
            if leftO:
                ip = int(result)
            else:
                ip += 1

        elif operator == "read":
            temp = input()
            memory.setValue(result, temp)
            ip += 1

        elif operator == "write":
            print(memory.getValue(result), end=" ")
            ip += 1

        elif operator == "return":
            memory.setValue(result, str(leftO))
            ip += 1
        
        elif operator == "endfunc":
            memory.memoryStack.pop()
            for x in range(0, len(memory.functions[function])):
                memory.counters[x] -= int(memory.functions[function][x])
            ip = ipStack.pop()

        elif operator == "era":
            function = result
            for x in range(0, len(memory.functions[function])):
                memory.counters[x] += int(memory.functions[function][x])
                if (memory.counters[x] > 500):
                    print("Error: Stack Overflow of memory for modules")
                    exit()
            ip += 1

        elif operator == "parameter":
            memory.eraTemporary[result] = str(leftO)
            ip += 1

        elif operator == "gosub":
            memory.memoryStack.append(memory.eraTemporary)
            memory.eraTemporary = {}
            ipStack.append((ip + 1))
            ip = int(result)
        
        elif (operator == "ver"):
            exp = memory.getValue(result)
            if ((exp >= leftO) and (exp <= rightO)):
                ip += 1
            else:
                print("Array out of bounds")
                exit()