from tkinter import *

class Checkerboard:
    def __init__(self):
        window = Tk()
        window.title('Display a checkerboard')

        count = 0
        for i in range(8):
            for j in range(8):
                if count % 2 == 0:
                    Label(window, width = 5, height = 2, bg = 'white').grid(row = i, column = j)
                else:
                    Label(window, width = 5, height = 2, bg = 'black').grid(row = i, column = j)
                count += 1
            count += 1

        window.mainloop()

Checkerboard()

                
                    
