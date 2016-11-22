import multitask


def coroutine1():
    for i in range(3):
        print 'c1'
        yield i

def coroutine2():
    for i in range(3):
        print 'c2'
        yield i

multitask.add(coroutine1())
multitask.add(coroutine2())
multitask.run()