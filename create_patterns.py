""" having functions for all the shapes"""
def right_facing_triangle(max_height):
    # right facing triangle

    for i in range(1, max_height + 1):
        my_str = '*' * i
        print(my_str)
    for j in range(max_height - 1, 0, -1):
        my_str = '*' * j
        print(my_str)


def right_angled_triangle(height):
    #right angled triangle
    for i in range(1, height + 1):
        my_str = '*' * i
        print(my_str)


def kite(width):
    #kite
    for i in range(1, width + 1, 2):
        my_str = '*' * i
        print(my_str)
    for j in range(width - 2, 0, -2):
        my_str = '*' * j
        print(my_str)


def rectangle(height,width):
# rectangle
    for i in range(0, height):
        my_str = ''
        for j in range(0, width):
            my_str += '*'
        print(my_str)


"""having while loop to ensure program runs continously as long as the user wantes it to run"""

while(True):

    """displaying instructions for user"""

    print("Drawing shapes through patterns\n Instructions for users")
    print("To Draw a right facing triangle please press 1")
    print("To Draw a right angled triangle please press 2")
    print("To Draw a kite please press 3")
    print("To Draw a rectangle please press 4")

    """Asking what shape to draw from user"""

    shape_input = input("What shape you want to draw please enter a valid number:\n ")

    """" Error handling for invalid input for shapes"""
    try:
        shape_input = int (shape_input)
    except:
        print("Invalid number entered")
        continue

    if shape_input != 1  and shape_input != 2 and shape_input != 3 and shape_input != 4:
        print("\nInvalid number entered for shapes please try again\n")
        continue

    """handling user inputs for different shapes which can be drawn by our program"""

    if shape_input==1:
        height_rt_facing_triangle = input('Please enter the maximum height of the right facing triangle:\n')

        """" Error handling for invalid input for right facing triangle height"""

        try:
            height_rt_facing_triangle = int(height_rt_facing_triangle)
        except:
            print("Invalid number entered for height of right facing triangle")
            continue

        print("Right facing triangle:\n")
        right_facing_triangle(height_rt_facing_triangle)

    elif shape_input == 2:
        height_rt_angled_triangle = input('Please enter the maximum height of the right angled triangle:\n')

        """" Error handling for invalid input for right angled triangle height"""

        try:
            height_rt_angled_triangle = int(height_rt_angled_triangle)
        except:
            print("Invalid number entered for height of right angled triangle")
            continue

        print("Right angled triangle\n")
        right_angled_triangle(height_rt_angled_triangle)

    elif shape_input == 3:
        kite_width = input('Please enter the width of the kite:\n')

        """" Error handling for invalid input for kite's width"""

        try:
            kite_width = int(kite_width)
        except:
            print("Invalid number entered for width of kite")
            continue

        print("kite:\n")
        kite(kite_width)

    elif shape_input == 4:
        height_rectangle = input('Please enter the length of the rectangle:\n')

        """" Error handling for invalid input for rectangle's height"""

        try:
            height_rectangle = int(height_rectangle)
        except:
            print("Invalid number entered for rectangle height")
            continue

        width_rectangle = input('Please enter the width of the rectangle:\n')

        """" Error handling for invalid input for rectangle's width"""

        try:
            width_rectangle = int(width_rectangle)
        except:
            print("Invalid number entered for rectangle width")
            continue

        print("Rectangle:\n")
        rectangle(height_rectangle,width_rectangle)

    # Asking user whether he wants to continue using calculator
    con = input("if you wish to continue press Y, or press N to end program:\n")
    if con == 'Y':
        continue
    else:
        break

print("\n end of program")
