#SERVER LOAD DATA FUNCTIONS
dataset = {}

def loadData(fileName):
    datafile = open(fileName)

    for line in datafile:
        innerDict = parseLine(line)
        dataset[innerDict.get("name")] = innerDict

    datafile.close()


def parseLine(line):
    innerDict = {}
    word = ""
    innerDictKey = ["name", "age", "address", "number"]
    innerDictIdx = 0

    line = line + "\n"
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

#SERVER QUERY FUNCTIONS

def printEntity(key):
    entity = ""
    counter = 0

    for innerKey in dataset[key]:
        entity = entity + dataset[key][innerKey]
        if (counter < len(dataset[key]) - 1):
            entity = entity + "|"
            counter += 1

    entity = entity + "\n"

    return entity

def printReport(): 
    report = "\n** Python DB Content **\n"

    for outerKey in dataset:
        report = report + printEntity(outerKey)

    return report


def findCustomer(key):
    if (key not in dataset):
        return "\nServer response: " + key + " not dound in database\n"
    else:
        return "\nServer response: " + printEntity(key)


def addCustomer(customer_name, customer_age, customer_address, customer_phone):
    if (customer_name not in dataset):
        dataset[customer_name] = {"name":customer_name, "age":customer_age, "address":customer_address, "number":customer_phone}
        return "\nServer response: Customer " + customer_name + " added to the database\n"
    else:
        return "\nServer response: Customer " + customer_name + " already exists\n"

def deleteCustomer(customer_name):
    if (customer_name in dataset):
        del dataset[customer_name]
        return "\nServer response: Customer " + customer_name + " was deleted\n"
    else:
        return "\nServer response: Customer " + customer_name + " does not exist\n"

def updateAge(customer_name, customer_age):
    if (customer_name in dataset):
        if ("age" in dataset[customer_name]):
            pre_age = dataset[customer_name]["age"]
            dataset[customer_name]["age"] = customer_age
            return "\nServer response: Customer " + customer_name + "'s age was changed from '" + pre_age + "' to '" + customer_age + "'\n"
        else:
            dataset[customer_name]["age"] = customer_age
            return "\nServer response: Customer " + customer_name + "'s age was set to '" + customer_age + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"


def updateAddress(customer_name, customer_address):
    if (customer_name in dataset):
        if ("address" in dataset[customer_name]):
            pre_address = dataset[customer_name]["address"]
            dataset[customer_name]["address"] = customer_address
            return "\nServer response: Customer " + customer_name + "'s address was changed from '" + pre_address + "' to '" + customer_address + "'\n"
        else:
            dataset[customer_name]["age"] = customer_address
            return "\nServer response: Customer " + customer_name + "'s address was set to '" + customer_address + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"


def updatePhone(customer_name, customer_phone):
    if (customer_name in dataset):
        if ("number" in dataset[customer_name]):
            pre_phone = dataset[customer_name]["number"]
            dataset[customer_name]["number"] = customer_phone
            return "\nServer response: Customer " + customer_name + "'s phone number was changed from '" + pre_phone + "' to '" + customer_phone + "'\n"
        else:
            dataset[customer_name]["number"] = customer_phone
            return "\nServer response: Customer " + customer_name + "'s phone number was set to '" + customer_phone + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"