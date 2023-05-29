# 1.Calculate tax payable for a given income. Prompt user to enter a positive number.

fileStat = int(input("Filing status: Enter '1' for 'Single' or '2' for 'Married' : "))
income = int(input("Enter total taxable income (positive number) : $"))

if fileStat == 1:
  if income < 9950:
    print(income * .01)
  elif income < 40525 :
    print(income * .12) 
  elif income < 86375 :
    print(income * .22)
  elif income < 164925 :
    print(income * .24)
  elif income < 209425 :
    print(income * .32)
  elif income < 523600 :
    print(income * .35)
  elif income > 523599 :
    print(income * .37)  
  else :
    print("Your input is wack. Try no symbols...")
elif fileStat == 2:
  if income < 19900:
    print(income * .01)
  elif income < 81050 :
    print(income * .12) 
  elif income < 172750 :
    print(income * .22)
  elif income < 329850 :
    print(income * .24)
  elif income < 418850 :
    print(income * .32)
  elif income < 628300 :
    print(income * .35)
  elif income > 628300 :
    print(income * .37)  
  else :
    print("Your input is wack. Try no symbols...")
else : 
  print("Are you a unicorn?!?!")
