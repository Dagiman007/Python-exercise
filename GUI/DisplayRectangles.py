from tkinter import *

class DisplayRectangles:
    def __init__(self):
        window = Tk()
        window.title('Display rectangles')

        self.canvas = Canvas(window, bg = 'white', width = 300, height = 300)
        self.canvas.pack()

        for i in range(20):
            self.displayRect(i)

        window.mainloop()

    def displayRect(self, i):
        self.canvas.create_rectangle(10 + i * 6, 10 + i * 6, 
                int(self.canvas["width"]) - 10 - i * 6, int(self.canvas["height"]) - 10 - i * 6)

DisplayRectangles()
