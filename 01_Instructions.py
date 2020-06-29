# Component 1 - Instructions


# Function (Gives the user an option to either skip or view the instructions
def instructions():

    print('''****** Welcome To The Measurement Calculator ******''')

    first_time = input("\nPress <v> to view the instructions or <s> to skip ")

    if first_time == "s":       # Skips the instructions if the user enters s
        return ""
    elif first_time == "v":      # Prints the instructions if the user enters v
        print('''
--------------------------------------------------------------------
------          Measurement Calculator - Instructions         ------        
--------------------------------------------------------------------
This program is a tool that you can use for your measurement homework.
All you have to do is choose your desired shape like squares, rectangles,
triangles and parallelograms. Then you choose the type of measurement
you want like area or perimeter. It will then calculate it for you and 
give you the method so you can do it yourself next time.
Enjoy :)
---------------------------------------------------------------------''')

    else:
        print("Please type either <s> or <v>")  # Prints this error message if the user enters anything other than s or v

        return ""


instructions()
print()
print()
