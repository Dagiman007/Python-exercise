from tkinter import *

class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title('Popup Menu Demo')

        # Create a popup menu
        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = 'Draw a line',
                              command = self.displayLine)
        self.menu.add_command(label = 'Draw a oval',
                              command = self.displayOval)
        self.menu.add_command(label = 'Draw a Rectangle',
                              command = self.displayRect)
        self.menu.add_command(label = 'Clear',
                              command = self.clearCanvas)

        #place canvas in window
        self.canvas = Canvas(window, width = 200,
                             height = 100,
                             bg = 'white')
        self.canvas.pack()

        #bind popup to canvas
        self.canvas.bind('<Button-3>',self.popup)

        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,90, tags = 'rect')

    def displayOval(self):
        self.canvas.create_oval(10,10,190,90, tags = 'oval')

    def displayLine(self):
        self.canvas.create_line(10,10,190,90, tags = 'line')
        self.canvas.create_line(10,90,190,10, tags = 'line')

    def clearCanvas(self):
        self.canvas.delete('rect', 'oval', 'line')

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

PopupMenuDemo()
