# convert.py
# this program converts a user's input of dollars into its' absolute value in cents
# author: Laura Condon

# asks the user for their input and converts it to a float
lodgement = float(input("Please enter the amount to convert from dollars to cents: "))
# multiples by 100 to convert the input into cents
cents = lodgement*100
# returns the absolute value of the user's input as an integer
print(abs(int(cents)))