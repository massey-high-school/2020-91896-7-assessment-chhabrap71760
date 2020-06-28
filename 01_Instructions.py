# To Do
# Ask user if they want to view the instructions otherwise
# If not, allow them to skip


def instructions():

    print('''****** Welcome To The Measurement Calculator ******''')

    first_time = input("\nPress <v> to view the instructions or <s> to skip ")

    if first_time == "s":
        return ""
    elif first_time == "v":
        print('''
                      ***** Instructions ******

This program is a tool that you can use for your measurement homework.
All you have to do is choose your desired shape like squares, rectangles,
triangles, parallelograms and circles. Then the type of measurement
you want like area, perimeter, diameter, radius and circumference.
<<<<<<< HEAD
It will then calculate it for you and give you the method so you can do
it yourself next time.''')
=======
It will then calculate it for you and show you the method so you can do
it yourself next time''')
>>>>>>> e8da247edb20c903c365024c7d9c3f10b5332b5a

    else:
        print("Please type either <s> or <v>")
        return ""
instructions()
print()
print()


