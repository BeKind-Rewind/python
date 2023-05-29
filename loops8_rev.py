# 8.Reverse a Number using a while loop

num = int(input("Enter a number : "))
revNum = 0

while num != 0 :
  digit = num % 10
  revNum = revNum * 10 + digit
  num //= 10

print("Reversed :", str(revNum))
    
    