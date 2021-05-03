database_user = {
   'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
}

from datetime import datetime


def login():
    #login function here
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Welcome " + name + "\nLogin Time:" + current_time)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False


def bankOperations():
    current_balance=0
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        amount=input('How much would you like to withdraw?\n')
        print("Take your cash\n")
        bankOperations()
                
    elif(selectedOption == 2):
        amount=int(input('How much would you like to deposit?\n'))
        current_balance += amount
        print('Your current balance is {}'.format(current_balance))
        bankOperations()
                
    elif(selectedOption == 3):
        complaint=input(('What issue will you like to report?\n'))
        print('Thank you for coontacting us')
        bankOperations()

    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')


print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()
            
else:
    print('Login failed, username or password incorrect')