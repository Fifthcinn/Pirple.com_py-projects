
"""
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. If the value doesn't exist already, 
it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;
"""

"""def functionName(input)
    Action
    return Output
"""
"""
myUniqueList =[]
denied = ["bill"]

def approvedGuest(guest):
    if guest not in myUniqueList:
        myUniqueList.append(guest)
        return True
    else:
        denied.append(guest)
    return False

def refuseGuest(guest):
    if guest in myUniqueList:
        denied.append(guest)
        
        return False


guest = "Anna"
guest = approvedGuest("Anna")
guest = approvedGuest("Anna")
guest = approvedGuest("Anna")
guest = approvedGuest("Anna")
guest = approvedGuest("Anna")


print(guest)

print(myUniqueList)
print(denied)
"""

"""
myUniqueList = ["rob"]
myLeftOvers = []
guest = input("Enter Name: ")



def guestEntry(guest):
    if guest in myUniqueList:
        myLeftOvers.append(guest)
        return False
    elif guest not in myUniqueList:
        myUniqueList.append(guest)
        return True
    """

myUniqueList = ["rob"]
myLeftOvers = []
guest = input("Enter Name: ")

#print(guestEntry(guest))

print(myUniqueList)
print(myLeftOvers)


def guestRefuse(guest):
    if guest in myUniqueList:
        myLeftOvers.append(guest)
        return False


def guestEntry(guest):
    if guest not in myUniqueList:
        myUniqueList.append(guest)
        return True


print(guestEntry(guest))
print(myUniqueList)
print(myLeftOvers)


while True:
    guest = input("Enter Name: ")
    def guestEntry(guest):
        if guest in myUniqueList:
            myLeftOvers.insert(0,guest)
            print(myLeftOvers)
            return False
        elif guest not in myUniqueList:
            myUniqueList.insert(0,guest)
            print(myUniqueList)
            return True
    if guestEntry == False:
        break

print(myUniqueList)
print(myLeftOvers)

print(guestEntry(myUniqueList))
print(guestEntry(myLeftOvers))


#choice = input("do you want to enter another name? press y for yes or n for no")


































#myUniqueList = myUniqueList + guestEntry(guest)
#myLeftOvers = myUniqueList + guestRefuse(guest)

