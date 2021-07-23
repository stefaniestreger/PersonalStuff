def main():
    filename = 'grades.txt'
    try:
        high_grade(filename)
        count_records(filename)
     except IOError:
        print('Invalid file name: ', filename)

def count_records(filename):
    grade_file = open(filename, 'r')
    record_count = 0
    for line in grade_file:
        record_count += 1
    print('Number of records: ', record_count)

def high_grade(filename):
    try:
        grade_file = open(filename, 'r')
        record = grade_file.readline()
        highest_score = 0
        highest_score_name = 0
        while record != '':
            new_record = record.rstrip('\n')
            student_record = new_record.split(',')
            for x in student_record:
                pair = x.split(';')
                next_score_name = pair[0]
                next_score = int(pair[1])
                if next_score > highest_score:
                    highest_score_name = next_score_name
                    highest_score = next_score
                else:
                    break
            record = grade_file.readline()
        print('Highest Score: ', highest_score_name, ',', highest_score)
        grade_file.close()
    except ValueError:
        print('A number in the file is not a number')

main()
