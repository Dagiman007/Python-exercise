from tkinter import *

class ImageDemo:
    def __init__(self):
        window = Tk()
        window.title('Image Demo')

        #Create PhotoImage objects
        aImage = PhotoImage(file = 'image/a.gif')
        
        cImage = PhotoImage(file = 'image/c.gif')
        dImage = PhotoImage(file = 'image/d.gif')
        eImage = PhotoImage(file = 'image/e.gif')
        fImage = PhotoImage(file = 'image/f.gif')

        #frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = aImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = aImage)
        canvas['width'] = 200
        canvas['height'] = 100
        canvas.pack(side = LEFT)

        #frame2 contains buttons, checkbuttons and radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = cImage).pack(side = LEFT)
        Button(frame2, image = dImage).pack(side = LEFT)
        Checkbutton(frame2, image = eImage).pack(side = LEFT)
        Radiobutton(frame2, image = eImage).pack(side = LEFT)
        Radiobutton(frame2, image = fImage).pack(side = LEFT)

        window.mainloop()

ImageDemo()
