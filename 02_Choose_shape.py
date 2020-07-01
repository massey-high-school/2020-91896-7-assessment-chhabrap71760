# Component 2 - Choose shape


# Shape Choosing Function (Allows the user to enter the right letter assigned to their desired shape)
def choose_shape(shape_list):

    valid = False
    while not valid:
        shape_input = input('''
-----------------------------------------------
Which shape would you like to use out of these?  
Press:

• <A> for square
• <B> for rectangle
• <C> for triangle
• <D> for Parallelogram
-----------------------------------------------''').lower()  # The .lower() allows the user to type capital letters

        print()

        if shape_input == "a":
            print(shape_list[-4])
        elif shape_input == "b":
            print(shape_list[-3])
        elif shape_input == "c":
            print(shape_list[-2])
        elif shape_input == "d":
            print(shape_list[-1])
        else:
            print("Please select a letter from the list above")   # Prints this error message if the user enters invalid
            continue

        return shape_input  # This returns the question after the error message so the user can try again


# Main routine

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


chosen_shape = choose_shape(shapes)
