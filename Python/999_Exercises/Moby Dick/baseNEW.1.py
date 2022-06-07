sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
count = 0   

for i in range(0,len(sentence)):    
    if sentence[i:i+5] == "whale":  
        count = count + 1           
print(count)

'''
    The above works like so. The following loops:
    i = 0
        sentence[0:0+5] is "whale"
        count = 1
    i = 1
        sentence[1:1+5] is "hale "
        count = 1     This isn't the word whale so it doesn't count up
    i = 2
        sentence[2:2+5] is "ale h"
        count = 1
    i = 3
        sentence[3:3+5] is "le he"
        count = 1
    i = 4
        sentence[4:4+5] is "e hel"
        count = 1
        
    And so on until it goes through EVERY letter.
'''

count = 0
with open('moby.txt') as f:                        
    for line in f:                                
        sentence = line.strip()                    
        for i in range(0,len(sentence)):           
            if sentence[i:i+5].lower() == "whale":
                count = count + 1
print(count)

f.close()
