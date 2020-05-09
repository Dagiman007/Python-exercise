from tkinter import *
from CheckSudokuSolution import isValid
import tkinter.messagebox

class SudokuGUI:
    def __init__(self):
        window = Tk()
        window.title('Check Sudoku solution')

        frame = Frame(window)
        frame.pack()

        self.cells = []
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        for i in range(9):
            for j in range(9):
                Entry(frame, width = 2, justify = RIGHT,
                      textvariable = self.cells[i][j]).grid(
                          row = i, column = j)

        Button(window, text = 'Validate',
               command = self.validate).pack()

        window.mainloop()

    def validate(self):
        # Get the numbers from the entries
        values = [[eval(x.get()) for x in self.cells[i]] for i in range(9)]

        if isValid(values):
            tkinter.messagebox.showinfo('Check Sudoku solution',
                                        'The solution is valid')
        else:
            tkinter.messagebox.showwarning('Check Sudoku solution',
                                           'The solution is invalid')

SudokuGUI()
