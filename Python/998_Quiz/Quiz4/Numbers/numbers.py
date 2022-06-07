num = [6,9,32,28,15,22,3,18]
minimum = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
maximum = 0
average = 0

for i in range(0,len(num)):
    if(num[i]<minimum):
        minimum = num[i]
print(str(minimum))

for i in range(0,len(num)):
    if(num[i]> maximum):
        maximum = num[i]
print(str(maximum))

summ = 0
count = 0
for i in range(0,len(num)):
    summ = summ + num[i]
    count = count + 1
    count2 = count
average = summ / count2
print(str(average))