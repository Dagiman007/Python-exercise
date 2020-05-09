from tkinter import *
import random

class DeckOfCardsGUI:
    def __init__(self):
        window = Tk()
        window.title('Pick Four Cards Randomly')

        self.imageList = []  # Store images for cards
        for i in range(1,53):
            self.imageList.append(PhotoImage(file = 'C:/Users/DagiMan/Desktop/Python Programming - CBT Nuggets/Exercise/image/card/'
                                             + str(i) + '.gif'))

        frame = Frame(window)
        frame.pack()

        self.labelList = []  # A list of four labels
        for i in range(4):
            self.labelList.append(Label(frame,
                                        image = self.imageList[i]))
            self.labelList[i].pack(side = LEFT)

        Button(window, text = 'Shuffle',
               command = self.shuffle).pack()

        window.mainloop()

    # Choose four random cards
    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[i]

DeckOfCardsGUI()
        
