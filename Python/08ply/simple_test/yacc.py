import ply.yacc as yacc
import lexer # Import lexer information

tokens = lexer.tokens # Need token list

def p_assign(p):
    '''assign : NAME EQUALS expr'''
    print("assign:", list(p))

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

yacc.yacc()

def run():
    data = "x = 3 * 4 + 5 * 6"
    yacc.parse(data)

if __name__ == '__main__':
    run()
