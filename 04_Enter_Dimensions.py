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
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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
print(chosen_shape)

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

# Enter dimensions

if chosen_shape == "a" and choose_type == "area":
    int(input("Enter the value of a side:"))
elif chosen_shape == "a" and choose_type == "perimeter":
    int(input("Enter the value of a side:"))
elif chosen_shape == "b" and choose_type == "area":
    input("Enter the value of the length (base)")
    input("Enter the value of the width (height)")
elif chosen_shape == "b" and choose_type == "perimeter":
    int(input("Enter the value of the length (base)"))
    int(input("Enter the value of the width (height)"))
else:
    print("Please enter a number that is more than zero")
