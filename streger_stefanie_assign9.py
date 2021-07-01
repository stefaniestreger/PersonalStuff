#defines the menu items
feet_inches = 1
yards_feet = 2
miles_yards = 3
miles_feet = 4
quit_choice = 5

def main(): #defines the main program functions
    displayMenu()
    choice = int(input('Please choose a menu option: '))
    while choice != quit_choice:
        if choice == feet_inches:
            feet = int(input('Enter the number of feet: '))
            feetToInches(feet)
            print(feetToInches(feet))
            print('                      ')
            displayMenu()
            choice = int(input('Please choose a menu option: '))
        elif choice == yards_feet:
            yards = int(input('Enter the number of yards: '))
            print(yardsToFeet(yards))
            print('                      ')
            displayMenu()
            choice = int(input('Please choose a menu option: '))
        elif choice == miles_yards:
            miles = int(input('Enter the number of miles: '))
            print(milesToYards(miles))
            print('                      ')
            displayMenu()
            choice = int(input('Please choose a menu option: '))
        elif choice == miles_feet:
            miles = int(input('Enter the number of miles: '))
            print(milesToFeet(miles))
            print('                      ')
            displayMenu()
            choice = int(input('Please choose a menu option: '))
        else:
            print('Your choice is not valid.')
            print('                      ')
            displayMenu()
            choice = int(input('Please choose a menu option: '))
    while choice == quit_choice:
        print('Goodbye')
        break

def displayMenu(): #defines how the menu should be displayed
    print('Conversion Menu')
    print('                      ')
    print('1. Convert feet to inches')
    print('2. Convert yards to feet')
    print('3. Convert miles to yards')
    print('4. Convert miles to feet')
    print('5. Exit')
    print('                      ')

def feetToInches(feet): #defines the feet conversion function
    inches = feet * 12
    return 'There are ' + str(inches) + ' inches in ' + str(feet) + ' feet.'

def yardsToFeet(yards): #defines the yards conversion function
    feet = yards * 3
    return 'There are ' + str(feet) + ' feet in ' + str(yards) + ' yards.'

def milesToYards(miles): #defines the miles > yards conversion function
    yards = miles * 1760
    return 'There are ' + str(yards) + ' yards in ' + str(miles) + ' miles.'

def milesToFeet(miles): #defines the miles > feet conversion function
    feet = miles * 5280
    return 'There are ' + str(feet) + ' feet in ' + str(miles) + ' miles.'

main() #calls the main function for input
