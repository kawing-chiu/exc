
class MyAwaitable:
    def __await__(self):
        y = yield 10
        print("yielded:", y)
        y = yield 'a'
        print("yielded:", y)

class MyAwaitable2:
    def __await__(self):
        y = yield 20
        print("yielded:", y)
        y = yield 'b'
        print("yielded:", y)
                             
async def coro():              
    a = await MyAwaitable()
    print("awaited:", a)
    b = await MyAwaitable2()
    print("awaited 2:", b)
    return "my return value"
                             
                             
if __name__ == "__main__":   
    c = coro()              
    c.send(None)             
    # send multiple times...
