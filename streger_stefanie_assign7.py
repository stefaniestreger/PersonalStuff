total = 0
max_value = int(input('Enter the value for the maximum number: '))
number = int(input('Enter a number between 1 and ' + str(max_value) + ' to add: '))
while number >= 0:
    if number > 0 and number <= max_value:
        total += number
    elif number == 0 or number > max_value:
        print('Invalid number')
    number = int(input('Enter a number between 1 and ' + str(max_value) + ' to add: '))
else:
    print('Sum of all valid number you entered: ' + str(total))
