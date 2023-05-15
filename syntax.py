from ply.yacc import yacc
from lexer import *

# PROGRAM
def p_program(p):
    '''
    program : var_dec df_dec modules MAIN LEFTCURLYBRACE body RIGHTCURLYBRACE END
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
    var_dec1 : VAR type ID var_dec2 SEMICOLON
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
    var_dec2 : COMMA ID var_dec2
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
    assignment : variable EQUAL exp SEMICOLON
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
    condition : IF LEFTPARENTHESIS exp RIGHTPARENTHESIS LEFTCURLYBRACE body RIGHTCURLYBRACE condition1
    '''
    p[0] = ('rule condition: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_condition1(p):
    '''
    condition1 : ELSE LEFTCURLYBRACE body RIGHTCURLYBRACE
               | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule condition1: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule condition1: ', p[1])

# W_CYCLE
def p_w_cycle(p):
    '''
    w_cycle : WHILE LEFTPARENTHESIS exp RIGHTPARENTHESIS LEFTCURLYBRACE body RIGHTCURLYBRACE
    '''
    p[0] = ('rule w_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# F_CYCLE
def p_f_cycle(p):
    '''
    f_cycle : LEFTPARENTHESIS FOR ID EQUAL exp SEMICOLON exp RIGHTPARENTHESIS LEFTCURLYBRACE body RIGHTCURLYBRACE
    '''
    p[0] = ('rule f_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])

# READ
def p_read(p):
    '''
    read : READ LEFTPARENTHESIS variable RIGHTPARENTHESIS SEMICOLON
    '''
    p[0] = ('rule read: ', p[1], p[2], p[3], p[4], p[5])

# WRITE
def p_write(p):
    '''
    write : WRITE LEFTPARENTHESIS exp RIGHTPARENTHESIS SEMICOLON
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
    exp : t_exp exp1
    '''
    p[0] = ('rule exp: ', p[1], p[2])

def p_exp1(p):
    '''
    exp1 : OR exp
         | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule exp1: ', p[1], p[2])
    else:
        p[0] = ('rule exp1: ', p[1])

# T-EXP
def p_t_exp(p):
    '''
    t_exp : g_exp t_exp1
    '''
    p[0] = ('rule t_exp: ', p[1], p[2])

def p_t_exp1(p):
    '''
    t_exp1 : AND t_exp
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule t_exp1: ', p[1], p[2])
    else:
        p[0] = ('rule t_exp1: ', p[1])

# G-EXP
def p_g_exp(p):
    '''
    g_exp : m_exp g_exp1
    '''
    p[0] = ('rule g_exp: ', p[1], p[2])

def p_g_exp1(p):
    '''
    g_exp1 : g_exp2 m_exp
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
    m_exp : t m_exp1
    ''' 
    p[0] = ('rule m_exp: ', p[1], p[2])

def p_m_exp1(p):
    '''
    m_exp1 : m_exp2 m_exp
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
    t : f t1
    ''' 
    p[0] = ('rule t: ', p[1], p[2])

def p_t1(p):
    '''
    t1 : t2 t
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
    f : LEFTPARENTHESIS exp RIGHTPARENTHESIS
      | CTEINT
      | CTEFLOAT
      | CTECHAR
      | CTESTRING
      | ctebool
      | variable
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

parser = yacc()

file = open("archivo.w", "r")
content = file.read()
result = parser.parse(content)

print(result)