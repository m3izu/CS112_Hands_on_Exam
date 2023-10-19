# Ask the user to input in between 1 - 3
Prompt = int(input("Type 1 for Base 10 to Base 2\nType 2 for Base 10 to Base 8\nType 3 for Base 10 to Base 16:"))

# Converts the decimal intro its respective assignment
if Prompt == 1:
    Dec = int(input("Enter a Decimal Number:"))
    print(format(Dec, "b"))
elif Prompt == 2:
    Oct = int(input("Enter a Decimal Number:"))
    print(format(Oct, "o"))
elif Prompt == 3:
    Hex = int(input("Enter a Decimal Number:"))
    print(format(Hex, "x"))
else:
    print("Invalid Input, Please Try Again")
