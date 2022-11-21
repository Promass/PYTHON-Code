###########################################
#SERVER LOAD DATA FUNCTIONS
###########################################

#Global database that is kept in memory by the server
dataset = {}

#This function is called to load the txt file which contains all the data
def loadData(fileName):
    datafile = open(fileName)

    for line in datafile:
        innerDict = parseLine(line)
        if (innerDict.get("name") != ""):
            dataset[innerDict.get("name")] = innerDict

    datafile.close()

#This function takes a line from the text file, decomposes it and returns a dictionary containing the information
def parseLine(line):
    innerDict = {}
    word = ""
    innerDictKey = ["name", "age", "address", "number"]
    innerDictIdx = 0

    line = line + "\n"
    for charac in line:
        if (innerDictIdx < 4):
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
        else:
            break
    
    return innerDict

#This function gets rid of hanging spaces before and after strings. It also gets rid of extra space inbetween strings
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

###########################################
#SERVER QUERY FUNCTIONS
###########################################

#This function takes in a key and returns the value (name, age, address and number) associated with the key
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

#Required function that prints everything in the database. It returns a formatted string that contains all the database info
def printReport(): 
    report = "\n** Python DB Content **\n"

    for outerKey in dataset:
        report = report + printEntity(outerKey)

    return report

#Required function that returns the value of a given key (customer_name)
def findCustomer(key):
    if (key not in dataset):
        return "\nServer response: " + key + " not dound in database\n"
    else:
        return "\nServer response: " + printEntity(key)

#Required function that adds a new customer to the database
def addCustomer(customer_name, customer_age, customer_address, customer_phone):
    if (customer_name not in dataset):
        dataset[customer_name] = {"name":customer_name, "age":customer_age, "address":customer_address, "number":customer_phone}
        return "\nServer response: Customer " + customer_name + " added to the database\n"
    else:
        return "\nServer response: Customer " + customer_name + " already exists\n"

#Required function that takes the key (customer_name) and deletes this entity from the database
def deleteCustomer(customer_name):
    if (customer_name in dataset):
        del dataset[customer_name]
        return "\nServer response: Customer " + customer_name + " was deleted\n"
    else:
        return "\nServer response: Customer " + customer_name + " does not exist\n"

#Required function that updates age
def updateAge(customer_name, customer_age):
    if (customer_name in dataset):
        if ("age" in dataset[customer_name] and dataset[customer_name]["age"] != ""):
            pre_age = dataset[customer_name]["age"]
            dataset[customer_name]["age"] = customer_age
            return "\nServer response: Customer " + customer_name + "'s age was changed from '" + pre_age + "' to '" + customer_age + "'\n"
        else:
            dataset[customer_name]["age"] = customer_age
            return "\nServer response: Customer " + customer_name + "'s age was set to '" + customer_age + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"

#Required function that updates address
def updateAddress(customer_name, customer_address):
    if (customer_name in dataset):
        if ("address" in dataset[customer_name] and dataset[customer_name]["address"] != ""):
            pre_address = dataset[customer_name]["address"]
            dataset[customer_name]["address"] = customer_address
            return "\nServer response: Customer " + customer_name + "'s address was changed from '" + pre_address + "' to '" + customer_address + "'\n"
        else:
            dataset[customer_name]["age"] = customer_address
            return "\nServer response: Customer " + customer_name + "'s address was set to '" + customer_address + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"

#Required function that updates phone number
def updatePhone(customer_name, customer_phone):
    if (customer_name in dataset):
        if ("number" in dataset[customer_name] and dataset[customer_name]["number"] != ""):
            pre_phone = dataset[customer_name]["number"]
            dataset[customer_name]["number"] = customer_phone
            return "\nServer response: Customer " + customer_name + "'s phone number was changed from '" + pre_phone + "' to '" + customer_phone + "'\n"
        else:
            dataset[customer_name]["number"] = customer_phone
            return "\nServer response: Customer " + customer_name + "'s phone number was set to '" + customer_phone + "'\n"
    else:
        return "\nServer response: Customer " + customer_name + " not found\n"