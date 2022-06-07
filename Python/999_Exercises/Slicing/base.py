x = input("enter your first and last name please ")
print(" ")
for i in range (0, len(x)):
  y = x[i: i + 1]
  print(y)

print(" ")
for i in range(0, len(x)):
    y = x[i: i + 1]
    if y == " ":
        a = x[i:len(x)]
        b = x[0 : i]
        print(a)
        print(b)