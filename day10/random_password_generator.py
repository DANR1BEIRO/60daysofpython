import random
import string

def password_generator(prompt):
    _lenght = prompt
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    while len(password) < _lenght:
        password += random.choice(characters)
    print(f"Your random password is: {password}")

if __name__=="__main__":
    password_generator(int(input("Max password number: ")))


