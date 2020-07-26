#  Final Build - Measurement Calculator


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
        print('''
****************************************        
!! SORRY THAT IS NOT A VALID RESPONSE !!
****************************************''')  # Error message if the user enters a valid response
        print()


# Number Checking Function (This function is for when the user enters a number below zero or just not a number
def number_checker(question):

    error = '''
***********************************************
!! PLEASE ENTER A NUMBER THAT IS MORE THAN 0 !!
***********************************************'''  # Prints error message

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
        print('''
***********************************
!! PLEASE ENTER EITHER YES OR NO !!
***********************************''')  # Prints error message
        print()


def instructions():

    print("^^^^ Welcome to the measurement calculator ^^^^")
    print()
    first_time = yes_no("Is this your first time using this program ??")
    print()
    if first_time == "no":
        return ""

    print('''
--------------------------------------------------------------------
------          Measurement Calculator - Instructions         ------        
--------------------------------------------------------------------
This program is a tool that you can use for your measurement homework.
All you have to do is choose your desired shape like squares, rectangles,
triangles and parallelograms. Then you choose the type of measurement
you want like area or perimeter. It will then calculate it for you and
if you want, it will give you the method so you can do it yourself next
time 
Enjoy :)
---------------------------------------------------------------------''')


print()
print()


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


# list of the shapes in this calculator
shape_list = ["square", "rectangle", "triangle", "parallelogram"]

instructions()

# Initialise List
shape_type_total = []
calculation_history = []

# Asks the user how many questions they have
print()
questions = number_checker("How many measurement questions do you have?")
print()

questions_played = 0

while questions_played < questions:
    print()
    print("^^ Calculation {} ^^".format(questions_played+1))
    print()
    shape_input = string_checker('''
-----------------------------------------------
Which shape would you like to use out of these?
You can either enter the whole word just enter the first letter

• Square
• Rectangle
• Triangle
• Parallelogram
-----------------------------------------------''', shape_list)
    print(shape_input)
    print()

    # Add shape to the calculation history
    shape_type_total.append(shape_input)

    # List of types of measurement
    types = ["area", "perimeter", ]


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

    # Add type to the calculation history
    shape_type_total.append(choose_type)

    area = 0
    perimeter = 0
    heightP = 0


