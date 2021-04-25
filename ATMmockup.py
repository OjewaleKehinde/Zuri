import random
database ={123456789:['Kehinde', 'paul', 'paul1234']}
accountNumbers= list(database.keys())

def menu():
    print('Welcome to Chase Bank')

    firstAction = input("Enter 1 to login if you already have an account. If not, enter 2 to sign up with Chase bank \n")
    if firstAction == '1':
        login()
    elif firstAction == '2':
        register()
    else:
        print("You have not selected a valid option")
        menu()
    
def login():
    accountNumberEntered = int(input("Please input your account number to log in \n"))
    password = input("Please input your password \n")
    for accountNumber,credentials in database.items():
        if accountNumber == accountNumberEntered:
            if credentials[2] == password:
                bankOperation(credentials)
            elif credentials[2] != password:
                print('Invalid account or password')
            login()
        elif accountNumber != accountNumberEntered:
            print('Invalid account or password')
            login()
    
    
def logout():
    login()

def register():
    first_name =input("What is your first name?\n")
    last_name =input("What is your last name?\n")
    password =input("create your password\n") 
    accountNumber = generateAccountNumber()
    
    database[accountNumber] = [first_name, last_name,password]
 
    login()

def bankOperation(user):
      selectedOption = int(input("What would you like to do? 1.Deposit  2.Withdrawal  3.Complaint 4.Logout \n"))
      if selectedOption == 1:
        deposit(user) 

      elif selectedOption == 2:
        withdrawal(user)
      elif selectedOption ==3:
        complaint()  
      elif selectedOption ==4:
          logout()                    
      else:
        print("Invalid option selected")
      bankOperation(user)
      
                     
                      
def withdrawal(user):
    amount= input('Select the amount you would like to withdraw \n')
    print("Please take your cash\n")

    

def deposit(user):
    amount = input('Enter the amount you would like to deposit \n')


def complaint():
    input('Please type your complait in the box below \n')
    print("Thank you for contacting Chase bank. Our team will get back to you shortly \n") 
      


def generateAccountNumber():
    generatedAccountNumber = random.randrange(1111111111, 9999999999)
    print('Your registration has been completed succssfully. Welcome to Chase bank. \nYour account number is {}'.format(generatedAccountNumber))


menu()