def main():
    num1 = int(input('Enter a positive number: '))
    num2 = int(input('Enter another positive number: '))
    new_thing = is_equal(num1, num2)
    if new_thing == True:
        print("Equal")
    else:
        print("Not Equal")

def is_equal(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

main()