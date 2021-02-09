
#------------------------------------------------------------------------------------


myUniqueList = []
notAllowedIn = []

guest = "Eanna"

#myUniqueList = list(guest)

#print(myUniqueList)
#Print(notAllowedIn)

def guestListCheck(x):
    if x not in myUniqueList:
        myUniqueList.insert(0,x)
        return True
    elif x in myUniqueList:
        return False
        

print(myUniqueList)
print("")
checked = guestListCheck(guest)
print(myUniqueList)
print("")
checked = guestListCheck(guest)
print(myUniqueList)
print("")
guest = "Aoife"
checked = guestListCheck(guest)
print(myUniqueList)



#print(notAllowedIn)
#print(checked)







#-------------------------------------------------------------------------------------




myUniqueList = [22]

guest = 22

def eannasFunction(check):
    Action = myUniqueList.append(guest)
    return Action

guestCheck = eannasFunction(guest)

print(guestCheck)
"""


"""
myUniqueList = []
Name = ("sid")


def tracker(guestList):
    entry = guestList + 1
    return True


Name2 = tracker(Name)

print(Name2)

def tracker():
    output = myUniqueList.append(Name)
    return output

#print(Name)
guest = tracker(Name)
print(guest)


tracker()

print(Name)


print("")






"""
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. If the value doesn't exist already, 
it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;
"""


def functionName(input)
    Action
    return Output


myUniqueList = ["tarzan"]
denied = ["bill"]


def approvedGuest(guest):
    if guest not in myUniqueList:
        myUniqueList.append(guest)
        return True

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

guest = guest + approvedGuest(guest)




print(guest)
print(myUniqueList)
print(denied)



guest = input ("Enter Name:")

madlib = f"Guest {guest} has already entered"

print(madlib)



#guest = input("Enter Name: ")




def phrase(state):
    if state == "a":
        return "Correct"

state = "a"

print(phrase(state))

