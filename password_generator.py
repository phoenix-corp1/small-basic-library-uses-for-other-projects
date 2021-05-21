import random
import string

def get_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    length = int(input("enter the length of password:"))
    password = ''.join(random.choice(password_characters)for i in range(length))

    print("your password is:",password)

get_password('length')