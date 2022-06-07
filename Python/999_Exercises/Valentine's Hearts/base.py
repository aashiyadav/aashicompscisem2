people_list = ["mom", "dad", "sister","brother", "friend"]
comp_list=["is smart!", "has a great personality", "is very pretty", "is super sweet"]



with open('People.txt') as f:
    for line in f:
        l = line.strip()
        comp_list.append(l)
        

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        comp_list.append(f)

import random
peoplenum = random.randrange(0,len(people_list))
compnum = random.randrange(0,len(comp_list))
print()
print(people_list[peoplenum] + " " + comp_list[compnum])
