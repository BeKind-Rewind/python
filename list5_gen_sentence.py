# 5.Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
#        and the object is in ["Hockey","Football"].

subj = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey", "Football"]

import random

print(random.choice(subj), random.choice(verb), random.choice(obj))
