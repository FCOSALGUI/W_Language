from ply.yacc import yacc
from lexer import *

# PROGRAM
def p_program(p):
    '''
    program: var_dec df_dec modules MAIN { body } END
    '''

    p[0] = ('rule program: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])


# VAR_DEC
def p_var_dec(p):
    '''
    var_dec: var_dec1 var_dec
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule var_dec: ', p[1], p[2])
    else:
        p[0] = ('rule var_dec: ', p[1])

def p_var_dec1(p):
    '''
    var_dec1: VAR type ID var_dec2 ;
            | var_dec3
            | var_dec4
            | empty
    '''
    if (len(p) == 6):
        p[0] = ('rule var_dec1: ', p[1], p[2], p[3], p[4], p[6])
    else:
        p[0] = ('rule var_dec1: ', p[1])

def p_var_dec2(p):
    '''
    var_dec2: , ID var_dec2
            | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule var_dec2: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule var_dec2: ', p[1])

def p_var_dec3(p):
    '''
    var_dec3: VAR type ID [ CTEINT ] ;
    '''
    p[0] = ('rule var_dec3: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_var_dec4(p):
    '''
    var_dec4: VAR type ID [ CTEINT ] [ CTEINT ] ;
    '''
    p[0] = ('rule var_dec4: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10])

# DF_DEC
def p_df_dec(p):
    '''
    df_dec: df_dec1 df_dec
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule df_dec: ', p[1], p[2])
    else:
        p[0] = ('rule df_dec: ', p[1])

def p_df_dec1(p):
    '''
    df_dec1: DATAFRAME ID [ CTEINT ] = ( type ID df_dec2 ) ;
           | empty 
    '''
    if (len(p) == 13):
        p[0] = ('rule df_dec1: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])
    else:
        p[0] = ('rule df_dec1: ', p[1])

def p_df_dec2(p):
    '''
    df_dec2: , type ID df_dec2
           | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule df_dec2: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule df_dec2: ', p[1])

# MODULES
def p_modules(p):
    '''
    modules: modules1 modules
           | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule modules: ', p[1], p[2])
    else:
        p[0] = ('rule modules: ', p[1])

def p_modules1(p):
    '''
    modules1: FUNC modules2 ID ( modules3 ) { var_dec body modules4 }
            | empty
    '''
    if (len(p) == 12):
        p[0] = ('rule modules1: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])
    else:
        p[0] = ('rule modules1: ', p[1])

def p_modules2(p):
    '''
    modules2: type
            | VOID
    '''
    p[0] = ('rule modules2: ', p[1])

def p_modules3(p):
    '''
    modules3: type ID modules5
            | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules3: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules3: ', p[1])

def p_modules4(p):
    '''
    modules4: RETURN ID ;
            | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule modules4: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule modules4: ', p[1])

def p_modules5(p):
    '''
    modules5: , type ID modules5
            | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule modules5: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule modules5: ', p[1])

# TYPE
def p_type(p):
    '''
    type: INT
        | FLOAT
        | CHAR
        | STRING
        | BOOL
    '''
    p[0] = ('rule type: ', p[1])

# BODY
def p_body(p):
    '''
    body: statement body
        | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule body: ', p[1], p[2])
    else:
        p[0] = ('rule body: ', p[1])

# STATEMENT
def p_statement(p):
    '''
    statement: assignment
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
    assignment: variable = exp ;
    '''
    p[0] = ('rule assignment: ', p[1], p[2], p[3], p[4])

# DF_ASSIGNMENT
def p_df_assignment(p):
    '''
    df_assignment: ID . PUSH ( exp df_assignment1 ) ;
    '''
    p[0] = ('rule df_assignment: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_df_assignment1(p):
    '''
    df_assignment1: , exp df_assignment1
                  | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule df_assignment1: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule df_assignment1: ', p[1])

# CONDITION
def p_condition(p):
    '''
    condition: IF ( exp ) { body } condition1
    '''
    p[0] = ('rule condition: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])

def p_condition1(p):
    '''
    condition1: ELSE { body }
              | empty
    '''
    if (len(p) == 5):
        p[0] = ('rule condition1: ', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('rule condition1: ', p[1])

# W_CYCLE
def p_w_cycle(p):
    '''
    w_cycle: WHILE ( exp ) { body }
    '''
    p[0] = ('rule w_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# F_CYCLE
def p_f_cycle(p):
    '''
    f_cycle: ( FOR ID = exp ; exp ) { body }
    '''
    p[0] = ('rule f_cycle: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])

# READ
def p_read(p):
    '''
    read: READ ( variable ) ;
    '''
    p[0] = ('rule read: ', p[1], p[2], p[3], p[4], p[5])

# WRITE
def p_write(p):
    '''
    write: WRITE ( exp ) ;
    '''
    p[0] = ('rule write: ', p[1], p[2], p[3], p[4], p[5])

# CALL
def p_call(p):
    '''
    call: ID ( call1 )
        | ID ( call1 ) ; 
    '''
    if (len(p) == 4):
        p[0] = ('rule call: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call: ', p[1], p[2], p[3])

def p_call1(p):
    '''
    call1: exp call2
         | empty
    '''
    if (len(p) == 3):
        p[0] = ('rule call1: ', p[1], p[2])
    else:
        p[0] = ('rule call1: ', p[1])

def p_call2(p):
    '''
    call2: , exp call2
         | empty
    '''
    if (len(p) == 4):
        p[0] = ('rule call2: ', p[1], p[2], p[3])
    else:
        p[0] = ('rule call2: ', p[1])

# SPECIAL_CALL
def p_special_call(p):
    '''
    special_call: keys
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
    keys: ID . KEYS ( ) ;
    '''
    p[0] = ('rule keys: ', p[1], p[2], p[3], p[4], p[5], p[6])

# AVG
def p_avg(p):
    '''
    avg: ID . AVG ( ID ) ;
    '''
    p[0] = ('rule avg: ', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

# COUNT

def p_empty(p):
     'empty :'
     pass

def p_error(p):
    print(f'Syntax error at {p.value!r} on line {p.lineno} of type {p}')
    exit()

parser = yacc.yacc()

