import zipfile
import zlib

# brute-force search
corpus_file = "/usr/share/dict/words"
with zipfile.ZipFile("docs.zip", "r") as archive:
    first = archive.infolist()[0]  # info about each member
    with open(corpus_file) as corpus:
        for line in corpus:
            word = line.strip().encode("ASCII")
            try:
                with archive.open(first, 'r', pwd=word) as member:
                    text = member.read()
                print("Password", word)
                print(text)
                break
            except (RuntimeError, zlib.error, zipfile.BadZipFile):
                pass