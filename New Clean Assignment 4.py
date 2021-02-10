"""

# 1. guestName = enter name to check if permissable
# 2. name gets entered into input
# 3. function checks name
# 4. if function returns true, name gets added to myUniqueList
# 5. if function returns false, name gets added to myLeftovers
# 6. print both lists 
# 7. user gets asked if they would like to enter another name
# 6. if yes back to 2
# 9. if no, break

myUniqueList = []
myLeftOvers = []
guestName = ""
guest = ""

def guestRefuse(guest):
    if myUniqueList == []:
        return ""
    elif guestName in myUniqueList:
#        myLeftOvers.append(guestName)
        return False


def guestEntry(guest):
    if myLeftOvers == []:
        return ""
    elif guestName not in myUniqueList:
#        myUniqueList.append(guestName)
        return True


userChoice = ""
while userChoice == "":
    guestName = input("\nTYPE 'END' TO CLOSE \nPlease enter name: ")
    if guestName == "end":
        break

    if guestName in myUniqueList:
            myLeftOvers.append(guestName)
    print("myLeftOvers: " + str(myLeftOvers))
    print(guestRefuse(guestName))


    
    if guestName not in myUniqueList:
            myUniqueList.append(guestName)
    print("myUniqueList: " + str(myUniqueList))
    print(guestEntry(guestName))
    

#print(guestRefuse(guestName))
#print(guestEntry(guestName))
#    userChoice = input("Try another name? yes or no: ")
#    if guestName == "end":
#        break

#print(guestEntry("john"))

"""