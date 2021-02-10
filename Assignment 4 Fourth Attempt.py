"""
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, 
unless its value already exists in myUniqueList. If the value doesn't exist already, 
it should be added and the function should return True. 
If the value does exist, it should not be added, and the function should return False;
Finally, add some code below your function that tests it out. 
It should add a few different elements, showcasing the different scenarios, 
and then finally it should print the value of myUniqueList to show that it worked.
"""

import array

myUniqueList = []
guest = ""

print(myUniqueList)

def addToMyUniqueList(guest):
    if guest not in myUniqueList:
        myUniqueList.append(guest)
        print(myUniqueList)
        return True
    else:
        return False

guest = "rob"
print(addToMyUniqueList(guest))
guest = "rob"
print(addToMyUniqueList(guest))

"""
Extra Credit:

Add another function that pushes all the rejected inputs into a separate 
global array called myLeftovers. If someone tries to add a value to myUniqueList 
but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

help(array)

help(array)





















