from ply.yacc import yacc
from lexer import *
from FuncTable import FuncTable
from Func import Func
from FuncSize import FuncSize
from VarsTable import VarsTable
from Var import Var

from QuadList import QuadList
from Semantics import Semantics

import os

### Sintaxis ###

# PROGRAM
def p_program(p):
    '''
    program : np_create_mainFunc np_set_scope_main var_dec df_dec modules MAIN np_set_goto_main np_reset_counters LEFTCURLYBRACE body RIGHTCURLYBRACE END np_end_program
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
    var_dec3 : VAR type ID LEFTBRACKET CTEINT RIGHTBRACKET SEMICOLON np_add_array
             | empty
    '''
    if (len(p) == 8):
        p[0] = ('rule var_dec3: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    else:
        p[0] = ('rule var_dec3: ', p[1])

def p_var_dec4(p):
    '''
    var_dec4 : VAR type ID LEFTBRACKET CTEINT RIGHTBRACKET LEFTBRACKET CTEINT RIGHTBRACKET SEMICOLON np_add_matrix
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
    modules1 : FUNC modules2 ID np_create_module np_set_scope_module LEFTPARENTHESIS modules3 RIGHTPARENTHESIS var_dec LEFTCURLYBRACE body modules4 RIGHTCURLYBRACE np_end_module np_reset_counters
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
    modules3 : type ID np_add_parameter modules5
             | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules3: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules3: ', p[1])

def p_modules4(p):
    '''
    modules4 : RETURN exp SEMICOLON np_create_return
             | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules4: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules4: ', p[1])

def p_modules5(p):
    '''
    modules5 : COMMA type ID np_add_parameter modules5
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
    f_cycle : FOR LEFTPARENTHESIS assignment np_push_for assignment np_for_jump exp RIGHTPARENTHESIS np_check_for LEFTCURLYBRACE body RIGHTCURLYBRACE np_for_end
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
def p_call_exp(p):
    '''
    call_exp : ID np_verify_call LEFTPARENTHESIS np_generate_era call1 RIGHTPARENTHESIS np_end_call
    '''

def p_call(p):
    '''
    call : ID np_verify_call LEFTPARENTHESIS np_generate_era call1 RIGHTPARENTHESIS np_end_call SEMICOLON 
    '''
    if (len(p) == 4):
        p[0] = ('rule call: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call: ', p[1], p[2], p[3])

def p_call1(p):
    '''
    call1 : exp np_push_parameter call2
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call1: ', p[1], p[2])
    else:
        p[0] = ('rule call1: ', p[1])

def p_call2(p):
    '''
    call2 : COMMA exp np_push_parameter call2
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
      | call_exp
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

# Apuntadores de arreglos
Tpointers = [25000, 25999]

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

# Apuntadores de arreglos
CTpointers = 0

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

### Puntos neuralgicos para funciones ###
def p_np_create_module(p):
    '''
    np_create_module : empty
    '''
    vTable = VarsTable()
    if (p[-2][1] == "void"):
        funcType = p[-2][1]
    else:
        funcType = p[-2][1][1]
    
    funcName = p[-1]
    address = len(QuadrupleList.list)
    
    FunctionTable.addFunc(funcName, funcType, [], None, vTable, address)
    
def p_np_set_scope_module(p):
    '''
    np_set_scope_module : empty
    '''
    global scope
    scope = p[-2]

def p_np_add_parameter(p):
    '''
    np_add_parameter : empty
    '''
    global varType
    varType = p[-2][1]
    name = p[-1]
    addVariable(varType, name)
    FunctionTable.addParameter(name, scope)

def p_np_reset_counters(p):
    '''
    np_reset_counters : empty
    '''
    global CLint
    CLint = 0
    global CLfloat
    CLfloat = 0
    global CLstring
    CLstring = 0
    global CLchar
    CLchar = 0
    global CLbool
    CLbool = 0
    global CTint
    CTint = 0
    global CTfloat
    CTfloat = 0
    global CTstring
    CTstring = 0
    global CTchar
    CTchar = 0
    global CTbool
    CTbool = 0
    global CTpointers
    CTpointers = 0

def p_np_create_return(p):
    '''
    np_create_return : empty
    '''
    operandType = typeStack.pop()
    operand = operandsStack.pop()

    funcType = FunctionTable.getFuncType(scope)
    if (funcType == "void"):
        print("Error: The void function " + scope + " has a return expression")
        exit()
    else:
        if (funcType == operandType):
            QuadrupleList.addQuad("return", operand, None, FunctionTable.table[scope].startAddress)
        else:
            print("Error: Return expression for function " + scope + " is not the same as the function type")
            exit()

def p_np_end_module(p):
    '''
    np_end_module : empty
    '''
    quad = QuadrupleList.list[len(QuadrupleList.list) - 1]
    funcType = FunctionTable.getFuncType(scope)
    if ((funcType == "void")):
        if (quad.operator != 17):
            size = FuncSize(CLint, CLfloat, CLstring, CLchar, CLbool, CTint, CTfloat, CTstring, CTchar, CTbool, CTpointers)
            FunctionTable.addFuncSize(scope, size)
            QuadrupleList.addQuad("endfunc", None, None, None)
        else: 
            print("Error: The void function " + scope + " has a return expression")
            exit()
    else:
        if(quad.operator == 17):
            size = FuncSize(CLint, CLfloat, CLstring, CLchar, CLbool, CTint, CTfloat, CTstring, CTchar, CTbool, CTpointers)
            FunctionTable.addFuncSize(scope, size)
            QuadrupleList.addQuad("endfunc", None, None, None)
        else:
            print("Error: Return expression for function " + scope + " is not declared")
            exit()

### Puntos neuralgicos de las llamadas a funciones ###
parameterCounter = 0
def p_np_verify_call(p):
    '''
    np_verify_call : empty
    '''
    name = p[-1]
    if name not in FunctionTable.table:
        print("Error: Function ID with name" + name + "not declared")
        exit()
    
def p_np_generate_era(p):
    '''
    np_generate_era : empty
    '''
    global parameterCounter
    parameterCounter = 0
    funcName = p[-3]
    startAddress = FunctionTable.table[funcName].startAddress

    QuadrupleList.addQuad("era", None, None, startAddress)

def p_np_push_parameter(p):
    '''
    np_push_parameter : empty
    '''
    global parameterCounter

    if (len(operandsStack) > 0):
        operandType = typeStack.pop()
        operand = operandsStack.pop()
        funcName = p[-5 - (3 * parameterCounter)]
        parameterSize = len(FunctionTable.table[funcName].parameters)

        if (parameterCounter < parameterSize):
            parameterName = FunctionTable.table[funcName].parameters[parameterCounter]
            parameterAddress = FunctionTable.searchParameter(parameterName, funcName)
            parameterType = determineVarType(parameterAddress)

            if (parameterType == operandType):
                QuadrupleList.addQuad("parameter", operand, None, parameterAddress)
                parameterCounter += 1
            
            else:
                print("Error: Type of argument sent to parameter of function " + funcName + " doesn't coincide")
                exit()

        else:
            print("Error: Tried to send more parameters to function " + funcName + " than it accepts")
            exit()
    else:
        print("Error: Tried to retrieve expression to add to parameter but the operand stack is empty")
        exit()

def p_np_end_call(p):
    '''
    np_end_call : empty
    '''
    global parameterCounter
    funcName = p[-6]
    funcType = FunctionTable.table[funcName].type
    size = len(FunctionTable.table[funcName].parameters)
    startAddress = FunctionTable.table[funcName].startAddress
    if(parameterCounter != size):
        print("Error: Parameters sent to function " + funcName + " does not coincide with the number that it accepts")
        exit()
    
    else:
        QuadrupleList.addQuad("gosub", None, None, startAddress)
        if (funcType != "void"):
            returnAddress = determineTempAdress(funcType)
            QuadrupleList.addQuad("=", startAddress, None, returnAddress)
            operandsStack.append(returnAddress)
            typeStack.append(funcType)

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

### Guardar arreglos ###
def p_np_add_array(p):
    '''
    np_add_array : empty
    '''
    arrayType = p[-6][1]
    arrayName = p[-5]
    dim1 = str(int(p[-3]) - 1)

    global CCint
    address = Cint[0] + CCint
    name = "0"
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1

    address = Cint[0] + CCint
    name = dim1
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1

    addArray(arrayType, arrayName, dim1)

def p_np_add_matrix(p):
    '''
    np_add_matrix : empty
    '''
    arrayType = p[-9][1]
    arrayName = p[-8]
    dim1 = str(int(p[-6]) - 1)
    dim2 = str(int(p[-3]) - 1)
    dim2FullDim = str(int(dim2) + 1)

    global CCint
    address = Cint[0] + CCint
    name = "0"
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1

    address = Cint[0] + CCint
    name = dim1
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1

    address = Cint[0] + CCint
    name = dim2
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1

    address = Cint[0] + CCint
    name = dim2FullDim
    if (address > Cint[1]):
        print("Stack overflow of constant integers for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCint += 1
    
    addMatrix(arrayType, arrayName, dim1, dim2)

def addArray(arrayType, arrayName, dim1):
    initialAddress = 0
    if(scope == "main"):
        if (arrayType == "int"):
            global CGint
            initialAddress = Gint[0] + CGint
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Gint[1]):
                print("Stack overflow of global integers for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CGint += (int(dim1) + 1)

        if (arrayType == "float"):
            global CGfloat
            initialAddress = Gfloat[0] + CGfloat
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Gfloat[1]):
                print("Stack overflow of global floats for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CGfloat += (int(dim1) + 1)

        if (arrayType == "string"):
            global CGstring
            initialAddress = Gstring[0] + CGstring
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Gstring[1]):
                print("Stack overflow of global strings for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CGstring += (int(dim1) + 1)

        if (arrayType == "char"):
            global CGchar
            initialAddress = Gchar[0] + CGchar
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Gchar[1]):
                print("Stack overflow of global chars for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CGchar += (int(dim1) + 1)

        if (arrayType == "bool"):
            global CGbool
            initialAddress = Gbool[0] + CGbool
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Gbool[1]):
                print("Stack overflow of global bools for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CGbool += (int(dim1) + 1)

    else:
        if (arrayType == "int"):
            global CLint
            initialAddress = Lint[0] + CLint
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Lint[1]):
                print("Stack overflow of local integers for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CLint += (int(dim1) + 1)

        if (arrayType == "float"):
            global CLfloat
            initialAddress = Lfloat[0] + CLfloat
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Lfloat[1]):
                print("Stack overflow of local floats for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CLfloat += (int(dim1) + 1)

        if (arrayType == "string"):
            global CLstring
            initialAddress = Lstring[0] + CLstring
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Lstring[1]):
                print("Stack overflow of local strings for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CLstring += (int(dim1) + 1)

        if (arrayType == "char"):
            global CLchar
            initialAddress = Lchar[0] + CLchar
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Lchar[1]):
                print("Stack overflow of local chars for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CLchar += (int(dim1) + 1)

        if (arrayType == "bool"):
            global CLbool
            initialAddress = Lbool[0] + CLbool
            finalAddress = initialAddress + (int(dim1))
            if (finalAddress > Lbool[1]):
                print("Stack overflow of local bools for array " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addArray(arrayName, initialAddress, dim1)
                CLbool += (int(dim1) + 1)

def addMatrix(arrayType, arrayName, dim1, dim2):
    initialAddress = 0
    if(scope == "main"):
        if (arrayType == "int"):
            global CGint
            initialAddress = Gint[0] + CGint
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Gint[1]):
                print("Stack overflow of global integers for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CGint += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "float"):
            global CGfloat
            initialAddress = Gfloat[0] + CGfloat
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Gfloat[1]):
                print("Stack overflow of global floats for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CGfloat += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "string"):
            global CGstring
            initialAddress = Gstring[0] + CGstring
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Gstring[1]):
                print("Stack overflow of global strings for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CGstring += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "char"):
            global CGchar
            initialAddress = Gchar[0] + CGchar
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Gchar[1]):
                print("Stack overflow of global chars for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CGchar += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "bool"):
            global CGbool
            initialAddress = Gbool[0] + CGbool
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Gbool[1]):
                print("Stack overflow of global bools for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CGbool += ((int(dim1) + 1) * (int(dim2) + 1))

    else:
        if (arrayType == "int"):
            global CLint
            initialAddress = Lint[0] + CLint
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Lint[1]):
                print("Stack overflow of local integers for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CLint += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "float"):
            global CLfloat
            initialAddress = Lfloat[0] + CLfloat
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Lfloat[1]):
                print("Stack overflow of local floats for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CLfloat += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "string"):
            global CLstring
            initialAddress = Lstring[0] + CLstring
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Lstring[1]):
                print("Stack overflow of local strings for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CLstring += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "char"):
            global CLchar
            initialAddress = Lchar[0] + CLchar
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Lchar[1]):
                print("Stack overflow of local chars for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CLchar += ((int(dim1) + 1) * (int(dim2) + 1))

        if (arrayType == "bool"):
            global CLbool
            initialAddress = Lbool[0] + CLbool
            finalAddress = initialAddress + ((int(dim1) + 1) * (int(dim2) + 1)) - 1
            if (finalAddress > Lbool[1]):
                print("Stack overflow of local bools for matrix " + arrayName)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addMatrix(arrayName, initialAddress, dim1, dim2)
                CLbool += ((int(dim1) + 1) * (int(dim2) + 1))

def p_np_push_id(p):
    '''
    np_push_id : empty
    '''
    if (len(p[-1][2]) == 5):
        # Si el id es matriz
        if(len(p[-1][2][4]) == 4):
            expAddress2 = operandsStack.pop()
            expType2 = typeStack.pop()

            expAddress1 = operandsStack.pop()
            expType1 = typeStack.pop() 
            if ((expType2 == "int") and (expType1 == "int")):
                global CTpointers

                arrayName = p[-1][1]
                arrayAddress = FunctionTable.getVarAddress(arrayName, scope)
                arrayType = determineVarType(arrayAddress)
                dim1 = FunctionTable.getArrayDimension(arrayName, scope)
                dim2 = FunctionTable.getMatrixDimension(arrayName, scope)
                dim2FullDim = str(int(dim2) + 1)
                dim1Address = Constants.searchVar(dim1, "main").address
                dim2Address = Constants.searchVar(dim2, "main").address
                dim2FullDimAddress = Constants.searchVar(dim2FullDim, "main").address
                zeroAddress = Constants.searchVar("0", "main").address

                pointerAddress = Tpointers[0] + CTpointers
                if (pointerAddress > Tpointers[1]):
                    print("Stack overflow of pointers for array " + arrayName)
                    exit()
                else:
                    FunctionTable.table[scope].varsTable.addVar(str(pointerAddress), pointerAddress)
                    CTpointers += 1

                    QuadrupleList.addQuad("ver", zeroAddress, dim1Address, expAddress1)
                    temp1 = determineTempAdress("int")
                    QuadrupleList.addQuad("*", expAddress1, dim2FullDimAddress, temp1) # s1*d2
                    QuadrupleList.addQuad("ver", zeroAddress, dim2Address, expAddress2)
                    temp2 = determineTempAdress("int")
                    QuadrupleList.addQuad("+", temp1, expAddress2, temp2) # + s2
                    # UNICA EXCEPCION A LA REGLA DE USAR PURAS DIRECCIONES
                    # Se suma lo que este guardado en la expAddress y la arrayAddress se suma tal cual esta
                    # Para marcar esta excepcion, basate en la direccion del pointer address, de ahi en fuera todas las demas sumas funcionan igual
                    QuadrupleList.addQuad("+dirb", temp2, arrayAddress, pointerAddress) # + dirB
                    operandsStack.append(pointerAddress)
                    typeStack.append(arrayType)

            else:
                print("Expression sent to index array " + arrayName + " is not integer. You can only index arrays with integers")
                exit()
        
        # Si el id es arreglo
        else:
            expAddress = operandsStack.pop()
            expType = typeStack.pop() 
            if (expType == "int"):
                arrayName = p[-1][1]
                arrayAddress = FunctionTable.getVarAddress(arrayName, scope)
                arrayType = determineVarType(arrayAddress)
                dim1 = FunctionTable.getArrayDimension(arrayName, scope)

                dim1Address = Constants.searchVar(dim1, "main").address
                zeroAddress = Constants.searchVar("0", "main").address

                pointerAddress = Tpointers[0] + CTpointers
                if (pointerAddress > Tpointers[1]):
                    print("Stack overflow of pointers for array " + arrayName)
                    exit()
                else:
                    FunctionTable.table[scope].varsTable.addVar(str(pointerAddress), pointerAddress)
                    CTpointers += 1

                    QuadrupleList.addQuad("ver", zeroAddress, dim1Address, expAddress)
                    # UNICA EXCEPCION A LA REGLA DE USAR PURAS DIRECCIONES
                    # Se suma lo que este guardado en la expAddress y la arrayAddress se suma tal cual esta
                    # Para marcar esta excepcion, basate en la direccion del pointer address, de ahi en fuera todas las demas sumas funcionan igual
                    QuadrupleList.addQuad("+dirb", expAddress, arrayAddress, pointerAddress) # s2 + dirB
                    operandsStack.append(pointerAddress)
                    typeStack.append(arrayType)
            else:
                print("Expression sent to index array " + arrayName + " is not integer. You can only index arrays with integers")
                exit()


    else:
        name = p[-1][1]
        address = FunctionTable.getVarAddress(name, scope)
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
    
    operand = Constants.searchVar(name, "main")
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

    operand = Constants.searchVar(name, "main")
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

    operand = Constants.searchVar(name, "main")
    operandsStack.append(operand.address)
    typeStack.append("char")

def p_np_add_constant_string(p):
    '''
    np_add_constant_string : empty
    '''
    global CCstring
    address = Cstring[0] + CCstring
    name = p[-1]
    if (address > Cstring[1]):
        print("Stack overflow of constant strings for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCstring += 1

    operand = Constants.searchVar(name, "main")
    operandsStack.append(operand.address)
    typeStack.append("string")

def p_np_add_constant_bool(p):
    '''
    np_add_constant_bool : empty
    '''
    global CCbool
    address = Cbool[0] + CCbool
    name = p[-1][1]
    if (address > Cbool[1]):
        print("Stack overflow of constant bools for constant " + name)
        exit()
    else:
        Constants.addConstant(name, address)
        CCbool += 1

    operand = Constants.searchVar(name, "main")
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
           or (operatorStack[-1] == "#=")
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
    else:
        if (varType == "int"):
            global CLint
            address = Lint[0] + CLint
            if (address > Lint[1]):
                print("Stack overflow of local integers for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CLint += 1       
        
        elif (varType == "float"):
            global CLfloat
            address = Lfloat[0] + CLfloat
            if (address > Lfloat[1]):
                print("Stack overflow of local floats for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CLfloat += 1

        elif (varType == "string"):
            global CLstring
            address = Lstring[0] + CLstring
            if (address > Lstring[1]):
                print("Stack overflow of local strings for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CLstring += 1
        
        elif (varType == "char"):
            global CLchar
            address = Lchar[0] + CLchar
            if (address > Lchar[1]):
                print("Stack overflow of local chars for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CLchar += 1

        elif (varType == "bool"):
            global CLbool
            address = Lbool[0] + CLbool
            if (address > Lbool[1]):
                print("Stack overflow of local bools for variable " + name)
                exit()
            else:
                FunctionTable.table[scope].varsTable.addVar(name, address)
                CLbool += 1

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
# El que suma, resta o multiplica
def p_np_push_for(p):
    '''
    np_push_for : empty
    '''
    QuadrupleList.addQuad("goto", None, None, None)
    jumpStack.append(len(QuadrupleList.list))
    jumpStack.append((len(QuadrupleList.list) - 1))
    
def p_np_for_jump(p):
    '''
    np_for_jump : empty
    '''
    jump = jumpStack.pop()
    QuadrupleList.editQuadGoto(jump,len(QuadrupleList.list))

def p_np_check_for(p):
    '''
    np_check_for : empty
    '''
    expTypeBoolean = typeStack.pop()
    if (expTypeBoolean != "bool"):
        print("Type mismatch at for boolean component, it is not boolean")
        exit()
    else:
        resultBoolean = operandsStack.pop()
        QuadrupleList.addQuad("gotof", resultBoolean, None, None)
        jumpStack.append(len(QuadrupleList.list) - 1)
        

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

### Puntos neuralgicos para terminar el programa (END) ###
def p_np_end_program(p):
    '''
    np_end_program : empty
    '''
    QuadrupleList.addQuad("end", None, None, None)

parser = yacc()

fileName = input("De el nombre del archivo para compilar con terminacion .w: ")
temp, fileExtension = os.path.splitext(fileName)

if (fileExtension != ".w"):
    print("Error: Nombre del archivo no tiene terminacion .w y no se compilara")

else:
    file = open(fileName, "r")
    content = file.read()
    result = parser.parse(content)

    file.close()

    ### Inicio del proceso para crear el codigo objeto ###
    objFile = open("obj.a", "w")

    constantsList = Constants.getConstants()
    functionList = FunctionTable.getAllFunc()

    for constant in constantsList:
        objFile.write(f'{str(constant)} | ')
    objFile.write("%% \n")

    for function in functionList:
        objFile.write(f'{str(function)} | ')
    objFile.write("%% \n")
    for x in range(0,len(QuadrupleList.list)):
        objFile.write(QuadrupleList.list[x].toString() + "\n")
    objFile.write("%%")

    objFile.close()

    print("Archivo objeto creado o sobreescrito en la misma carpeta con nombre obj.a")