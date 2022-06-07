x = int(input("how many numbers would you like in your list? "))
import random
thislist = []
for i in range (0,x):
    y = random.randrange(11)
    thislist.append(y)
print(thislist)