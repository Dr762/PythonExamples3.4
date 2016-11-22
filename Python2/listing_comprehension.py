
# listing comprehension

numbers = range (20)
print numbers
num = [i for i in numbers if i % 2 == 0]
print num

seq = ["one","two","three"]
for i, elem in enumerate(seq):  #enum
    seq[i] = '%d: %s' % (i, seq[i])
    print seq


