from datetime import datetime
import time
from pymongo import MongoClient
from termcolor import colored
from hashmap import chatbase


class Network:
    cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['socialmedia']['messaging']
    all_messages = db.find({})
    chats = {}
    restart = False
    
    

    def sending_message(self, user):
        while True:
            date = datetime.now().strftime("%x")
            for message in self.all_messages:
                try:
                    if date != message['Date']:
                        print(colored('Today: {}'.format(message['Time']), 'red'))
                    else:
                        print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                    print(colored("From: ", 'green'), message['Id'])
                    print(colored("Message: ", 'green'), message['Message'])
                    print('-'*25)
                except:
                    pass
            
            person = "Name: {}".format(user)
            message = input("Message: ")

            if message == '/quit':
                break
            elif message == '/update':
                self.restart()
            else:
                time = datetime.now().strftime("%X")
                msg = {"Id": person, "Message": message, "Date": date, "Time":time}
                self.db.insert_one(msg)
                print('-'*25)

    def create_gc(self, name, password):
        name = name.strip(" ")
        cluster_for_chat = self.cluster['socialmedia']['gas']
        ext_db = self.cluster['socialmedia']
        name_db = ext_db[name]
        dictionary = {name: datetime.now()}
        name_db.insert_one(dictionary)
        self.chats[name] = password
        chatbase.setter(name, name_db)

    def join_gc(self, name, chat_base):
        db = chat_base 
        current_messages = db.find({})
        count = 0
        while True:
            date = datetime.now().strftime("%x")
            for message in current_messages:
                if count == 0:
                    pass 
                else:
                    try:
                        if date != message['Date']:
                            print(colored('Today: {}'.format(message['Time']), 'red'))
                        else:
                            print(colored("{} ~ {}".format(message['Date'], message['Time']), "red"))
                        print(colored("From: ", 'green'), message['Id'])
                        print(colored("Message: ", 'green'), message['Message'])
                        print('-'*25)
                    except:
                        pass
                count += 1
            
            person = "Name: {}".format(name)
            message = input("Message: ")

            if message == '/quit':
                break
            elif message == '/update':
                self.restart()
                
                
            else:
                time = datetime.now().strftime("%X")
                msg = {"Id": person, "Message": message, "Date": date, "Time":time}
                chat_base.insert_one(msg)
                print('-'*25)


    def find_chat(self, name):
        try:
            chat_cluster = self.cluster['socialmedia'][name]
            return chat_cluster
        except:
            print("Groupchat not found")
    
    def restart(self):
        print("\n")
        import sys
        print("Updating the database")
        import os
        os.execv(sys.executable, ['python'] + sys.argv)
        

        
                    


        

        
        


network = Network()