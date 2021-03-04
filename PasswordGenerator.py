
import string
import random
from datetime import date

today = date.today()
print("Welcome to Fae's password generator,\
        \n a program dedicated to suggest a strong and safe password for you.\
        \n Please note that, your password must be longer than 6 characters")
username = input("please what's your name? \n>>>")



def ps_generator(x = 3, y = 3, z = 3):
    """returns a password (a string) of a given length specified by the user"""
    
    
    #if no_alph + no_numsy != length:
    alph = list(string.ascii_lowercase + string.ascii_uppercase)
    num = [n for n in range(1, 10)] 
    symbol = list("~!@#$%^&*()_+{}[]:'<>?,./")
    
    alph_char =  random.sample(alph, x)
    num_char = random.sample(num, y)
    sym_char = random.sample(symbol, z)
    password = [str(i) for i in (alph_char + num_char + sym_char)]
    random.shuffle(password)
    spassword = "".join(password)
    return spassword


def gen_password(n = 5):

    length = ""
    while length is not int:
        
        try:
            length = int(input('How long do you want your password to be? \n>>>'))
            no_alph = int(input("please, enter the number of letters your password should contain: \n >>>"))
            no_numsy = int(input("please, enter the number of numerics and symbols your password should contain: \n>>> "))
            break
        except ValueError:
            print('INPUT MUST BE AN INTEGER: Please enter a valid number: ')

    no_sym = length - (no_alph + no_numsy)
        
    if length < 6:
        raise ValueError("Password must be longer than 6 characters")
    
    else:        
        passwords = []
        for v in range(n):
            password = ps_generator(x = no_alph, y = no_numsy, z = no_sym)
            passwords.append(password)
        
    return passwords


result = gen_password()
print(f'{username} consider using one of these passwords\n')
for p in result:
    print(p, "\n")
print("Thanks for using our service")
    
        
    
