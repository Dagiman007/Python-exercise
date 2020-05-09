from Account import Account

def main():
    # Create ten accounts
    accounts = [Account(i, 100) for i in range(10)]

    while True:
        # Prompt the user to enter an id
        ID = eval(input('Enter an account id: '))
        while ID > 9 and ID < 0:
            ID = eval(input('Incorrect id, enter again!: '))

        account = accounts[ID]
        
        print('Main Menu')
        print('1: Check Balance\n2: Withdraw\n3: Deposit\n4: Exit')

        choice = eval(input('Enter a choice: '))

        while choice != 4:
            if choice == 1:
                print('The balance is ', account.getBalance())
            elif choice == 2:
                withdrawAmount = eval(input('Enter an amount to withdraw: '))
                account.withdraw(withdrawAmount)
            elif choice == 3:
                depositAmount = eval(input('Enter an amount to deposit: '))
                account.deposit(depositAmount)
            else:
                break
            print('Main Menu')
            print('1: Check Balance\n2: Withdraw\n3: Deposit\n4: Exit')

            choice = eval(input('Enter a choice: '))

                

main()
