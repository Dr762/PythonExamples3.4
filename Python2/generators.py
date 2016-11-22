#  returns generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b  # right hand op


fib = fibonacci()
print "Fibonacci "
print [fib.next() for i in range(10)]


def power(vals):
    for value in vals:
        print 'powering %s' % value
        yield value


def adder(values):
    for value in values:
        print 'adding to %s' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


elems = [1, 2, 3, 10, 16]
res = adder(power(elems))
print res.next()
print res.next()
print res.next()
print res.next()
print res.next()


def psycho():
    print 'tell the problem'
    while True:
        answer = (yield)
        if answer.endswith('?'):
            print ("Don't ask  yourself too much ")
        elif 'good' in answer:
            print "Sounds good"
        elif 'bad' in answer:
            print "Too negative"


free = psycho()
print free.next()
print free.send("All is bad")
print free.send("Is the life shit ?")