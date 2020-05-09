from tkinter import *

class MainGUI:
    def __init__(self):
        window = Tk()
        window.title('Traffic Lights')

        self.canvas = Canvas(window, bg = 'white', width = 300, height = 400)
        self.canvas.pack()

        fill = None
        self.canvas.create_rectangle(100, 50, 200, 350)
        self.drawOval(100, 50, 200, 150, fill, 'oval')
        self.drawOval(100, 150, 200, 250, fill, 'oval')
        self.drawOval(100, 250, 200, 350, fill, 'oval')
        

        frame = Frame(window)
        frame.pack()

        self.v1 = IntVar()
        rbRed = Radiobutton(frame, text = 'Red', variable = self.v1,
                            value = 1, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame, text = 'yellow', variable = self.v1,
                            value = 2, command = self.processRadiobutton)
        rbGreen = Radiobutton(frame, text = 'Green', variable = self.v1,
                            value = 3, command = self.processRadiobutton)
        rbRed.grid(row = 1, column = 1)
        rbYellow.grid(row = 1, column = 2)
        rbGreen.grid(row = 1, column = 3)

        window.mainloop()
        

    def processRadiobutton(self):
        if self.v1.get() == 1:
            self.canvas.delete('oval')
            self.fill = 'red'
            self.drawOval(100, 50, 200, 150, self.fill, 'oval')
            self.drawOval(100, 150, 200, 250, None, 'oval')
            self.drawOval(100, 250, 200, 350, None, 'oval')
        elif self.v1.get() == 2:
            self.canvas.delete('oval')
            self.fill = 'yellow'
            self.drawOval(100, 50, 200, 150, None, 'oval')
            self.drawOval(100, 150, 200, 250, self.fill, 'oval')
            self.drawOval(100, 250, 200, 350, None, 'oval')
        else:
            self.canvas.delete('oval')
            self.fill = 'green'
            self.drawOval(100, 50, 200, 150, None, 'oval')
            self.drawOval(100, 150, 200, 250, None, 'oval')
            self.drawOval(100, 250, 200, 350, self.fill, 'oval')
            
            

    def drawOval(self, x1, y1, x2, y2, color, tag):
        self.canvas.create_oval(x1, y1, x2, y2, fill = color, tags = tag)
            
            

MainGUI()

        
                      
        
        
                             
