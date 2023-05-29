# 2.Prompt user to enter a number and print out all the odd, even numbers between 0 and the number separately on two

num = int(input("Enter a number : "))

start, end = 0, num


print("Even numbers")
for i in range(start, end + 1) :
  if i % 2 == 0 :
    print(i)

print("Odd numbers")
for i in range(start, end + 1) :
  if i % 2 != 0 :
    print(i)
