# 1.Prepare a list of tuples by pairing each element from second list with element from first list.

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

def merge(list1, list2):
  mergeList = [(list1[i], list2[i]) for i in range(0, len(list1))]
  return mergeList

print(merge(list1, list2))