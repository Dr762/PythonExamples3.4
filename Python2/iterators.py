import itertools
from itertools import groupby


class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Return next elem """
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Return iterator itself"""
        return self


i = iter('abcdef')
print i.next()
print i.next()

print "MyIterator usage"
for el in MyIterator(8):
    print el


# tee: The Back and Forth Iterator
def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b


seq1 = ["one", "two", "three"]
print with_head(seq1)
print with_head(seq1, 2)
print with_head(seq1, 3)


# rgroupby: The uniq Iterato
def compress(data):
    return ((len(list(group)), name)
            for name, group in groupby(data))


def decompress(data):
    return (car*size for size, car in data)

print list(compress("get uuuuuuuuuuuuuuuuuuuuuuuup"))
compressed = compress("get uuuuuuuuuuuuuuuuuuuuuuuup")
print ''.join(decompress(compressed))
