def loadData(fileName):
    dataList = {}
    datafile = open(fileName)

    for line in datafile:
        parsedLine = parseLine(line)
        dataList[parsedLine[0]] = parsedLine

    datafile.close()

    return dataList


def parseLine(line):
    lineList = []
    word = ""

    for charac in line:
        if (charac == "\n"):
            word = spaceStrip(word)
            lineList.append(word)
            break
        elif (charac != "|"):
            word = word + str(charac)
        else:
            word = spaceStrip(word)
            lineList.append(word)
            word = ""
    
    return lineList


def spaceStrip(word):
    stripped = word.strip()
    wordIdx = 0
    newWord = ""

    for character in stripped:
        wordIdx = wordIdx + 1
        if (character == " " and stripped[wordIdx] == " "):
            continue
        else:
            newWord = newWord + character

    return newWord


def printReport(dataset): 
    dataset.values()
