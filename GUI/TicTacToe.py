from tkinter import *
import random

class TicTacToe:
    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe board')

        image1 = PhotoImage(file = 'C:/Users/DagiMan/Desktop/Python Programming - CBT Nuggets/Exercise/Ex docs/image/x.gif')
        image2 = PhotoImage(file = 'C:/Users/DagiMan/Desktop/Python Programming - CBT Nuggets/Exercise/Ex docs/image/o.gif')

        for i in range(3):
            for j in range(3):
                m = random.randint(0, 1)
                if m == 0:
                    Label(window, image = image1).grid(row = i, column = j)
                else:
                    Label(window,  image = image2).grid(row = i, column = j)

        window.mainloop()

TicTacToe()
                
