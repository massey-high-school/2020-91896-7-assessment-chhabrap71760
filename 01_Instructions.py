# Component 1 - Instructions


# Function (Gives the user an option to either skip or view the instructions
def instructions():

    print("^^^^ Welcome to the measurement calculator ^^^^")
    print()
    first_time = input("Is this your first time using this program ")

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
instructions()
