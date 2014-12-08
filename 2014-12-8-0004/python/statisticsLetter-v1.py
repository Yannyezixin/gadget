# !/usr/bin/python2.7
# Filename: statisticsLetter.py


def statisticsLetter(filename):
    letterNumber = 0

    infile = open(filename)
    fileContent = infile.read()
    letterNumber = len(fileContent.split())

    return letterNumber


if __name__ == '__main__':
    filename = 'filename.txt'
    letterNumber = statisticsLetter(filename)

    print letterNumber
