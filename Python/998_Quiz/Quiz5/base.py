x = input("please write a sentence telling me your favorite number: ")
y = input("please input your age: ")
for i in range (len(x)-2):
  y = x[i: len(x)]
  print(y)

print(" ")
for i in range(0, len(x)):
    y = x[i: i + 1]
    if y == (0, len(x)-2):
        print(y)
        