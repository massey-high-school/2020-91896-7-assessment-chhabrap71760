# Ask for the chosen shape

# Main Routine goes here

shape_input = input('''
Which shape would you like to use out of these? 
Press:
<A> for square
<B> for rectangle
<C> for triangle
<D> for circle
<E> for parallelogram''')
print()
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
    print("Please select a letter from the list above")
