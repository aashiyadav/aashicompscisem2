import random
wordlist = [ ]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        wordlist.append(l)
        
number =random.randrange(12972)
answer = wordlist[number]
print(answer)

a = 0
for i in range(0,6):
    guess = input("guess a word! ")
    if guess == answer:
        print("you won !!")
        a = 1
        break
    else:
        print("guess again !!")
if a == 0:
    print("you lost! the word was: " + answer)