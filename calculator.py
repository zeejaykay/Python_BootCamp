

# using while loop to continuously run the calculator till the user wants to exit
while(True):
    print("\n Zaeem\'s  Basic Calculator\n")
    print("Please enter two numbers on which you wish to perform calculation's and the operand\n") # displaying instructions
    num_1 = input("Please enter the 1st number:\n")  # taking input from user
    # error checking for invalid number entry
    try:
        num_1 = int (num_1)
    except:
        print("Invalid number entered")
        continue
    num_2 = input("please enter the 2nd number: \n")
    try:
        num_2 = int (num_2)
    except:
        print("Invalid number entered")
        continue
    operator = input("Please enter the operator: \n")
    if operator != '+' and operator != '*' and operator != '-' and operator != '/': # error checking for invalid entry in operator
        print("Invalid operator")
        continue
    # Calculating for each operation and displaying only the operation requested by the user
    if operator == "+":
        result = num_1 + num_2
        print("your calculation result is:", result, "\n")
    elif operator == "-":
        result = num_1 - num_2
        print("your calculation result is:  %d \n" % result)
    elif operator == "*":
        result = num_1 * num_2
        print("your calculation result is: %d \n" % result)
    elif operator == "/":
        result = num_1 / num_2
        print("your calculation result is %d \n" %(result))
    # Asking user whether he wants to continue using calculator
    con=input("if you wish to continue press Y, or press N to end program:\n")
    if con == 'Y':
        continue # returns to top of loop starts calculating again
    else:
        break # Ending the program

print("\n end of program")
