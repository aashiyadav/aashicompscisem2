import random
restaurants = ["elephante", "bjs", "yard house"]
menu1 = ['vodka sauce pasta', 'broccolini', 'margerita pizza', "alfredo sauce pasta"]
menu2 = ["avacado burger", "french fries", "nachos", "spagetti", "zitti pene pasta"]
menu3 = ["garlic mushroom noodles", "creamy tomato brisque soup", "gardine orange chicken", "onion rings", "truffle garlic fries"]
print(restaurants)
x = (input("choose a restaurant from the given list "))
if (x == 'elephante'):
    print("the menu for this restaurant is: " )
    print(menu1)
    rand = random.randrange(0,len(menu1))
    print("reccomendations: " + menu1[rand])
if (x == 'bjs'):
    print("the menu for this restaurant is: ")
    print(menu2)
    rand = random.randrange(0,len(menu2))
    print("reccomendations: " + menu2[rand])
if (x == 'yard house'):
    print("the menu for this restaurant is: ")
    print(menu3)
    rand = random.randrange(0,len(menu3))
    print("reccomendations: " + menu3[rand])