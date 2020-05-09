value1 = input("Enter a string : ")
value2 = int(input("Enter an integer : "))
value3 = float(input("Enter a float number : "))

atup = (value1,value2,value3)
alist = [value1,value2,value3]
adict = {'First element':value1,'Second element':value2,'Third element':value3}

print('\n')
print("your tuple is :",atup)
print("your list is :",alist)
print("your dictionary is :",adict)

print('\n')
value4 = input("add another value")
alist.append(value4)
print("your new list is :",alist)
