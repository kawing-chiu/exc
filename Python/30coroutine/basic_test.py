# Native coroutine test
class MyAwaitable:
    def __await__(self):
        y = yield 10
        print("yielded:", y)
        y = yield 'a'
        print("yielded:", y)
        return "end of awaitable 1"

class MyAwaitable2:
    def __await__(self):
        y = yield 20
        print("yielded:", y)
        y = yield 'b'
        print("yielded:", y)
        return "end of awaitable 2"
                             
async def coro():              
    a = await MyAwaitable()
    print("awaited:", a)
    b = await MyAwaitable2()
    print("awaited 2:", b)
    return "my return value"
                             
# Generator-based coroutine test
def my_generator():
    y = yield 10
    print("yielded:", y)
    y = yield 'a'
    print("yielded:", y)
    return "end of generator 1"

def my_generator2():
    y = yield 20
    print("yielded:", y)
    y = yield 'b'
    print("yielded:", y)
    return "end of generator 2"
                             
def gen():              
    a = yield from my_generator()
    print("yielded from:", a)
    b = yield from my_generator2()
    print("yielded from 2:", b)
    return "my return value"

                             
if __name__ == "__main__":   
    c = coro()              
    c.send(None)             
    # send multiple times...
