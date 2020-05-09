from tkinter import *

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('Move Text')

        self.width = 250
        self.height = 50
        self.x = self.width / 2  # Starting center position
        self.y = self.height / 2
        self.dx = 5  # Move right by default
        self.dy = 5  # Move down by default

        frame0 = Frame(window)
        frame0.pack()

        self.v1 = StringVar()
        rbRed = Radiobutton(frame0, text = 'Red', variable = self.v1, value = 'R',
                            command = self.processRadiobutton)
        rbYellow = Radiobutton(frame0, text = 'Yellow', variable = self.v1, value = 'Y',
                            command = self.processRadiobutton)
        rbWhite = Radiobutton(frame0, text = 'White', variable = self.v1, value = 'W',
                            command = self.processRadiobutton)
        rbGray = Radiobutton(frame0, text = 'Gray', variable = self.v1, value = 'G',
                            command = self.processRadiobutton)
        rbGreen = Radiobutton(frame0, text = 'Green', variable = self.v1, value = 'Gn',
                            command = self.processRadiobutton)
        rbRed.grid(row = 1, column = 1)
        rbYellow.grid(row = 1, column = 2)
        rbWhite.grid(row = 1, column = 3)
        rbGray.grid(row = 1, column = 4)
        rbGreen.grid(row = 1, column = 5)

        self.canvas = Canvas(window, width = self.width, height = self.height, bg = 'white')
        self.canvas.pack()

        
        self.displayText()


        frame1 = Frame(window)
        frame1.pack()

        Button(frame1, text = '<=', command = self.processLeftButton).grid(row = 1, column = 5)
        Button(frame1, text = '=>', command = self.processRightButton).grid(row = 1, column = 6)

        window.mainloop()

    background = None

    def displayText(self):
        self.canvas.delete('text')
        self.canvas.create_text(self.x, self.y, text = 'Welcome', fill = self.background, tags = 'text')

    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.background = 'red'
        elif self.v1.get() == 'Y':
            self.background = 'yellow'
        elif self.v1.get() == 'W':
            self.background = 'white'
        elif self.v1.get() == 'G':
            self.background = 'gray'
        elif self.v1.get() == 'Gn':
            self.background = 'green'

        self.displayText()
            
    def processLeftButton(self):
        self.x -= self.dx
        if self.x < 0:
            self.x = self.width
        self.displayText()
        
    def processRightButton(self):
        self.x += self.dx
        if self.x > self.width:
            self.x = 0
        self.displayText()

        

MainGUI()
