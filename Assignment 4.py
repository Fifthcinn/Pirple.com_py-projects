
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


myUniqueList = ["rob"]
myLeftOvers = []
guest = input("Enter Name: ")


def guestEntry(guest):
    if guest in myUniqueList:
        return False
    elif guest not in myUniqueList:
         return True
    


"""while guestEntry == True:
    guest = input("Enter Name: ")

def approved(people):
    if guestEntry == True:
        myUniqueList.append(guest)
print(approved(guestEntry(guest)))
"""

print(guestEntry(guest))
print(myUniqueList)


