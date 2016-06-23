
def f():
    print((yield 'start'))
    print((yield 123))
    print((yield'abc'))

g = f()

# besides next(), generators can be driven by generator.send():
g.send(None)    # the first send must have None as argument
g.send(23)
g.send('go')
