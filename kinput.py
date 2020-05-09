lb = int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))

print("\nYou chose {0} as your lower bound, \
and {1} as your upper bound.".format(lb,ub))

verify = input("\nProceed? (y/n): ")
response = verify.lower()

if response == 'y':
    for multiplier in range (lb, (ub + 1)):
        for i in range (1,11):
            print(i,"x",multiplier,"=",i*multiplier)

else:
    print("we are done")
