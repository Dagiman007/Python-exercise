from tkinter import *

window = Tk()  # create a window
label = Label(window,text='Welcome to ppython') #create a label
button = Button(window,text='click this') #create a button
label.pack() #place the label in the window
button.pack() #place the button in the window

window.mainloop()
