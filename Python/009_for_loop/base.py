x = input ("please enter a line length: ")
x = int (int(x))
y = input( "would you like a vertical or horizontal line: ")
if str(y) == str("vertical"):
      for i in range (0,x):
           print("*")
   
else:
    for i in range (0,x):
         print("*", end=" ")
    
    
