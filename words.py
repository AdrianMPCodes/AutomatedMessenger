#Change filepath of where the script is
with open('[INSERT FILEPATH OF SCRIPT]', 'r') as f:
    text = f.read()
    words = text.split()
length = len(words)

for x in range (length):
    my_msg = words[x]
    print(my_msg)
