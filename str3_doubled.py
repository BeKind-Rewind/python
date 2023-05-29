# 3.Create a function in Python that accepts a string and the python must return a string with each character
#       in the original string doubled. If you send the “now” function as a parameter it must return “nnooww,”.
#       If you send “123a!”, it must return “112233aa!!”.

string = input("Enter a word :")

doubled = ''

for i in string :
  doubled += i*2

print(doubled)