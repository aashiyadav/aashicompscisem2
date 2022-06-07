x = input("hello, how many items would you like to buy? ")
x = int (int(x))
total = 0
for i in range (0,x):
          a = input("which item are you buying? ")
          price = float(input("what is the price of this item? "))
          total = total + price
          print("thanks for buying " + a)
          
print("your total is : " + str(total))