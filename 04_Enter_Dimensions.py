# Component 4 - Enter Dimensions


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

    error = "Please enter a number that is more than zero"

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
        print("Please enter either yes or no...\n")
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

if chosen_shape == "a" and choose_type == "area":
    side = number_checker("Please enter the value of a side:")
elif chosen_shape == "a" and choose_type == "perimeter":
    side = number_checker("Please enter the value of a side:")
elif chosen_shape == "b" and choose_type == "area":
    height = number_checker("Please enter the height:")
    width = number_checker("please enter the width:")
elif chosen_shape == "b" and choose_type == "perimeter":
    height = number_checker("Please enter the height:")
    width = number_checker("please enter the width:")
elif chosen_shape == "c" and choose_type == "area":
    base = number_checker("Please enter the base:")
    height = number_checker("Please enter the height:")
elif chosen_shape == "c" and choose_type == "perimeter":
    side1 = number_checker("Please enter the value of a side:")
    side2 = number_checker("Please enter the value of a side:")
    side3 = number_checker("Please enter the value of a side:")
elif chosen_shape == "d" and choose_type == "area":
    have_height = yes_no("do you have a height?")
    if have_height == "no":
        area = number_checker("Please enter the area:")
        base = number_checker("Please enter the base:")
    elif have_height == "yes":
        height = number_checker("Please enter the height:")
        base = number_checker("Please enter the base:")
elif chosen_shape == "d" and choose_type == "perimeter":
    height = number_checker("Please enter the height:")
    base = number_checker("please enter the height:")
