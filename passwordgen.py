 # build a program that generates 15 unique password characters

if __name__ == '__main__':
    import random, string

    number_of_passwords=16 
    length_of_password=6

    characters=string.ascii_letters + string.digits + string.punctuation

    for password_index in range(number_of_passwords):
        password = ""
 
        for index in range(length_of_password):
            password = password + random.choice(characters)
        
        print('password {} generated: {}'.format(password_index, password))