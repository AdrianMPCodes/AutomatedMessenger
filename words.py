with open('/Users/adrianmendozaperez/Documents/Python/sms/text.txt', 'r') as f:
    text = f.read()
    words = text.split()
length = len(words)

for x in range (length):
    my_msg = words[x]
    print(my_msg)
