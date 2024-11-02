
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    # wb = write bytes mode
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()

    file.close()
    return key

master_pswd = input("Enter your master password: ") # use this password to encrypt passwords
key = load_key() + master_pswd.encode() # takes string and converts into bytes

# initialize the encryption module
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # rstrip() strip off carriage return from the line
            data = line.rstrip()

            # will look for the certain character and return as a list format
            user, passw = data.split('|')
            print("User: " , user , "| Password: ",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # allows to open a file and automatically closes the file
    # w r a modes
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add): press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue
