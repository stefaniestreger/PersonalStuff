def main():
    my_string = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    silly_encrypt(my_string)
    print('English input: ', my_string)
    print('Silly Encryption output: ', silly_encrypt(my_string))

def silly_encrypt(my_string):
    word_list = my_string.split()
    new_list = []
    for x in word_list:
        first_letter = str(x[0])
        end_letter = str(x[1:])
        new_word = end_letter + first_letter + 'IE'
        new_list.append(new_word)
        updated_string = (" ".join(new_list))
    return updated_string

main()

