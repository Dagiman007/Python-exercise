from tkinter import *

SIZE = 8
class EightQueens:
    def __init__(self):
        self.queens = SIZE * [-1]  # Queen position
        self.search(0)  # Search for a solution from row 0

        # Display solutions in queens
        window = Tk()
        window.title('Eight Queens')

        image = PhotoImage(file = r'C:\Users\DagiMan\Desktop\Python Programming - CBT Nuggets\Exercise\Ex docs\image\queen.gif')
        for i in range(SIZE):
            for j in range(SIZE):
                if self.queens[i] == j:
                    Label(window, image = image).grid(
                        row = i, column = j)
                else:
                    Label(window, width = 5, height = 2,
                          bg = 'red').grid(row = i, column = j)

        window.mainloop()

    def search(self, row):
        if row == SIZE:  # Stopping condition
            return True

        for column in range(SIZE):
            self.queens[row] = column # Place it at (row, column)
            if self.isValid(row, column) and self.search(row + 1):
                return True  # Found and exit loop

        # No solution for a queen placed at any column of this row
        return False

    # Check if a queen can be placed at row i and column j
    def isValid(self, row, column):
        for i in range(1, row + 1):
            if (self.queens[row - i] == column  # Check column
                or self.queens[row - i] == column - i
                or self.queens[row - i] == column + i):
                return False  # There is conflict
        return True # No conflict

EightQueens()
