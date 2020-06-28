# Ask the user what type of measurement they want


# Function
def string_checker(question, to_check):

<<<<<<< HEAD
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print()
        print("sorry that is not a valid response")
        print()


# Main Routine

types = ["area", "perimeter", "diameter", "circumference", "radius"]


choose = string_checker('''What type of measurement would you like to choose?
• Area
• Perimeter
• diameter
• circumference
• radius''', types)
print()
print(choose)
=======
# Integer Checking function

# Shape list

types = ["you have chosen area", "you have chosen Perimeter", "You have chosen Diameter",
         "You have chosen Circumference", "You have chosen Radius"]

# Main Routine

type_input = input('''
What type of measurement would you like to choose?
<1> for Area
<2> for Perimeters
<3> for Diameter
<4> for Circumference
<5> for Radius ''')


if type_input == "1":
    print(types[-5])
elif type_input == "2":
    print(types[-4])
elif type_input == "3":
    print(types[-3])
elif type_input == "4":
    print(types[-2])
elif type_input == "5":
    print(types[-1])
else:
    print()
    print("Please select a number from the list above")




>>>>>>> e8da247edb20c903c365024c7d9c3f10b5332b5a
