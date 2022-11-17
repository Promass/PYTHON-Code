def loadData(fileName):
    dataList = {}
    datafile = open(fileName)

    for line in datafile:
        innerDict = parseLine(line)
        dataList[innerDict.get("name")] = innerDict

    datafile.close()

    return dataList


def parseLine(line):
    innerDict = {}
    word = ""
    innerDictKey = ["name", "age", "address", "number"]
    innerDictIdx = 0

    for charac in line:
        if (charac == "\n"):
            word = spaceStrip(word)
            innerDict[innerDictKey[innerDictIdx]] = word
            innerDictIdx = innerDictIdx + 1
            break
        elif (charac != "|"):
            word = word + str(charac)
        else:
            word = spaceStrip(word)
            innerDict[innerDictKey[innerDictIdx]] = word
            innerDictIdx = innerDictIdx + 1
            word = ""
    
    return innerDict


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
    data_values = "** Python DB Content **\n"

    for outerKey in dataset:
        for innerKey in dataset[outerKey]:
            data_values = data_values + dataset[outerKey][innerKey]
            data_values = data_values + "|"
        data_values = data_values + "\n"

    return data_values
