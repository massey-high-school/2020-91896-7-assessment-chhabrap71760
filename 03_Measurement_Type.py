# Ask the user what type of measurement they want

# Function

# Main Routine
shape_input = input('''
Which shape would you like to use out of these?
Press:
<A> for square
<B> for rectangle
<C> for triangle
<D> for circle
<E> for parallelogram''')
print()

type_input = input('''
What type of measurement would you like to choose?

<1> for Area
<2> for Perimeter
<3> for Diameter
<4> for Circumference
<5> for Radius''')

types = ["you have chosen area", "you have chosen Perimeter", "You have chosen Diameter",
         "You have chosen Circumference", "You have chosen Radius"]

# Shape list

Shapes = ['''
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
                     _____
                 ,-~"     "~-.
               ,^             ^.
              /                 :
             Y                   Y
             l                   [
             |                   |
             !                   !
              :                 /
               ^.             .^
                 "-.._____.,-" ''', '''
        _________________________________
       /                                /
      /                                /
     /                                /
    /                                /
   /                                /
  /                                /
 /                                /
/________________________________/''']


if shape_input == "a":
    print(Shapes[-5])
elif shape_input == "A":
    print(Shapes[-5])
elif shape_input == "b":
    print(Shapes[-4])
elif shape_input == "B":
    print(Shapes[-4])
elif shape_input == "c":
    print(Shapes[-3])
elif shape_input == "C":
    print(Shapes[-3])
elif shape_input == "d":
    print(Shapes[-2])
elif shape_input == "D":
    print(Shapes[-2])
elif shape_input == "e":
    print(Shapes[-1])
elif shape_input == "E":
    print(Shapes[-1])
else:
    print()
    print("Please select a letter from the list above")
    print()

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
    print()