# This piece of heavily messy code asks the dimensions according to what the user chose earlier and prints it with shape

    # Square and Area
    if shape_input == "square" and choose_type == "area":
        side = number_checker("Please enter the value of a side:")
        area = side * 2
        print(shapes[-4])
        print("side = {}".format(side))
        print()
        print("{:.2f}".format(area))
        shape_type_total.append(area)

    # Square and perimeter
    elif shape_input == "square" and choose_type == "perimeter":
        side = number_checker("Please enter the value of a side:")
        perimeter = side * 4
        print(shapes[-4])
        print("side = {}".format(side))
        print()
        print("{:.2f}".format(perimeter))
        shape_type_total.append(perimeter)

    # Rectangle and Area
    elif shape_input == "rectangle" and choose_type == "area":
        length = number_checker("Please enter the length:")
        width = number_checker("please enter the width:")
        area = length * width
        print(shapes[-3])
        print("length = {}".format(length))
        print("width = {}".format(width))
        print()
        print("{:.2f}".format(area))
        shape_type_total.append(area)

    # Rectangle and perimeter
    elif shape_input == "rectangle" and choose_type == "perimeter":
        length = number_checker("Please enter the length:")
        width = number_checker("please enter the width:")
        perimeter = 2 * (length + width)
        print(shapes[-3])
        print("length = {}".format(length))
        print("width = {}".format(width))
        print()
        print("{:.2f}".format(perimeter))
        shape_type_total.append(perimeter)

    # Triangle and Area
    elif shape_input == "triangle" and choose_type == "area":
        base = number_checker("Please enter the base:")
        height = number_checker("Please enter the height:")
        area = 0.5 * base * height
        print(shapes[-2])
        print("Base = {}".format(base))
        print("Height = {}".format(height))
        print()
        print("{:.2f}".format(area))
        shape_type_total.append(area)

    # Triangle and Perimeter
    elif shape_input == "triangle" and choose_type == "perimeter":
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
        shape_type_total.append(perimeter)

    # Parallelogram and Area
    elif shape_input == "parallelogram" and choose_type == "area":
        have_height = yes_no("do you have a height?").lower()                      # This part asks the user just in case if

        if have_height == "no":                                                  # they already have a height
            areaP = number_checker("Please enter the area:")
            base = number_checker("Please enter the base:")
            heightP = areaP/base
            print(shapes[-1])
            print("Area = {}".format(areaP))
            print("Base = {}".format(base))
            print()
            print("{:.2f}".format(heightP))
            shape_type_total.append(heightP)

        elif have_height == "yes":                                              # And if they do it'll continue asking
            height = number_checker("Please enter the height:")                    # the values to get the area
            base = number_checker("Please enter the base:")
            area = base * height
            print(shapes[-1])
            print("Height = {}".format(height))
            print("Base = {}".format(base))
            print()
            print("{:.2f}".format(area))
            shape_type_total.append(area)

    # Parallelogram and Perimeter
    elif shape_input == "parallelogram" and choose_type == "perimeter":
        side = number_checker("Please enter the side:")
        base = number_checker("please enter the base:")
        perimeter = 2 * (base + side)
        print(shapes[-1])
        print("side = {}".format(side))
        print("Base = {}".format(base))
        print()
        print("{:.2f}".format(perimeter))
        shape_type_total.append(perimeter)

    # Ask the user if they would like to see the method
    print()
    explain = yes_no("Would you like to see the method to calculate this yourself").lower()

    if explain == "yes":
        if shape_input == "square" and choose_type == "area":
            print('''
    ------------------------------------------------------------
    It is fairly easy,
    All u have to do to find the area is times any side
    by 2. This is because all of the sides of a square are equal
    ------------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "square" and choose_type == "perimeter":
            print('''
    ------------------------------------------------------------
    It's pretty simple,
    To find the perimeter of something all you have to do is add
    all of the sides, and since a square has all equal sides you 
    just have to times a side by 4 because a square has 4 sides
    -------------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "rectangle" and choose_type == "area":
            print('''
    ---------------------------------------------------------
    To find the area of a rectangle is simple,
    You just have to use the formula: (Area = Length x width)
    To get the area just times Length and width together.
    --------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "rectangle" and choose_type == "perimeter":
            print('''
    -------------------------------------------------------------
    This one is easy
    you just add all of the sides and you get your answer
    or what you could do is add the length and width together
    and times it by 2 (Perimeter = 2 x (length + Width)
    
    That works because the opposite sides of both length and width
    are equal, so you just add them together and times it by 2
    --------------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "triangle" and choose_type == "area":
            print('''
    -------------------------------------------------------
    It isn't difficult, you just have to use this formula:
    (0.5 x Base x Height) or (1/2 x Base x Height)
    This formula is similar to the rectangle's one
    just with the 1/2 added to it, this is because a triangle is
    just half of a rectangle. Just thing base x Height and then
    half that answer, then you have your area of a triangle.
    --------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "triangle" and choose_type == "perimeter":
            print('''
    ---------------------------------------------
    This is super easy. 
    you just add all of the sides together,
    and that's you get the perimeter of a triangle
    ---------------------------------------------''')
            questions_played += 1
        elif shape_input == "parallelogram" and choose_type == "area":
            print('''
    -------------------------------------------------------
    Don't be overwhelmed by this one it isn't that hard.
    You just use the formula: (Area = Base x Height)
    and if you don't have the height, you must have the area
    so you just the formula: (Height = area ÷ base)
    -------------------------------------------------------''')
            questions_played += 1
        elif shape_input == "parallelogram" and choose_type == "perimeter":
            print('''
    ----------------------------------------------------------------
    This one is easy
    you just add all of the sides and you get your answer
    or what you could do is add the side and base together
    and times it by 2 (Perimeter = 2 x (side + base)
    
    Use the side not the height, The height is used to find the area
    
    That works because the opposite sides of both height and base
    are equal, so you just add them together and times it by 2
    -----------------------------------------------------------------''')
            questions_played += 1

    elif explain == "no":
        questions_played += 1


calculation_history.append(shape_type_total)

print(calculation_history)

print()
print("***** Calculation History *****")

for item in calculation_history:
    print("{} - {} - {}".format(item[0], item[1], item[2]))

print()
print("^^^^ Thank You for using Measurement Calculator :) ^^^^")
print()
