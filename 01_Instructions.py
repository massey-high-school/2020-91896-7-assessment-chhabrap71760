# To Do
# Ask user if they want to view the instructions otherwise
# If not, allow them to skip


def instructions():

    print('''****** Welcome To The Measurement Calculator 
    ******''')

    first_time = input("\nHave you used this program before? ")

    if first_time == "yes":
        return ""


print()
print('''
This program is a tool that you can use for your measurement homework.
All you have to do is choose your desired shape like squares, rectangles, 
triangles, parallelograms and circles. Then the type of measurement 
you want like area, perimeter, diameter, radius and circumference.
It will then calculate it for you and give you the method so you can do
it yourself next time.''')

instructions()
