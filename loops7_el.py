# 7.print all elements in a list
#       print all even index elements in a list
#       print all odd index elements in a list

list = ['apple', 'pickle', 'banana', 'hamburger', 'chili', 'steak', 'broccoli']
evenIndexList =[]
oddIndexList =[]

print("Original list")
print(list)
print()

print("Even indexed items")
for i in range(0, len(list), 2):
  evenIndexList.append(list[i])
print(evenIndexList)
print()

print("Odd indexed items")
for i in range(1, len(list), 2):
  oddIndexList.append(list[i])
print(oddIndexList)
 