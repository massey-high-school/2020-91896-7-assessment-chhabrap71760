# Ask for the chosen shape


# Function
def choose_shape(shape_list):

    valid = False
    while not valid:
        shape_input = input('''
        Which shape would you like to use out of these?  
        Press:
        <A> for square
        <B> for rectangle
        <C> for triangle
        <D> for circle
        <E> for parallelogram ''').lower()
        print()

        if shape_input == "a":
            print(shape_list[-5])
        elif shape_input == "b":
            print(shape_list[-4])
        elif shape_input == "c":
            print(shape_list[-3])
        elif shape_input == "d":
            print(shape_list[-2])
        elif shape_input == "e":
            print(shape_list[-1])
        else:
            print("Please select a letter from the list above")
            continue

        return shape_input


# Main routine


# Shape list
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

chosen_shape = choose_shape(shapes)
print(chosen_shape)
