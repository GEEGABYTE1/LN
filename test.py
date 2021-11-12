from pymongo import MongoClient
from datetime import datetime 
from termcolor import colored 

cluster = MongoClient("mongodb+srv://GEEGABYTE1:12345@socialmedia.few6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['socialmedia']['messaging']
all_messages = db.find({})

date = datetime.now().strftime("%x")

for message in all_messages:
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

person = input('Name: ')
message = input('Message: ')
time = datetime.now().strftime("%X")
msg = {"Id": person, "Message": message, "Date": date, "Time":time}
print(msg)
db.insert_one(msg)