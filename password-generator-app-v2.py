import random
upperCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
menu = int(input('1. Generate Uppercase Password\n2. Generate Lowercase Password\n3. Generate Numbers Password\n4. Generate Special Characters Password\n5. Generate All Characters Password\nChoose a number: '))

if menu == 1:
    password_lenght = int(
        input('How many characters do you want in your password? '))
    for x in range(0, password_lenght):
        password = random.choice(upperCharacters)
        print(password, end='')

elif menu == 2:
    password_lenght = int(
        input('How many characters do you want in your password? '))
    for x in range(0, password_lenght):
        password = random.choice(lowerCharacters)
        print(password, end='')

elif menu == 3:
    password_lenght = int(
        input('How many characters do you want in your password? '))
    for x in range(0, password_lenght):
        password = random.choice(numbers)
        print(password, end='')

elif menu == 4:
    password_lenght = int(
        input('How many characters do you want in your password? '))
    for x in range(0, password_lenght):
        password = random.choice(specialCharacters)
        print(password, end='')

elif menu == 5:
    password_lenght = int(
        input('How many characters do you want in your password? '))
    for x in range(0, password_lenght):
        password = random.choice(
            upperCharacters + lowerCharacters + numbers + specialCharacters)
        print(password, end='')
