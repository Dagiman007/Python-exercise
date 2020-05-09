from tkinter import *

'''window = Tk()

def processOk():
    print('OK button is clicked')
def processCancel():
    print('Cancel button is clicked')

btOk = Button(window,text='ok',fg='white',bg='black',command=processOk)
btCancel = Button(window,text='Cancel',bg='red',fg='white',command=processCancel)

btOk.pack()
btCancel.pack()

window.mainloop()'''

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOk = Button(window,text='ok',fg='white',bg='black',command=self.processOk)
        btCancel = Button(window,text='Cancel',bg='red',fg='white',command=self.processCancel)
        btOk.pack()
        btCancel.pack()

        window.mainloop()

    def processOk(self):
        print('OK button is clicked')
    def processCancel(self):
        print('Cancel button is clicked')

ProcessButtonEvent()
        
        
