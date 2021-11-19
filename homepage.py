import time 
from localnetwork import network
from accounts import user
from termcolor import colored



class Homepage:

    def user_connection(self):
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
                print(colored("Group chat {name} successfully made!".format(name=chat_name), 'green'))
                network.create_gc(chat_name, chat_password)
                chats = user.logged_in_user[-1]
                chats.append(chat_name)
                time.sleep(0.2)
                print(colored("You can now add or invite others! ", "blue"))



        
    def global_network(self):
        if user.signed_in:
            user_user = user.logged_in_user[0]
            print(network.sending_message(user_user))


        

test = Homepage()
print(test.user_connection())