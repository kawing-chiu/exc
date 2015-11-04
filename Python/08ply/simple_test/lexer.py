import ply.lex as lex


tokens = [ 'NAME', 'NUMBER', 'PLUS', 'MINUS',
        'TIMES', 'DIVIDE', 'EQUALS' ]

t_ignore_TAB = r'\t'
t_ignore_SPACE = r'\ '
# or:
# t_ignore = ' \t'
# note that t_ignore is a normal string, all characters within the string will 
# be ignored

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    #print("got t:", t.value)
    t.value = int(t.value)
    return t

#t_ignore_COMMENT = r'\#.*'
# the same effect:
def t_del_comment(t):
    r'\#.*'
    pass
    # as long as t is not returned, no token needs to be defined

lexer = lex.lex()

def run():
    lexer.input("x = 3 * 4 + 5 * 6 #hehe")
    #while True:
    #    tok = lexer.token()
    #    if not tok: break
    #    print(tok)
    for tok in lexer:
        print(tok)

    print("-------------")
    lexer.input("y = 1 * 0 + 2 * 8 #hehe")
    for tok in lexer:
        print(tok)

if __name__ == '__main__':
    run()
