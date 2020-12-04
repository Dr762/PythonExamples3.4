text = """We are the people """

with open("message.txt","w") as target:
    target.write(text)

with open("message.txt","r") as source:
   text = source.read()

print(text)
