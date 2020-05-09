def main():
    print('i\t\t  m(i)')
    for i in range(1,1000,100):
        print(i,'\t\t',format(m(i),'6.4f'))

def m(i):
    sum = 0
    for j in range(1,i+1):
        sum += ((-1) ** (j+1))/(2*j - 1)
    sum *= 4
    
    return sum

main()
