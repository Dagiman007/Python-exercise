from tkinter import *

class MouseKeyEventDemo:
    def __init__(self):
        window = Tk()
        window.title('Mouse key event demo')
        canvas = Canvas(window, bg = 'white', width = 200, height = 100)
        canvas.pack()

        # Bind with <Button-1> event
        canvas.bind('<Button-1>', self.processMouseEvent)

        # Bind with <Key> event
        canvas.bind('<key>',self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()

    def processMouseEvent(self, event):
        print('Clicked at ',event.x,event.y)
        print('Position in the screen ', event.x_root, event.y_root)
        print('Which button is clicked?', event.num)

    def processKeyEvent(self, event):
        print('keysym? ', event.keysym)
        print('Char? ', event.char)
        print('Keycode? ', event.keycode)

MouseKeyEventDemo()
