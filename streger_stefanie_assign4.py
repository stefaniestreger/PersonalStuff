monster = int(input("Enter a monster's number:"))
if monster == 0:
    print("The monster color is: purple")
elif monster >= 1 and monster <= 10:
    if (monster % 2) == 0:
        print("The monster color is: black")
    else:
        print("The monster color is: blue")
elif monster >= 11 and monster <= 18:
    if (monster % 2) == 0:
       print("The monster color is: blue")
    else:
        print("The monster color is: black")
elif monster >= 19 and monster <= 28:
    if (monster % 2) == 0:
       print("The monster color is: black")
    else:
        print("The monster color is: blue")
elif monster >= 29 and monster <= 36:
    if (monster % 2) == 0:
       print("The monster color is: blue")
    else:
        print("The monster color is: black")
elif monster < 0 or monster > 36:
        print("You have entered an invalid number out of this range")
