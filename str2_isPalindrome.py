# 2.Program to find whether a string is a palindrome.

originStr = input("Enter word :")

# originStr = originStr.casefold()

revStr = reversed(originStr)

if list(originStr) == list(revStr) :
  print("It IS a palindrome!")
else :
  print("It's NOT a palindrome.")