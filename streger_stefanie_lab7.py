name = input('Enter a username that has only alphabetical characters and is between 5 and 10 characters: ')
while not name.isalpha():
    print('Invalid username! Please try again.')
    print(name)
    name = input('Enter a username that has only alphabetical characters and is between 5 and 10 characters: ')
    continue
while name.isalpha():
    if len(name) < 5 or len(name) > 10:
        print('Invalid username! Please try again.')
        print(name)
        name = input('Enter a username that has only alphabetical characters and is between 5 and 10 characters: ')
    else:
        print(name)
        print('Username accepted.')
        break
else:
    print('Invalid username! Please try again.')
    print(name)
    name = input('Enter a username that has only alphabetical characters and is between 5 and 10 characters: ')






