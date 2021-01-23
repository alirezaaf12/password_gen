import string
import random


def generator(lenght):
    LETTERS = string.ascii_letters
    NUMBERS = string.digits  
    PUNCTUATION = string.punctuation    

    selectables = f"{LETTERS}{NUMBERS}{PUNCTUATION}"


    password = ""
    num = 0
    while num <= lenght:
        pass_sel = random.choice(selectables)
        password += pass_sel
        num += 1

    print(password)

user_input = input("how many character password should have? : ")

user_input = int(user_input)

generator(user_input)