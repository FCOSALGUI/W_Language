from ply.yacc import yacc
from lexer import *
from FuncTable import FuncTable
from Func import Func
from VarsTable import VarsTable
from Var import Var

from QuadList import QuadList
from Semantics import Semantics

### Sintaxis ###

# PROGRAM
def p_program(p):
    '''
    program : np_create_mainFunc np_set_scope_main var_dec df_dec modules MAIN np_set_goto_main LEFTCURLYBRACE body RIGHTCURLYBRACE END
            | empty
    '''
    if (len(p) == 9):
        p[0] = ('rule program: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    else:
        p[0] = ('rule program: ', p[1])

# VAR_DEC
def p_var_dec(p):
    '''
    var_dec : var_dec1 var_dec
            | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule var_dec: ', p[1], p[2])
    else:
        p[0] = ('rule var_dec: ', p[1])

def p_var_dec1(p):
    '''
    var_dec1 : VAR type ID np_add_variable var_dec2 SEMICOLON
             | var_dec3
             | var_dec4
             | empty
    '''
    if (len(p) == 6):
        p[0] = ('rule var_dec1: ', p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = ('rule var_dec1: ', p[1])

def p_var_dec2(p):
    '''
    var_dec2 : COMMA ID np_variable_same_type var_dec2
             | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule var_dec2: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule var_dec2: ', p[1])

def p_var_dec3(p):
    '''
    var_dec3 : VAR type ID LEFTBRACKET CTEINT RIGHTBRACKET SEMICOLON
             | empty
    '''
    if (len(p) == 8):
        p[0] = ('rule var_dec3: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        p[0] = ('rule var_dec3: ', p[1])

def p_var_dec4(p):
    '''
    var_dec4 : VAR type ID LEFTBRACKET CTEINT RIGHTBRACKET LEFTBRACKET CTEINT RIGHTBRACKET SEMICOLON
             | empty
    '''
    if (len(p) == 11):
        p[0] = ('rule var_dec4: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10])
    else:
        p[0] = ('rule var_dec4: ', p[1])

# DF_DEC
def p_df_dec(p):
    '''
    df_dec : df_dec1 df_dec
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule df_dec: ', p[1], p[2])
    else:
        p[0] = ('rule df_dec: ', p[1])

def p_df_dec1(p):
    '''
    df_dec1 : DATAFRAME ID LEFTBRACKET CTEINT RIGHTBRACKET EQUAL LEFTPARENTHESIS type ID df_dec2 RIGHTPARENTHESIS SEMICOLON
            | empty 
    '''
    if (len(p) == 13):
        p[0] = ('rule df_dec1: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])
    else:
        p[0] = ('rule df_dec1: ', p[1])

def p_df_dec2(p):
    '''
    df_dec2 : COMMA type ID df_dec2
            | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule df_dec2: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule df_dec2: ', p[1])

# MODULES
def p_modules(p):
    '''
    modules : modules1 modules
            | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule modules: ', p[1], p[2])
    else:
        p[0] = ('rule modules: ', p[1])

def p_modules1(p):
    '''
    modules1 : FUNC modules2 ID LEFTPARENTHESIS modules3 RIGHTPARENTHESIS LEFTCURLYBRACE var_dec body modules4 RIGHTCURLYBRACE
             | empty
    '''
    if (len(p) == 12):
        p[0] = ('rule modules1: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])
    else:
        p[0] = ('rule modules1: ', p[1])

def p_modules2(p):
    '''
    modules2 : type
             | VOID
    '''
    p[0] = ('rule modules2: ', p[1])

def p_modules3(p):
    '''
    modules3 : type ID modules5
             | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules3: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules3: ', p[1])

def p_modules4(p):
    '''
    modules4 : RETURN exp SEMICOLON
             | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules4: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules4: ', p[1])

def p_modules5(p):
    '''
    modules5 : COMMA type ID modules5
             | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule modules5: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule modules5: ', p[1])

# TYPE
def p_type(p):
    '''
    type : INT
         | FLOAT
         | CHAR
         | STRING
         | BOOL
    '''
    p[0] = ('rule type: ', p[1])

# BODY
def p_body(p):
    '''
    body : statement body
         | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule body: ', p[1], p[2])
    else:
        p[0] = ('rule body: ', p[1])

# STATEMENT
def p_statement(p):
    '''
    statement : assignment
              | df_assignment
              | condition
              | w_cycle
              | f_cycle
              | read
              | write
              | call
              | special_call
              | empty
    '''
    p[0] = ('rule statement: ', p[1])

# ASSIGNMENT
def p_assignment(p):
    '''
    assignment : variable np_push_id EQUAL np_push_operator_assignment exp np_pop_operator_assignment SEMICOLON
    '''
    p[0] = ('rule assignment: ', p[1], p[2], p[3], p[4])

# DF_ASSIGNMENT
def p_df_assignment(p):
    '''
    df_assignment : ID DOT PUSH LEFTPARENTHESIS exp df_assignment1 RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule df_assignment: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_df_assignment1(p):
    '''
    df_assignment1 : COMMA exp df_assignment1
                   | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule df_assignment1: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule df_assignment1: ', p[1])

# CONDITION
def p_condition(p):
    '''
    condition : IF LEFTPARENTHESIS exp RIGHTPARENTHESIS np_push_if LEFTCURLYBRACE body RIGHTCURLYBRACE condition1 np_conditional_end
    '''
    p[0] = ('rule condition: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_condition1(p):
    '''
    condition1 : ELSE np_push_else LEFTCURLYBRACE body RIGHTCURLYBRACE
               | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule condition1: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule condition1: ', p[1])

# W_CYCLE
def p_w_cycle(p):
    '''
    w_cycle : WHILE np_push_while LEFTPARENTHESIS exp RIGHTPARENTHESIS np_while_exp LEFTCURLYBRACE body RIGHTCURLYBRACE np_while_end
    '''
    p[0] = ('rule w_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# F_CYCLE
def p_f_cycle(p):
    '''
    f_cycle : FOR LEFTPARENTHESIS assignment np_push_for exp SEMICOLON exp RIGHTPARENTHESIS np_check_for LEFTCURLYBRACE body RIGHTCURLYBRACE np_for_end
    '''
    p[0] = ('rule f_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])

# READ
def p_read(p):
    '''
    read : READ np_push_rw LEFTPARENTHESIS variable np_push_id RIGHTPARENTHESIS SEMICOLON np_pop_rw
    '''
    p[0] = ('rule read: ', p[1], p[2], p[3], p[4], p[5])

# WRITE
def p_write(p):
    '''
    write : WRITE np_push_rw LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON np_pop_rw
    '''
    p[0] = ('rule write: ', p[1], p[2], p[3], p[4], p[5])

# CALL
def p_call(p):
    '''
    call : ID LEFTPARENTHESIS call1 RIGHTPARENTHESIS
         | ID LEFTPARENTHESIS call1 RIGHTPARENTHESIS SEMICOLON 
    '''
    if (len(p) == 4):
        p[0] = ('rule call: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call: ', p[1], p[2], p[3])

def p_call1(p):
    '''
    call1 : exp call2
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call1: ', p[1], p[2])
    else:
        p[0] = ('rule call1: ', p[1])

def p_call2(p):
    '''
    call2 : COMMA exp call2
          | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule call2: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call2: ', p[1])

# SPECIAL_CALL
def p_special_call(p):
    '''
    special_call : keys
                 | avg
                 | count
                 | max
                 | min
                 | sum
                 | plot
                 | histogram
                 | print
    '''
    p[0] = ('rule special_call: ', p[1])

# KEYS
def p_keys(p):
    '''
    keys : ID DOT KEYS LEFTPARENTHESIS RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule keys: ', p[1], p[2], p[3], p[4], p[5], p[6])

# AVG
def p_avg(p):
    '''
    avg : ID DOT AVG LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule avg: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# COUNT
def p_count(p):
    '''
    count : ID DOT COUNT LEFTPARENTHESIS RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule count: ', p[1], p[2], p[3], p[4], p[5], p[6])

# MAX
def p_max(p):
    '''
    max : ID DOT MAX LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule max: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# MIN
def p_min(p):
    '''
    min : ID DOT MIN LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule min: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# SUM
def p_sum(p):
    '''
    sum : ID DOT SUM LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule sum: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# PLOT
def p_plot(p):
    '''
    plot : ID DOT PLOT LEFTPARENTHESIS RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule plot: ', p[1], p[2], p[3], p[4], p[5], p[6])

# HISTOGRAM
def p_histogram(p):
    '''
    histogram : ID DOT HISTOGRAM LEFTPARENTHESIS RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule histogram: ', p[1], p[2], p[3], p[4], p[5], p[6])

# PRINT
def p_print(p):
    '''
    print : ID DOT PRINT LEFTPARENTHESIS print1 RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule print: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_print1(p):
    '''
    print1 : ID
           | empty
    '''
    p[0] = ('rule print1: ', p[1])

# VARIABLE
def p_variable(p):
    '''
    variable : ID variable1
    '''
    p[0] = ('rule variable: ', p[1], p[2])

def p_variable1(p):
    '''
    variable1 : LEFTBRACKET exp RIGHTBRACKET variable2
              | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule variable1: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule variable1: ', p[1])

def p_variable2(p):
    '''
    variable2 : LEFTBRACKET exp RIGHTBRACKET
              | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule variable2: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule variable2: ', p[1])

# EXP
def p_exp(p):
    '''
    exp : g_exp exp1
    '''
    p[0] = ('rule exp: ', p[1], p[2])

def p_exp1(p):
    '''
    exp1 : exp2 np_push_operator g_exp np_pop_operator_boolean
         | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule exp1: ', p[1], p[2])
    else:
        p[0] = ('rule exp1: ', p[1])

def p_exp2(p):
    '''
    exp2 : AND
         | OR
    '''
    p[0] = ('rule exp2: ', p[1])

# G-EXP
def p_g_exp(p):
    '''
    g_exp : m_exp g_exp1
    '''
    p[0] = ('rule g_exp: ', p[1], p[2])

def p_g_exp1(p):
    '''
    g_exp1 : g_exp2 np_push_operator m_exp np_pop_operator_c
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule g_exp1: ', p[1], p[2])
    else:
        p[0] = ('rule g_exp1: ', p[1])

def p_g_exp2(p):
    '''
    g_exp2 : LT
           | GT
           | LTOE
           | GTOE
           | E
           | NE
    '''
    p[0] = ('rule g_exp2: ', p[1])

# M-EXP
def p_m_exp(p):
    '''
    m_exp : t np_pop_operator_sr m_exp1
    ''' 
    p[0] = ('rule m_exp: ', p[1], p[2])

def p_m_exp1(p):
    '''
    m_exp1 : m_exp2 np_push_operator m_exp
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule m_exp1: ', p[1], p[2])
    else:
        p[0] = ('rule m_exp1: ', p[1])

def p_m_exp2(p):
    '''
    m_exp2 : MINUS
           | PLUS
    '''
    p[0] = ('rule m_exp2: ', p[1])

# T
def p_t(p):
    '''
    t : f np_pop_operator_md t1
    ''' 
    p[0] = ('rule t: ', p[1], p[2])

def p_t1(p):
    '''
    t1 : t2 np_push_operator t
       | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule t1: ', p[1], p[2])
    else:
        p[0] = ('rule t1: ', p[1])

def p_t2(p):
    '''
    t2 : DIVISION
       | MULTIPLICATION
    '''
    p[0] = ('rule t2: ', p[1])

# F
def p_f(p):
    '''
    f : LEFTPARENTHESIS np_create_temporal_operator_separator exp RIGHTPARENTHESIS np_delete_temporal_separator
      | CTEINT np_add_constant_int
      | CTEFLOAT np_add_constant_float
      | CTECHAR np_add_constant_char
      | CTESTRING np_add_constant_string
      | ctebool np_add_constant_bool
      | variable np_push_id
      | call
    '''
    if (len(p) == 4):
        p[0] = ('rule f: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule f: ', p[1])

def p_ctebool(p):
    '''
    ctebool : TRUE
            | FALSE
    '''
    p[0] = ('rule ctebool: ', p[1])
def p_empty(p):
     'empty :'
     pass

def p_error(p):
    print(f'Syntax error at {p.value!r} on line {p.lineno} of type {p}')
    exit()

### Creacion de estructuras principales ###
FunctionTable = FuncTable()
QuadrupleList = QuadList()

jumpStack = []
operatorStack = []
operandsStack = []
typeStack = []

scope = ""
varType = ""

### Direcciones Virtuales ###
# Globales
Gint = [5000, 5999]
Gfloat = [6000, 6999]
Gstring = [7000, 7999]
Gchar = [8000, 8999]
Gbool = [9000, 9999]

# Locales
Lint = [10000, 10999]
Lfloat = [11000, 11999]
Lstring = [12000, 12999]
Lchar = [13000, 13999]
Lbool = [14000, 14999]

# Temporales
Tint = [15000, 15999]
Tfloat = [16000, 16999]
Tstring = [17000, 17999]
Tchar = [18000, 18999]
Tbool = [19000, 19999]

# Constantes
Cint = [20000, 20999]
Cfloat = [21000, 21999]
Cstring = [22000, 22999]
Cchar = [23000, 23999]
Cbool = [24000, 24999]

### Contadores para variables ###
# Globales
CGint = 0
CGfloat = 0
CGstring = 0
CGchar = 0
CGbool = 0

# Locales
CLint = 0
CLfloat = 0
CLstring = 0
CLchar = 0
CLbool = 0

# Temporales
CTint = 0
CTfloat = 0
CTstring = 0
CTchar = 0
CTbool = 0

# Constantes
CCint = 0
CCfloat = 0
CCstring = 0
CCchar = 0
CCbool = 0

### Cubo Semantico ###
semanticCube = Semantics()

### Puntos neuralgicos ###
def p_np_set_scope_main(p):
    '''
    np_set_scope_main : empty
    '''
    global scope
    scope = "main"

def p_np_create_mainFunc(p):
    '''
    np_create_mainFunc : empty
    '''
    vTable = VarsTable()
    FunctionTable.addFunc("main", "main", None, None, vTable, None)
    jumpStack.append(0)
    QuadrupleList.addQuad("goto", None, None, None)

### Guardar variables ###
def p_np_add_variable(p):
    '''
    np_add_variable : empty
    '''
    global varType
    varType = p[-2][1]
    name = p[-1]
    addVariable(varType, name)

def p_np_variable_same_type(p):
    '''
    np_variable_same_type : empty
    '''
    name = p[-1]
    addVariable(varType, name)

def p_np_set_goto_main(p):
    '''
    np_set_goto_main : empty
    '''
    global scope
    scope = "main"
    address = jumpStack.pop()
    QuadrupleList.editQuadGoto(address, len(QuadrupleList.list))

#//TODO: Agregar funcionalidad para guardar direcciones de arreglos
def p_np_push_id(p):
    '''
    np_push_id : empty
    '''
    name = p[-1][1]
    address = FunctionTable.searchVar(name, scope)
    varType = determineVarType(address)

    operandsStack.append(address)
    typeStack.append(varType)

### Guardar Constantes ###
Constants = VarsTable()

def p_np_add_constant_int(p):
    '''
    np_add_constant_int : empty
    '''
    global CCint
    address = Cint[0] + CCint
    name = p[-1]
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1
    
    operand = Constants.searchVar(name)
    operandsStack.append(operand.address)
    typeStack.append("int")

def p_np_add_constant_float(p):
    '''
    np_add_constant_float : empty
    '''
    global CCfloat
    address = Cfloat[0] + CCfloat
    name = p[-1]
    if (address > Cfloat[1]):
        print("Stack overflow of constant floats for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCfloat += 1

    operand = Constants.searchVar(name)
    operandsStack.append(operand.address)
    typeStack.append("float")

def p_np_add_constant_char(p):
    '''
    np_add_constant_char : empty
    '''
    global CCchar
    address = Cchar[0] + Cchar
    name = p[-1]
    if (address > Cchar[1]):
        print("Stack overflow of constant chars for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCchar += 1

    operand = Constants.searchVar(name)
    operandsStack.append(operand.address)
    typeStack.append("char")

def p_np_add_constant_string(p):
    '''
    np_add_constant_string : empty
    '''
    global CCstring
    address = Cstring[0] + Cstring
    name = p[-1]
    if (address > Cstring[1]):
        print("Stack overflow of constant strings for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCstring += 1

    operand = Constants.searchVar(name)
    operandsStack.append(operand.address)
    typeStack.append("string")

def p_np_add_constant_bool(p):
    '''
    np_add_constant_bool : empty
    '''
    global CCbool
    address = Cbool[0] + Cbool
    name = p[-1]
    if (address > Cbool[1]):
        print("Stack overflow of constant bools for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCbool += 1

    operand = Constants.searchVar(name)
    operandsStack.append(operand.address)
    typeStack.append("bool")

### Puntos neuralgicos para estatutos lineales ###
def p_np_push_operator(p):
    '''
    np_push_operator : empty
    '''
    operator = p[-1][1]
    operatorStack.append(operator)

def p_np_push_operator_assignment(p):
    '''
    np_push_operator_assignment : empty
    '''
    operator = p[-1]
    operatorStack.append(operator)

def p_np_pop_operator_assignment(p):
    '''
    np_pop_operator_assignment : empty
    '''
    if(len(operatorStack) > 0):
        if(operatorStack[-1] == "="):
            assign()

### Funcion que asigna un valor a una variable (crea el cuadrupo de asignacion) ###           
def assign():
    expAddress = operandsStack.pop()
    expType = typeStack.pop()

    resultAddress = operandsStack.pop()
    resultType = typeStack.pop()

    operator = operatorStack.pop()

    if (expType == resultType):
        QuadrupleList.addQuad(operator, expAddress, None, resultAddress)
    else:
        print("Type mismatch when assigning a value to a variable for address: " + str(resultAddress))
        exit()

def p_np_pop_operator_boolean(p):
    '''
    np_pop_operator_boolean : empty
    '''
    if(len(operatorStack) > 0):
        if((operatorStack[-1] == "&&")
           or (operatorStack[-1] == "||")):
            pushTemporal()

def p_np_pop_operator_md(p):
    '''
    np_pop_operator_md : empty
    '''
    if(len(operatorStack) > 0):
        if((operatorStack[-1] == "*") or (operatorStack[-1] == "/")):
            pushTemporal()

def p_np_pop_operator_sr(p):
    '''
    np_pop_operator_sr : empty
    '''
    if(len(operatorStack) > 0):
        if((operatorStack[-1] == "+") or (operatorStack[-1] == "-")):
            pushTemporal()

def p_np_pop_operator_c(p):
    '''
    np_pop_operator_c : empty
    '''
    if(len(operatorStack) > 0):
        if((operatorStack[-1] == "<")
           or (operatorStack[-1] == ">")
           or (operatorStack[-1] == "<=")
           or (operatorStack[-1] == ">=")
           or (operatorStack[-1] == "==")
           or (operatorStack[-1] == "!=")):
            pushTemporal()

### Funcion que calcula la direccion de un temporal, crea el cuadruplo y pushea la direccion temporal a la pila de operandos ###
def pushTemporal():
    rightAddress = operandsStack.pop()
    rightType = typeStack.pop()

    leftAddress = operandsStack.pop()
    leftType = typeStack.pop()

    operator = operatorStack.pop()

    resultType = semanticCube.resultType(operator, leftType, rightType)
    resultAdress = determineTempAdress(resultType)

    QuadrupleList.addQuad(operator, leftAddress, rightAddress, resultAdress)
    operandsStack.append(resultAdress)
    typeStack.append(resultType)

### Puntos neuralgicos que crean un separador en la pila de operadores cuando se encuentra un paréntesis
def p_np_create_temporal_operator_separator(p):
    '''
    np_create_temporal_operator_separator : empty
    '''
    operatorStack.append("s")
    
def p_np_delete_temporal_separator(p):
    '''
    np_delete_temporal_separator : empty
    '''
    if(operatorStack[-1] == "s"):
        operatorStack.pop()

### Funcion para agregar variables a la tabla de variables ###
# //TODO: Agregar funcionalidad para guardar variables locales luego de cambiar el scope a una funcion
def addVariable(varType, name):
    address = 0
    if(scope == "main"):
        if (varType == "int"):
            global CGint
            address = Gint[0] + CGint
            if (address > Gint[1]):
                print("Stack overflow of global integers for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CGint += 1       
        
        elif (varType == "float"):
            global CGfloat
            address = Gfloat[0] + CGfloat
            if (address > Gfloat[1]):
                print("Stack overflow of global floats for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CGfloat += 1

        elif (varType == "string"):
            global CGstring
            address = Gstring[0] + CGstring
            if (address > Gstring[1]):
                print("Stack overflow of global strings for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CGstring += 1
        
        elif (varType == "char"):
            global CGchar
            address = Gchar[0] + CGchar
            if (address > Gchar[1]):
                print("Stack overflow of global chars for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CGchar += 1

        elif (varType == "bool"):
            global CGbool
            address = Gbool[0] + CGbool
            if (address > Gbool[1]):
                print("Stack overflow of global bools for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CGbool += 1             

### Puntos Neuralgicos if y else ###
def p_np_push_if(p):
    '''
    np_push_if : empty
    '''
    expType = typeStack.pop()
    if (expType != "bool"):
        print("Type mismatch at if evaluation, it is not a boolean")
        exit()
    else:
        result = operandsStack.pop()
        QuadrupleList.addQuad("gotof", result, None, None)
        jumpStack.append(len(QuadrupleList.list) - 1)

def p_np_push_else(p):
    '''
    np_push_else : empty
    '''
    QuadrupleList.addQuad("goto", None, None, None)
    falseJump = jumpStack.pop()
    jumpStack.append(len(QuadrupleList.list) - 1)
    QuadrupleList.editQuadGoto(falseJump, len(QuadrupleList.list))

def p_np_conditional_end(p):
    '''
    np_conditional_end : empty
    '''
    endJump = jumpStack.pop()
    QuadrupleList.editQuadGoto(endJump, len(QuadrupleList.list))

### Puntos neuralgicos while ###
def p_np_push_while(p):
    '''
    np_push_while : empty
    '''
    jumpStack.append(len(QuadrupleList.list))

def p_np_while_exp(p):
    '''
    np_while_exp : empty
    '''
    expType = typeStack.pop()
    if (expType != "bool"):
        print("Type mismatch at while evaluation, it is not a boolean")
        exit()
    else:
        result = operandsStack.pop()
        QuadrupleList.addQuad("gotof", result, None, None)
        jumpStack.append(len(QuadrupleList.list) - 1)

def p_np_while_end(p):
    '''
    np_while_end : empty
    '''
    endJump = jumpStack.pop()
    returnJump = jumpStack.pop()
    QuadrupleList.addQuad("goto", None, None, returnJump)
    QuadrupleList.editQuadGoto(endJump, len(QuadrupleList.list))

### Puntos neuralgicos for ###
#TODO: Hacer puntos neuralgicos para el FOR

# El que suma, resta o multiplica
def p_np_push_for(p):
    '''
    np_push_for : empty
    '''
    jumpStack.append(len(QuadrupleList.list))

def p_np_check_for(p):
    '''
    np_check_for : empty
    '''
    expTypeBoolean = typeStack.pop()
    if (expTypeBoolean != "bool"):
        print("Type mismatch at for boolean component, it is not boolean")
        exit()
    else:
        expTypeInteger = typeStack.pop()
        if (expTypeInteger != "int"):
            print("Type mismatch at for integer component, it is not integer")
            exit()
        else:
            resultBoolean = operandsStack.pop()
            QuadrupleList.addQuad("gotof", resultBoolean, None, None)
            jumpStack.append(len(QuadrupleList.list) - 1)
            operandsStack.pop()

def p_np_for_end(p):
    '''
    np_for_end : empty
    '''
    falseJump = jumpStack.pop()
    returnJump = jumpStack.pop()

    QuadrupleList.addQuad("goto", None, None, returnJump)
    QuadrupleList.editQuadGoto(falseJump, len(QuadrupleList.list))

### Puntos neuralgicos read y write ###
def p_np_push_rw(p):
    '''
    np_push_rw : empty
    '''
    operator = p[-1]
    operatorStack.append(operator)

def p_np_pop_rw(p):
    '''
    np_pop_rw : empty
    '''
    operator = operatorStack.pop()
    typeStack.pop()
    result = operandsStack.pop()

    QuadrupleList.addQuad(operator, None, None, result)

### Funcion que determina el tipo de variable dependiendo de su direccion virtual ###
def determineVarType(address):
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

### Funcion que calcula en que direccion sera agregada una temporal ###
def determineTempAdress(resultType):
    address = 0
    if (resultType == "int"):
        global CTint
        address = Tint[0] + CTint
        if (address > Tint[1]):
            print("Stack overflow of temporal integers")
            exit()
        else:
            CTint += 1
            return address

    elif (resultType == "float"):
        global CTfloat
        address = Tfloat[0] + CTfloat
        if (address > Tfloat[1]):
            print("Stack overflow of temporal floats")
            exit()
        else:
            CTfloat += 1
            return address
        
    elif (resultType == "string"):
        global CTstring
        address = Tstring[0] + CTstring
        if (address > Tstring[1]):
            print("Stack overflow of temporal strings")
            exit()
        else:
            CTstring += 1
            return address
        
    elif (resultType == "char"):
        global CTchar
        address = Tchar[0] + CTchar
        if (address > Tchar[1]):
            print("Stack overflow of temporal chars")
            exit()
        else:
            CTchar += 1
            return address
        
    elif (resultType == "bool"):
        global CTbool
        address = Tbool[0] + CTbool
        if (address > Tbool[1]):
            print("Stack overflow of temporal bools")
            exit()
        else:
            CTbool += 1
            return address

parser = yacc()

file = open("prueba.w", "r")
content = file.read()
result = parser.parse(content)

'''for x in range(0,len(QuadrupleList.list)):
    print(str(x) + ".- " + QuadrupleList.list[x].toString())

print(operatorStack)
print(operandsStack)
print(typeStack)
print(jumpStack)

print(len(QuadrupleList.list))'''

#print(FunctionTable.table["main"].varsTable.table["cosa1"].address)
#print(QuadrupleList.list[0].toString())