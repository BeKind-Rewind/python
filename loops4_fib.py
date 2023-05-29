# 4.Prompt user to enter a number and print out fibonacci sequence up to that number.
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. 
# This means to say the nth term is the sum of (n-1)th and (n-2)th term.

num = int(input("Enter number : "))

n1, n2 = 0, 1

count = 0

if num <=0 :
  print("Positive numbers only")
elif num == 1 :
  print("Fibonacci seq up to", num)
  print(n1)
else :
  print("Fibonacci sequence:")
  while count < num :
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
  