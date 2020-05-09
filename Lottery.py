import random

#generate lottery number
lottery = random.randint(0,99)

#prompt the user to enter a guess
guess = eval(input("Enter your lottery pick,two digit number: "))

#Get digits from the lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

#Get digits from the guess number
guessDigit1 = guess // 10
guessDigit2 = guess % 10

#check the guess
if guess == lottery:
    print("Exact match! you win $10,000.")
elif (guessDigit2 == lotteryDigit1 and \
      guessDigit1 == lotteryDigit2):
    print("Match all digit: you win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit2 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("sorry, no match")
