# 1.Python program to check if the number is an Armstrong number or not

# Armstrong is a number that is equal to each digit being powered to the total number of digits(length) and added together
num = int(input("Enter number to check : "))

# Changed num variable to string to 
# use the length to set the power
power = len(str(num))

# initialize sum 
sum = 0

# find the sum of the nth power of each digit
temp = num
while temp > 0 :
  digit = temp % 10 
  sum += digit ** power
  temp //= 10 

if num == sum :
  print(num, "IS an Armstrong number!")
else :
  print(num, "is NOT an Armstrong number.")