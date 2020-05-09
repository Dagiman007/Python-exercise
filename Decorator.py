def makebold(fun):
    def wrapper():
        return '<b>' + fun() + '</b>'
    return wrapper

def makeitalic(fun):
    def wrapper():
        return '<i>' + fun() + '</i>'
    return wrapper

@makebold
@makeitalic

def hello():
    return 'Hello world'

print(hello())

