
forms = ['animal','mineral','vegetable']
answer = input("Are you an animal, a mineral or a vegetable? ")

if answer == forms[0]:
    print("you are an animal, GRR!")
elif answer == forms[1]:
    print("You are a mineral; you must be healthy.")
elif answer == forms[2]:
    print("you are a vegetable")
else:
    print("you didn't put any valid response")
