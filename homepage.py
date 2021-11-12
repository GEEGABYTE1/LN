import time 
from localnetwork import network
from accounts import user



class Homepage:

    def landing(self):
        print("Welcome to LN")
        time.sleep(0.2)
        print("Short form for LocalNetwork")
        time.sleep(0.2)
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


        
    def global_network(self):
        user_user = user.logged_in_user[0]
        print(network.sending_message(user_user))


        

test = Homepage()
print(test.landing())