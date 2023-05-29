# 2.Prompt user to enter a value between 1 to 100 and print out the grade based on rules below
            # >= 90 and <= 100 : Grade A
            # >= 80 and < 90 : Grade B
            # >= 70 and < 80 : Grade C
            # < 70 : Grade F

grade = int(input("Enter grade : "))

if grade in range(90, 101) :
  print("Grade: A")
elif grade in range(80, 90) :
  print("Grade: B")
elif grade in range(70, 80) :
  print("Grade: C")
elif grade < 70 :
  print("Grade: F")
else :
  print("Enter a valid grade between 1 and 100")