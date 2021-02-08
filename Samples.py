

#Samples For Lists

#1
eannasList = [1,2,3,4,5]
print(eannasList)

print("")

#2
eannasList.append(9)
print(eannasList)

print("")

#3
eannasList.extend([20,21,22,23,24])
print(eannasList)

print("")

#4 - same as No. 3 but more efficient
eannasList.extend(range(30,35))
print(eannasList)

print("")

#5 - same as No. 1 but more efficient
# [1,2,3,4,5] - each number in this list has an index, 0 - 4
# list(range(1, 5)) - range (1, 5) means No. 1 - 5, not index
eannasList2 = list(range(1, 5))

print(eannasList2)
#-----------------------------------------------------------------


