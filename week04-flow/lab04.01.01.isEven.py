# Program prompts the user for an number 
# and indicates if the number is odd or even
# Author: Laura Condon

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print (str(number) + " is an even number")
else:
    print (str(number) + " is an odd number")
