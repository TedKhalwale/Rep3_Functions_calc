# Create a simple calculator using functions that can perform addition, subtraction,
# multiplication and division

# Prompt the user to enter 2 values :x and y
x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))

# Create a function to add the numbers:
def add(x, y):
    addition = x + y
    return addition
result = add(x, y)

# Create a function to subtract the 2 numbers:
def subtract(x, y):
    subtraction = x - y
    return subtraction
result = subtract(x, y)

# Create a function to multiply the 2 numbers:
def multiply(x, y):
    multiplication = x * y
    return multiplication
result = multiply(x, y)

# Create a function to divide the 2 numbers:
def divide(x, y):
    division = x / y
    return division
result = divide(x, y)

# Give the user aa set of options to choose from:
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

# Create an infinite loop when promopting the user to decide what to do:
while True:
# Prompt the user to choose what to do with the numbers:
    choice = input("What calculation do you want to perform? ")
# If the choice is not among the above set,take the user back and prompt them:
# to choose again 
    if choice in ['1', '2','3','4', '5']:
        break
    else:
        print("invalid  input, please enter valid no")
        
# An 'if' function to link the user's choice to the calculation functions above:
if choice == '1':
    result = add(x, y)
    print(result)
elif choice == '2':
    result = subtract(x, y)
    print(result)
elif choice == '3':
    result = multiply(x, y)
    print(result)
elif choice == '4':
    result = divide(x, y)
    print(result)
else:
    print("Thank you for using the spectaculerrificamazingderful calculator. See ya!")