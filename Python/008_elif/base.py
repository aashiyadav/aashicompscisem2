x = input("enter a number ")
y = input("enter a character ")
z = input("enter another number ")
a = int(int(x) * int(z))
b = int(int(x) - int(z))
c = int(int(x) + int(z))
d = int(int(x) / int(z))

if y == '+':
    print(c)
elif y == '-':
    print(b)
elif y == '/':
    print(d)
elif y == '*':
    print(a)


