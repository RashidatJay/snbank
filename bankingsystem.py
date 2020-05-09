
import random
import os
from datetime import datetime
def login():
    welcome_options=input('Welcome staff to the bank, choose Login or Close App:')
    while welcome_options=='Login':
        username_similar=input('Enter your username below:\n')
        password_similar=input('Enter your password below:\n')
    
   
        with open('staff.txt','r')as f:
            for line in f:
                info=line.split(',')
               
            if username_similar in line and password_similar in line:
                print('Login Sucessful')
       
                user_session=open('usersessions.txt','w')
                date=str(datetime.now())
                user=user_session.write(username_similar +' ' +date)
                user_session.close()
            
                login_sucess=True
                while login_sucess==True:  
                    options=input('Enter 1 to create a New bank account, Enter 2 to check Account details, Enter 3 to Logout:')
                    if options=='1':
                        account_name=input('Enter Account Name:\n')
                        opening_balance=input(str('Enter your opening balance:\n'))
                        account_type=input('Enter your account type:\n')
                        account_email=input('Enter your account email:\n')
                        account_number=''
                        for i in range(10):
                            account_number += str(random.randint(0,9))
                        with open('customers.txt', 'w') as customers_info:
                            customers_info.write(account_name+',')
                            customers_info.write(opening_balance+',')
                            customers_info.write(account_type+',')
                            customers_info.write(account_email+',')
                            customers_info.write(account_number)
                            print(f'Your account number is {account_number}')
   
                    
                    elif options=='2':
                        account_number_request=int(input('Enter your account number here:'))
                        customer=open('customers.txt','r')
                        number_details=customer.read()
                        print(number_details)
                   
                    
                    elif options=='3':
                        os.unlink('usersessions.txt')
                        print('Thankyou for logging in')
                        print('User session is now deleted')
                        login()
                        
                    else:
                        print('invalid input')
            else:
                print('Invalid login details, try again')
      

    if welcome_options=='Close App':
        print('Thanks for banking with us, you  have now exited the app')
        exit()
       
    
        

        

       
login()