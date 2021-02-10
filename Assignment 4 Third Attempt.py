# 1. guestName = enter name to check if permissable
# 2. name gets entered into input
# 3. function checks name
# 4. if function returns true, name gets added to myUniqueList
# 5. if function returns false, name gets added to myLeftovers
# 6. print both lists 
# 7. user gets asked if they would like to enter another name
# 6. if yes back to 2
# 9. if no, break

#       NOT THE ASSIGNMENT !!!! SIMPLIFY !!!!
#---------------------------------------------------------------------------------------------


"""
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. If the value doesn't exist already, 
it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;


-----------------------------------------------------------------------------------------------
"""

"""
myUniqueList = []
myLeftOvers = []
guestName = "rob"
guest = ""



while guest == "":
    guestCheck = input("\nType 'end' to quit\nEnter Name: ")
    if guestCheck == "end":
        break
    def guestRefuse(guestName):
        if guestName in myUniqueList:
            myLeftOvers.append(guestName)
            print(myLeftOvers)
            return False
        elif guestName not in myUniqueList:
            myUniqueList.append(guestName)
            print(myUniqueList)
            return True

"""

# -------------------------------------------------------------------------

"""
def guestEntry(guestName):
    if myLeftOvers == []:
        return ""
    elif guestName not in myUniqueList:
        myUniqueList.append(guestName)
        return True

guestName = guestEntry("Andy")

print(myUniqueList)
"""
 