# nameAndAge.py
# This program asks the user for their name and age, and then returns that information to them in a greeting
# author: Laura Condon

# prompts user to enter their information
name = input("Please enter your name: ")
age = input("Please enter your age: ")

# two differenet ways of returning the user's input with added greeting. \t adds a tab spacing
print("Hello " + name + "," + "\t your age is " + age)
print("Hello {}, \t your age is {}".format (name,age))
