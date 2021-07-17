def main():
    file_name = input('Enter the name of the file: ')
    new_file = open((file_name), 'r')
    line = new_file.readline()
    target_numbers = []
    bad_numbers = []
    while line != '':
        x = int(line)
        if x < 25 or x > 75:
            bad_numbers.append(x)
        else:
            target_numbers.append(x)
        line = new_file.readline()
    new_file.close()
    print('Target List: ', target_numbers)
    print('Bad numbers: ', bad_numbers)

main()