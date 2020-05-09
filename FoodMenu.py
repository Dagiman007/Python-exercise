fmenu = {'burger':1.50,'ham':1.99,'eggs':0.99}

corder = input("What will you have today - burger, ham or eggs? ")

if corder == 'burger':
    print("For the burger, that will be","$","%.2f" % fmenu.get(corder),",please")
elif corder == 'ham':
    print("For the ham, that will be","$","%.2f" % fmenu.get(corder),",please")
else:
    print("Eggs by default! your total is","$","%.2f" % fmenu.get('eggs'))
