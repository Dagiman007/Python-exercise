from tkinter import *

class MoveBall:
    def __init__(self):
        window = Tk()
        window.title('Moving Ball')

        self.width = 300
        self.height = 300
        self.x = 0  # Starting center position
        self.y = 0
        self.dx = 5  # Move right by default
        self.dy = 5  # Move down by default

        self.canvas = Canvas(window, bg = 'green', width = self.width, height = self.height)
        self.canvas.pack()
        self.ballImage = PhotoImage(file = 'C:/Users/DagiMan/Desktop/Python Programming - CBT Nuggets/Exercise/Ex docs/image/soccerball.gif')
        
        self.canvas.create_image(self.x, self.y, image = self.ballImage, tags = 'ball')
        
        frame = Frame(window)
        frame.pack()

        leftButton = Button(frame, text = 'Left', command = self.moveLeft)
        leftButton.pack(side = LEFT)
        rightButton = Button(frame, text = 'Right', command = self.moveRight)
        rightButton.pack(side = LEFT)
        upButton = Button(frame, text = 'Up', command = self.moveUp)
        upButton.pack(side = LEFT)
        downButton = Button(frame, text = 'Down', command = self.moveDown)
        downButton.pack(side = LEFT)

        
        window.mainloop()

    def moveLeft(self):
        self.x = self.x - self.dx
        self.animate()

    def moveRight(self):
        self.x = self.x + self.dx
        self.animate()

    def moveUp(self):
        self.y = self.y - self.dy
        self.animate()

    def moveDown(self):
        self.y = self.y + self.dy
        self.animate()

    def animate(self):
        self.canvas.delete('ball')
        self.canvas.update()
        if self.x > self.width or self.x < 0:
            self.x = 0
        if self.y > self.height or self.y < 0:
            self.y = 0
        self.canvas.create_image(self.x, self.y, image = self.ballImage, tags = 'ball')

MoveBall()
        

    
        
        
    
