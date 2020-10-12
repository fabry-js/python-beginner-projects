import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def get_len():
    length = input("Quanto deve essere lunga la password?: ")
    return int(length)

def password_combination_choice():
    '''
    Prompt a user to choose password character combination which could either be digits, letters, 
    punctuation or combibation of either of them.

    :returns list <class 'list'> of boolean. Defaults to [True, True, True] for invalid choice
        0th list item represents digits
        1st list item represents letters
        2nd list item represents punctuation
    '''
    want_digits = input("Vuoi i numeri ? (True / False): ")
    want_letters = input("Vuoi le lettere ? (True / False): ")
    want_puncts = input("Vuoi i caratteri speciali ? (True / False): ")
    
    try:
        want_digits = eval(want_digits.title())
        want_letters = eval(want_letters.title())
        want_puncts = eval(want_puncts.title())
        return [want_digits, want_letters, want_puncts]
    
    except NameError as e:
        print("Input non valido. Scrivi 'True' o 'False' ")

    return [True, True, True]


def pass_gen(cbl, length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified
    :cbl-> a list of boolean values representing a user choice for 
        string constant to be used to generate password.
        0th list item represents digits    
             True to add digits to constant False otherwise
        1st list item represents letters   
             True to add letters to constant False otherwise
        2nd list item represents punctuation
             True to add punctuation to constant False otherwise
    :returns string <class 'str'>
    '''
    printable = fetch_string_constant(cbl)
    
    printable = list(printable)
    random.shuffle(printable)
    
    random_password = random.choices(printable, k=length)
    
    random_password = ''.join(random_password)
    return random_password

def fetch_string_constant(choice_list):
    '''
    Returns a string constant based on users choice_list.
    Returned string constant can either be digits, letters, punctuation or
    combination of them.
    : choice_list --> list <class 'list'> of boolean
        0th list item represents digits    
            True to add digits to constant False otherwise
        1st list item represents letters   
            True to add letters to constant False otherwise
        2nd list item represents punctuation
            True to add punctuation to constant False otherwise
    '''
    string_constant = ''
    
    string_constant += NUMBERS if choice_list[0] else ''
    string_constant += LETTERS if choice_list[1] else ''
    string_constant += PUNCTUATION if choice_list[2] else ''
    
    return string_constant


if __name__ == "__main__":
    length = get_len()
    choice_list = password_combination_choice()
    password = pass_gen(choice_list, length)
    print(password)

    