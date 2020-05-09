'''A program that demonstrates cancelation error
which occurs when we manipulate a very large number
with a very small number'''

#prompt the user to enter n
print('Sum of 1 + 1/2 + 1/3 +...+1/n')
n = eval(input('Enter n: '))

sum1 = 0
sum2 = 0

for i in range(1,n + 1):
    sum1 += 1/i
for i in range(n,0,-1):
    sum2 += 1/i

print('The sum from left to right is {0}'.format(sum1))
print('The sum from right to left is {0}'.format(sum2),' --more accurate')
