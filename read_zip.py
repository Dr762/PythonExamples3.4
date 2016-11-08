import zipfile


# read a zipfile
with zipfile.ZipFile("docs.zip", "r") as archive:
    archive.printdir()
    first = archive.infolist()[0]  # info about each member
    with archive.open(first) as member:
        text = member.read()
        print(text)