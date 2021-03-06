from pymongo import MongoClient
from termcolor import colored
import time


class Users:
    cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['socialmedia']['accounts']
    all_accounts = db.find({})
    signed_in = False
    logged_in_user = None

    def sign_up(self):
        user_name = str(input("Please enter a username you would like to go by (Note: Users externally will see this name): "))
        password = str(input("Please enter a password: "))
        if user_name == '/quit' or password == '/quit':
            return False
        acc = {'User': user_name, 'Password': password}
        self.db.insert_one(acc)
        return True

    def sign_in(self):
        while True:
            user = str(input("Username: "))
            
            users = []
            passwords = []
            for account in self.all_accounts:
                users.append(account['User'])
                passwords.append(account['Password'])
            if user == '/quit':
                    break

            if user in users:
                while True:
                    password = str(input("Password: "))
                    
                    if password == '/quit':
                        break
                    elif password in passwords:
                        self.signed_in = True 
                        self.logged_in_user = [user, password, []]
                        print(colored("You have successfully signed in! ", 'green'))
                        break
                    else:
                        print("Password is incorrect")

                if self.signed_in == False:
                    print("You have left the logging in process...")
                else:
                    break


            else:
                print(colored("That username does not seem to be registered on this network", 'red'))
                time.sleep(0.2)
                print(colored("Try signing up to the network!", 'blue'))
        
        if self.signed_in == False:
            print("You have left the logging in process...")
        
        return self.signed_in
                

            


        
    
    
user = Users()

