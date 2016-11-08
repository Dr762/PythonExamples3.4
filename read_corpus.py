# read a word corpus
count = 0
corpus_file = "/usr/share/dict/words"
with open(corpus_file) as corpus:
    for line in corpus:
        word = line.strip()
        if len(word) == 10:
            print(word)
            count += 1
print(count)