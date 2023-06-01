### Máquina Virtual que ejecuta el código objeto ###
from VirtualMemory import VirtualMemory

obj = open("obj.a", "r")
text = obj.read().split()
memory = VirtualMemory()
counter = 0
# Se encarga de guardar las constantes
while(text[counter] != "%%"):
    address = text[counter]
    counter += 2
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
while(memory.quadruples[ip][0] != "23"):
    operator = memory.operatorTranslator(memory.quadruples[ip][0])
    leftO = memory.getValue(memory.quadruples[ip][1])
    rightO = memory.getValue(memory.quadruples[ip][2])
    result = memory.quadruples[ip][3]

    if operator == "<":
        memory.setValue(result, str(leftO < rightO))

    elif operator == ">":
        memory.setValue(result, str(leftO > rightO))

    elif operator == "<=":
        memory.setValue(result, str(leftO <= rightO))

    elif operator == ">=":
        memory.setValue(result, str(leftO >= rightO))

    elif operator == "==":
        memory.setValue(result, str(leftO == rightO))

    elif operator == "!=":
        memory.setValue(result, str(leftO != rightO))

    elif operator == "+":
        memory.setValue(result, str(leftO + rightO))
    
    elif operator == "-":
        memory.setValue(result, str(leftO - rightO))

    elif operator == "/":
        memory.setValue(result, str(leftO / rightO))

    elif operator == "*":
        memory.setValue(result, str(leftO * rightO))

    elif operator == "=":
        memory.setValue(result, leftO)

    elif operator == "goto":
        ip = result
    
    elif operator == "gotof":
        if not leftO:
            ip = result
    
    elif operator == "gotov":
        if leftO:
            ip = result

    elif operator == "read":
        temp = input()
        memory.setValue(result, temp)

    elif operator == "write":
        print(result)

    elif operator == "return":
        memory.setValue(result, leftO)
    
    elif operator == "endfunc":
        ip = ipStack.pop()
        memory.memoryStack.pop()

    elif operator == "era":
        memory.memoryStack.append({})

    elif operator == "parameter":
        memory.setValue(result, leftO)

    elif operator == "gosub":
        ipStack.append(ip)
        ip = result