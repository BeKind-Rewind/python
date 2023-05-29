# 3.Prompt user to enter a number and print out its factorial (using looping).

# The factorial of a number is the total of multiplying every integer from 1 to the number given.
num = int(input("Enter a number : "))

factorial = 1

#take care of the edge cases negative and 0 inputs
if num < 0 :
  print("No factorial for negative numbers")
elif num == 0 :
  print("Factorial of 0 is 1")
else : # loop through and multiply each number to the total from 1 to given number.
  for i in range(1, num + 1) :
    factorial = factorial * i
print("Factorial of", num, "is", factorial)  