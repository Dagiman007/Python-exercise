from tkinter import *

class BarChart:
    def __init__(self):
        window = Tk()
        window.title('Bar Chart')

        self.canvas = Canvas(window, width = 300, height = 300, bg = 'white')
        self.canvas.pack()

        self.canvas.create_line(10, 290, 290, 290)

        self.canvas.create_rectangle(10, (int(self.canvas['height']) - 10) - (290 * 0.2), 65, 290, fill = 'red')
        self.canvas.create_rectangle(70, (int(self.canvas['height']) - 10) - (290 * 0.1), 135, 290, fill = 'red')
        self.canvas.create_rectangle(140, (int(self.canvas['height']) - 10) - (290 * 0.3), 205, 290, fill = 'red')
        self.canvas.create_rectangle(210, (int(self.canvas['height']) - 10) - (290 * 0.4), 275, 290, fill = 'red')
        
        self.canvas.create_text(30, (int(self.canvas['height'])) - (290 * 0.2) + 20, text = 'Project--20%')
        self.canvas.create_text(90, (int(self.canvas['height'])) - (290 * 0.1) + 20, text = 'Quizzes--10%')
        self.canvas.create_text(160, (int(self.canvas['height'])) - (290 * 0.3) + 20, text = 'Midterm--30%')
        self.canvas.create_text(230, (int(self.canvas['height'])) - (290 * 0.4) + 20, text = 'Final--40%')



        window.mainloop()

BarChart()


