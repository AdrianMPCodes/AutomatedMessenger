import os
import config

#To run in  terminal: 
#cd documents, cd python, cd sms, python3 main.py
#creates functions to read a file and to send a message one word at a time
def get_words(file_path): 
    with open(file_path, 'r') as f:
        text = f.read()
        words = text.split()
    return words #array of each word in text.txt

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    words = get_words('text.txt') #gives the file path 
    for x in words: #gets one word at a time in the txt.txt file starting from 0-max 
        send_message(config.number, x) #sends the one word
