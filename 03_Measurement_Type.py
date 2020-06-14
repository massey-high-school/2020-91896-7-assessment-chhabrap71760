# Ask the user what type of measurement they want

# Function

# Main Routine


type_input = input('''
What type of measurement would you like to choose?

<1> for Area
<2> for Perimeter
<3> for Diameter
<4> for Circumference
<5> for Radius''')

types = ["you have chosen area", "you have chosen Perimeter", "You have chosen Diameter",
         "You have chosen Circumference", "You have chosen Radius"]

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
    print("Please select a number from the list above")

