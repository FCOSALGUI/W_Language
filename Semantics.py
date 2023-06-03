### Estructura que determina que tipo de variable resultara de realizar un tipo de operacion entre 2 operandos ###
class Semantics:
    def __init__(self):
        self.cube = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '/': 'float',
                    '*': 'int',
                    '&&': 'bool',
                    '||': 'bool',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '=' : 'int',
                    '#=': 'bool',
                    '!=': 'bool'
                },
                'float': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'bool',
                    '||': 'bool',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool'
                }
            },
            'float': {
                  'float': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'bool',
                    '||': 'bool',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '=' : 'float',
                    '#=' : 'bool',
                    '!=': 'bool'
                  },
                  'int': {
                    '+':'float',
                    '-':'float',
                    '/':'float',
                    '*':'float',
                    '&&': 'bool',
                    '||': 'bool',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '=': 'float'
                  }

            },
            'string':{
                'string': {
                    '=' :  'string',
                    '#=' : 'bool',
                    '!=' : 'bool'
                }
            },
            'char':{
                'char': {
                    '=' :  'char',
                    '#=' : 'bool',
                    '!=' : 'bool'
                }
            },
            'bool':{
                'bool': {
                    '&&' :  'bool',
                    '||' : 'bool',
                    '#=': 'bool',
                    '!=': 'bool'
                }
            }

        }
    def resultType(self, operator, type1, type2):
        if type1 in self.cube and type2 in self.cube[type1] and operator in self.cube[type1][type2]:
           return self.cube[type1][type2][operator]
        else: 
            print("Type mismatch between type " + type1 + " and " + type2 + " for operator " + operator)
            exit()
