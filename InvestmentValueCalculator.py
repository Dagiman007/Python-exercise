from tkinter import *

class InvestmentCalculator:
    def __init__(self):
        window = Tk()
        window.title('Investment Calculator')
        
        self.investmentAmountVar = StringVar()
        self.yearsVar = StringVar()
        self.annualInterestRateVar = StringVar()

        frame0 = Frame(window)
        frame0.pack()

        Label(frame0, text = 'Investment Amount').grid(row = 1, column = 1)
        Entry(frame0, width = 30, textvariable = self.investmentAmountVar).grid(
            row = 1, column = 2)
        Label(frame0, text = 'Years').grid(row = 2, column = 1)
        Entry(frame0, width = 30, textvariable = self.yearsVar).grid(
            row = 2, column = 2)
        Label(frame0, text = 'Annual Interest Rate').grid(row = 3, column = 1)
        Entry(frame0, width = 30, textvariable = self.annualInterestRateVar).grid(
            row = 3, column = 2)
        Label(frame0, text = 'Future Value').grid(row = 4, column = 1)
        
        self.futureValue = StringVar()
        Label(frame0, textvariable = self.futureValue).grid(row = 4, column = 2)

        frame1 = Frame(window)
        frame1.pack()

        Button(frame1, text = 'Calculate', command = self.calculate).pack(side = RIGHT)

    def calculate(self):
        self.monthlyInterestRate = eval(self.annualInterestRateVar.get()) / 1200
        value = eval(self.investmentAmountVar.get()) * \
                           (1 + self.monthlyInterestRate) ** (eval(self.yearsVar.get()) * 12)

        self.futureValue.set(str(value))
                        

InvestmentCalculator()

        
        
