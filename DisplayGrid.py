from tkinter import *

class DisplayGrid:
    def __init__(self):
        window = Tk()
        window.title('Display Grid')

        self.canvas = Canvas(window, width = 300, height = 300, bg = 'white')
        self.canvas.pack()

        for i in range(9):
            self.canvas.create_line(10, 10 + i * 20,
                                    170, 10 + i * 20, fill = 'blue')
            for j in range(9):
                self.canvas.create_line(10 + j * 20, 10,
                                        10 + j * 20, 170, fill = 'red')
        
        window.mainloop()

DisplayGrid()
