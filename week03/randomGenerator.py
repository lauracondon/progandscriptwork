# randomGenerator.py
# program that prints out a random number from a range specified by the user
# Author: Laura Condon

import random

number = random.randint(int(input("Enter the first number in your range: ")), int(input('Enter the second number in your range: ')) +1)
print("Here is a random number from your range: " + str(number))