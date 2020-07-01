# Component 3 - Measurement Type
# Ask the user what type of measurement they want


# String Checking Function (Allows the user to either enter in the word or the first letter of the word)
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


# Main Routine

types = ["area", "perimeter", ]  # List of types of measurement

# Asks the user for their input and displays their options
choose_type = string_checker('''
-----------------------------------------------------------------
Please enter in the type of measurement, 
you can either enter the whole word or just enter the first letter

• Area
• Perimeter
-----------------------------------------------------------------''', types)
print()
print(choose_type)
