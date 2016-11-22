import ftplib
import sys

# ftp (connect to the server)
host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"


def directory_list(path):
    with ftplib.FTP(host, user="anonymous") as connection:
        print("Welcome", connection.getwelcome())
        for name, details in connection.mlsd(path):
            print(name, details['type'], details.get('size'))


directory_list(root)


# ftp download
def get(fullname, output=sys.stdout):
    def line_save(aLine):  ##callback
        download = 0
        expected = 0
        dots = 0
        file = output
        print(aLine, file)
        if output != sys.stdout:
            download += len(aLine)
            show = (20 * download) // expected  # Floor Division - The division of
            # operands where the result is the quotient in which the digits after the decimal point are removed.
            if show > dots:
                end = ""
                file = sys.stdout
                print("-", end, file)
                sys.stdout.flush()
                dots = show

    with ftplib.FTP(host, user="anonymous") as connection:
        print("Welcome", connection.getwelcome())
        expected = connection.size(fullname)
        print("Getting", fullname, "to", output, "size", expected)
        connection.retrlines("RETR {0}".format(fullname), line_save)
    if output != sys.stdout:
        print()  # End the "dots"


get(root + "README")
with open("GUTINDEX.ALL", "w", encoding="UTF-8") as output:
    get(root + "GUTINDEX.ALL", output)
