# Ask the user what type of measurement they want


# Function
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
