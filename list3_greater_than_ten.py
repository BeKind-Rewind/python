# 3.For a given list, generate a list containing squares of the items in list that are greater than 10 and less than 50

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

sqrdGreaterThanTen = [i*i for i in list if i > 10 and i%2 == 0]

print(sqrdGreaterThanTen)