from tkinter import *

class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title('Animation Demo')

        width = 250
        canvas = Canvas(window, bg = 'white',
                        width = 150, height = 50)
        canvas.pack()

        x = 0
        canvas.create_text(x, 30,
                           text = 'I like to move', tags = 'text')
        dx = 3
        while True:
            canvas.move('text', dx, 0) #Move the text dx unit
            canvas.after(100)   #Sleep for 100 miliseconds
            canvas.update()  #Update the canvas
            if x < width:
                x += dx    #Get the current position for the string
            else:
                x = 0   #Reset string postion to the beginning
                canvas.delete('text')
                #Redraw text at the beginning
                canvas.create_text(x, 30, text = 'I like to move',
                                   tags = 'text')

        window.mainloop()

AnimationDemo()
                
                
