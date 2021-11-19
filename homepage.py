import time 
from localnetwork import network
from accounts import user
from termcolor import colored





class Homepage:
    network = network

    def user_connection(self):
        print("\n")
        print("/sign_up: If you don't have an account")
        time.sleep(0.2)
        print("\n")
        print("/sign_in: If you have already have an account")
        while True:
            prompt = str(input(': '))
            prompt = prompt.lower()
            prompt = prompt.strip(" ")
            if prompt == '/sign_up':
                while True:
                    sign_up_process = user.sign_up()
                    if sign_up_process == True:
                        print(colored("You have successfully signed up! ", 'green'))
                        time.sleep(0.2)
                        print("You can now sign in")
                        break
                    else:
                        print(colored("oops, there seems to be an error", 'red'))
                        break
            elif prompt == '/sign_in':
                process = user.sign_in()
                if process:
                    time.sleep(0.3)
                    print("\n")
                    self.landing()
                else:
                    print("The process was incomplete ")
            else:
                print("That command seems to be invalid")


    def landing(self):
        print("Welcome to LN")
        time.sleep(0.2)
        print("Short form for LocalNetwork!")
        time.sleep(0.2)
        print("\n")
        print("/global_chat: To acess the global chat worldwide")
        time.sleep(0.2)
        print("/create_gc: To create a groupchat")
        time.sleep(0.2)
        print("/join_gc: To join a groupchat")
        time.sleep(0.2)
        print("/gc: To start talking in group chat!")
        time.sleep(0.2)
        
        while True:
            print("\n")
            user_prompt = str(input(': '))

            if user_prompt == '/global_chat':
                print("Accessing the global network...")
                time.sleep(0.2)
                self.global_network()
            
            elif user_prompt == '/create_gc':
                chat_name = str(input("Please enter a name for your group chat: "))
                chat_password = str(input("Please enter a password for the chat: "))
                self.network.create_gc(chat_name, chat_password)
                chats = user.logged_in_user[-1]
                chats.append(chat_name)
                print(colored("Group chat {name} successfully made!".format(name=chat_name), 'green'))
                time.sleep(0.2)
                print(colored("You can now add or invite others! ", "blue"))

            elif user_prompt == '/join_gc':
                print("\n")
                for network in self.network.chats.keys():
                    print(network)
                    print('-'*24)
                    time.sleep(0.2)
                print('\n')
                des_chat_name = str(input("Please type in a gc name you want join: "))
                des_chat_name = des_chat_name.strip(" ")
                
                if not des_chat_name in list(self.network.chats.keys()):
                    print(colored("That group chat does not seem to be made", "red"))
                    time.sleep(0.2)             
                    print("Try creating a new group chat instead or make sure you typed the name correctly!")
                else:
                    user_chat_password = str(input("Please type in the chat password: "))
                    chat_password = self.network.chats[des_chat_name]
                    if user_chat_password == chat_password:
                        chat_base = self.network.find_chat(des_chat_name)
                        time.sleep(0.2)
                        print(colored("{username} has joined the chat! ".format(username=user.logged_in_user[0]), "blue"))
                        self.network.join_gc(user.logged_in_user[0], chat_base)

            else:
                print("Command not valid")



   

        
    def global_network(self):
        if user.signed_in:
            user_user = user.logged_in_user[0]
            print(self.network.sending_message(user_user))


        

test = Homepage()
print(test.user_connection())