from random import shuffle

rank = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

shuffle(rank)

# Prompt the user to pick four cards
choice = []
print('Pick four cards\n')
for i in range(4):
    temp = eval(input('Pick (1-52)'))
    choice.append(temp)

sum = 0
for i in range(len(choice)):
    if rank[choice[i] % 13] == 'A':
        sum += 1
    elif rank[choice[i] % 13] == 'J':
        sum += 11
    elif  rank[choice[i] % 13] == 'Q':
        sum += 12
    elif  rank[choice[i] % 13] == 'K':
        sum += 13
    else:
        sum += rank[choice[i] % 13]
        
    

print('The cards you picked ', end = ' ')
for i in range(len(choice)):
    print(rank[choice[i] % 13], end = ' ')

print('\nAnd their sum is ', sum)

