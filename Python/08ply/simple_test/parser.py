import ply.yacc as yacc

from lexer import tokens


def p_assign(p):
    '''assign : NAME EQUALS expr'''
    print("assign:", list(p))
    p[0] = 1000

def p_expr(p):
    '''expr : expr PLUS term
    | expr MINUS term
    | term
    '''
    print("expr:", list(p))

def p_term(p):
    '''term : term TIMES factor
    | term DIVIDE factor
    | factor
    '''
    print("term:", list(p))

def p_factor(p):
    '''factor : NUMBER'''
    print("factor:", list(p))

parser = yacc.yacc()

def run():
    data = "x = 3 * 4 + 5 * 6"
    # res is p[0] of the starting grammar rule
    res = parser.parse(data)
    print("res:", res)

if __name__ == '__main__':
    run()
