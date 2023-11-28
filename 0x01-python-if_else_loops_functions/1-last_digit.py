#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_numb = number - (10 * int(number / 10))
if (last_numb > 5):
    print("Last digit of", number, "is", last_numb, "and is greater than 5")
elif (last_numb == 0):
    print("Last digit of", number, "is", last_numb, "and is 0")
else:
    print("Last digit of", number, "is", last_numb, "and is less than 6 and not 0")
    

