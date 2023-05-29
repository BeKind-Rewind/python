# 2.For a given list, generate a list containing squares of even items in list

list = [1, 2, 3, 4, 5, 6, 10, 100, 123, 2, 13]

evenSquares = [i*i for i in list if i % 2 == 0]

print(evenSquares)