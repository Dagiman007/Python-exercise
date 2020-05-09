from tkinter import *

class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title('Widgets Demo') # set a title

        # Add a check button and a radio button to frame1\
        frame1 = Frame(window)  #create and add frame to window
        frame1.pack()
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1,text = 'Bold',
                              variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = 'Red', bg = 'red',
                            variable = self.v2, value = 1,
                            command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = 'Yellow', bg = 'Yellow',
                            variable = self.v2, value = 2,
                            command = self.processRadiobutton)
        cbtBold.grid(row = 1,column = 1)
        rbRed.grid(row = 1,column = 2)
        rbYellow.grid(row = 1,column = 3)

        # Add a label, an entry, a button and a message to frame
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2,text = 'Enter your name: ')
        self.name = StringVar()
        entryName = Entry(frame2,textvariable = self.name)
        btGetName = Button(frame2,text = 'Get Name',command = self.processButton)
        message = Message(frame2,text = 'It is a widgets demo')
        label.grid(row =1,column = 1)
        entryName.grid(row = 1,column = 2)
        btGetName.grid(row = 1,column = 3)
        message.grid(row = 1, column = 4)

        # Add text
        text = Text(window) #create and add text to window
        text.pack()
        text.insert(END,
                    'Tip\nThe best way to learn tkinter is to read ')
        text.insert(END,
                   'these carefully designed examples and use them ')
        text.insert(END,
                    'to create your applications.')

        window.mainloop()

    def processCheckbutton(self):
        print('Check button is '
              + ('checked ' if self.v1.get() == 1 else 'Unchecked'))

    def processRadiobutton(self):
        print(('Red' if self.v2.get() == 1 else 'yellow') +
              ' is selected')

    def processButton(self):
        print('Your name is '+ self.name.get())

WidgetsDemo()  #Create GUI
              
        
        
