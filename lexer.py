from ply.lex import lex

reserverd_words = {
    "program": "PROGRAM",
    "var" : "VAR",
    "null": "NULL",
    "func": "FUNC",
    "void": "VOID",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "string": "STRING",
    "bool": "BOOL",
    "array": "ARRAY",
    "dataframe": "DATAFRAME",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "read": "READ",
    "write": "WRITE",
    "return" : "RETURN",
    "true" : "TRUE",
    "false" : "FALSE",
    "end": "END",
    "push": "PUSH",
    "keys": "KEYS",
    "avg": "AVG",
    "count" : "COUNT",
    "max" : "MAX",
    "min": "MIN",
    "sum": "SUM",
    "plot": "PLOT",
    "histogram": "HISTOGRAM",
    "print": "PRINT",
}

tokens = ["ID", "CTEINT", "CTEFLOAT", "CTECHAR", "CTESTRING", "AND", "OR", "LT", "GT", "LTOE", "GTOE", "E", "NE",
          "LEFTBRACKET", "RIGHTBRACKET", "LEFTPARENTHESIS", "RIGHTPARENTHESIS", "LEFTCURLYBRACE", "RIGHTCURLYBRACE",
           "SEMICOLON", "COMMA", "PLUS", "MINUS", "MULTIPLICATION", "DIVISION", "EQUAL", "EXCLAMATION", "DOT" ] + list(reserverd_words.values())

literals = "[](){};,+-*/=!."

t_ignore = ' \t'

"""def t_COMMENT(t):
    r'\#([^\#\n]|(\#(.|\n)))*?'
    t.type = reserverd_words.get(t.value, "COMMENT")
    return t
"""

t_AND = r'\&\&'
t_OR = r'\|\|'
t_LT = r'\<'
t_GT = r'\>'
t_LTOE = r'\<\='
t_GTOE = r'\>\='
t_E = r'\=\='
t_NE = r'\!\='

def t_LEFTBRACKET(t):
    r'\['
    t.type = '['
    return t
    
def t_RIGHTBRACKET(t):
    r'\]'
    t.type = ']'
    return t

def t_LEFTPARENTHESIS(t):
    r'\('
    t.type = '('
    return t

def t_RIGHTPARENTHESIS(t):
    r'\)'
    t.type = ')'
    return t

def t_LEFTCURLYBRACE(t):
    r'\{'
    t.type = '{'
    return t

def t_RIGHTCURLYBRACE(t):
    r'\}'
    t.type = '}'
    return t

def t_SEMICOLON(t):
    r'\;'
    t.type = ';'
    return t

def t_COMMA(t):
    r'\,'
    t.type = ','
    return t

def t_PLUS(t):
    r'\+'
    t.type = '+'
    return t

def t_MINUS(t):
    r'\-'
    t.type = '-'
    return t

def t_MULTIPLICATION(t):
    r'\*'
    t.type = '*'
    return t

def t_DIVISION(t):
    r'\/'
    t.type = '/'
    return t

def t_EQUAL(t):
    r'\='
    t.type = '='
    return t

def t_EXCLAMATION(t):
    r'\!'
    t.type = '!'
    return t

def t_DOT(t): 
    r'\.'
    t.type = '.'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserverd_words.get(t.value, "ID")
    return t

def t_CTEFLOAT(t):
    r'[+-]?[0-9]+\.[0-9]+(e[-+]?[0-9]+(\.[0-9]+)?)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Declared float not valid %f", t.value)
        t.value = 0
    return t

def t_CTEINT(t):
    r'[-]?[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Declared integer not valid %d", t.value)
        t.value = 0
    return t

def t_CTECHAR(t):
    r'\'([^\"]? | [^\']?)\''
    t.type = reserverd_words.get(t.value, "CTECHAR")
    return t

def t_CTESTRING(t):
    r'\"([^\\\n]|(\\(.|\n)))*?\"'
    t.type = reserverd_words.get(t.value, "CTESTRING")
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    t.type = t.value[0]
    t.value = t.value[0]
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t

lexer = lex()