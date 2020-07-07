# Component 4b - Enter Calculate


# Shape Choosing function(Allows the user to enter the right letter assigned to their desired shape)
def choose_shape(shape_list):

    valid = False
    while not valid:
        shape_input = input('''
-----------------------------------------------
Which shape would you like to use out of these?
Press:

• <A> for square
• <B> for rectangle
• <C> for triangle
• <D> for Parallelogram
-----------------------------------------------''').lower()  # The .lower() allows the user to type capital letters

        print()

        if shape_input == "a":
            print(shape_list[-4])
        elif shape_input == "b":
            print(shape_list[-3])
        elif shape_input == "c":
            print(shape_list[-2])
        elif shape_input == "d":
            print(shape_list[-1])
        else:
            print("Please select a letter from the list above")   # Prints this error message if the user enters invalid
            continue

        return shape_input  # This returns the question after the error message so the user can try again


# String Checking function (Allows the user to either enter in the word or the first letter of the word)
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print()
        print("sorry that is not a valid response")  # Error message if the user enters a valid response
        print()


# Number Checking Function (This function is for when the user enters a number below zero or just not a number
def number_checker(question):

    error = "Please enter a number that is more than zero"  # Prints error message

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print()
                print(error)
                print()
            else:
                return response

        except ValueError:
            print()
            print(error)
            print()


# This is a function that comes into play when the user enters an invalid response in a yes/no question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print()
        print("Please enter either yes or no...\n")  # Prints error message
        print()


# Main Routine
# This is a list that holds my shapes
shapes = ['''
 ___________________
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|___________________|''', '''
 ___________________________________
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|                                   |
|___________________________________|''', '''
                    _,.-'":
             _,.-'"        :
       _,.-'"               :
 _,.-'"                      :
('-._                         :
     '-._                      :
         '-._                   :
             '-._                :
                 '-._             :
                     '-._          :
                         '-:_       :
                             '-._    :
                                 '-._)''', '''
        _________________________________
       /                                /
      /                                /
     /                                /
    /                                /
   /                                /
  /                                /
 /                                /
/________________________________/''']

chosen_shape = choose_shape(shapes)
types = ["area", "perimeter", ]  # List of types of measurement

# Asks the user for their input and displays their options
choose_type = string_checker('''
-----------------------------------------------------------------
Please enter in the type of measurement,
you can either enter the whole word or just enter the first letter

• Area
• Perimeter
-----------------------------------------------------------------''', types)
print(choose_type)
print()

area = 0
perimeter = 0
heightP = 0

# This piece of heavily messy code asks the dimensions according to what the user chose earlier and prints it with shape

# Square and Area
if chosen_shape == "a" and choose_type == "area":
    side = number_checker("Please enter the value of a side:")
    area = side * 2
    print(shapes[-4])
    print("side = {}".format(side))
    print()
    print("{:.2f}".format(area))

# Square and perimeter
elif chosen_shape == "a" and choose_type == "perimeter":
    side = number_checker("Please enter the value of a side:")
    perimeter = side * 4
    print(shapes[-4])
    print("side = {}".format(side))
    print()
    print("{:.2f}".format(perimeter))

# Rectangle and Area
elif chosen_shape == "b" and choose_type == "area":
    length = number_checker("Please enter the length:")
    width = number_checker("please enter the width:")
    area = length * width
    print(shapes[-3])
    print("length = {}".format(length))
    print("width = {}".format(width))
    print()
    print("{:.2f}".format(area))

# Rectangle and perimeter
elif chosen_shape == "b" and choose_type == "perimeter":
    length = number_checker("Please enter the length:")
    width = number_checker("please enter the width:")
    perimeter = 2 * (length + width)
    print(shapes[-3])
    print("length = {}".format(length))
    print("width = {}".format(width))
    print()
    print("{:.2f}".format(perimeter))

# Triangle and Area
elif chosen_shape == "c" and choose_type == "area":
    base = number_checker("Please enter the base:")
    height = number_checker("Please enter the height:")
    area = 0.5 * base * height
    print(shapes[-2])
    print("Base = {}".format(base))
    print("Height = {}".format(height))
    print()
    print("{:.2f}".format(area))

# Triangle and Perimeter
elif chosen_shape == "c" and choose_type == "perimeter":
    side1 = number_checker("Please enter the value of a side:")
    side2 = number_checker("Please enter the value of another side:")
    side3 = number_checker("Please enter the value of another side:")
    perimeter = side1 + side2 + side3
    print(shapes[-2])
    print("Side 1 = {}".format(side1))
    print("Side 2 = {}".format(side2))
    print("Side 3 = {}".format(side3))
    print()
    print("{:.2f}".format(perimeter))

# Parallelogram and Area
elif chosen_shape == "d" and choose_type == "area":
    have_height = yes_no("do you have a height?").lower()                           # This part asks the user just in case if

    if have_height == "no":                                                  # they already have a height
        areaP = number_checker("Please enter the area:")
        base = number_checker("Please enter the base:")
        heightP = areaP/base
        print(shapes[-1])
        print("Area = {}".format(areaP))
        print("Base = {}".format(base))
        print()
        print("{:.2f}".format(heightP))

    elif have_height == "yes":                                              # And if they do it'll continue asking
        height = number_checker("Please enter the height:")                    # the values to get the area
        base = number_checker("Please enter the base:")
        area = base * height
        print(shapes[-1])
        print("Height = {}".format(height))
        print("Base = {}".format(base))
        print()
        print("{:.2f}".format(area))

# Parallelogram and Perimeter
elif chosen_shape == "d" and choose_type == "perimeter":
    side = number_checker("Please enter the side:")
    base = number_checker("please enter the base:")
    perimeter = 2 * (base + side)
    print(shapes[-1])
    print("side = {}".format(side))
    print("Base = {}".format(base))
    print()
    print("{:.2f}".format(perimeter))




