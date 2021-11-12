from datetime import datetime
import time
from pymongo import MongoClient
from termcolor import colored


class Network:
    cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['socialmedia']['messaging']
    all_messages = db.find({})
    
    

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
            else:
                time = datetime.now().strftime("%X")
                msg = {"Id": person, "Message": message, "Date": date, "Time":time}
                self.db.insert_one(msg)
                print('-'*25)
        


network = Network()