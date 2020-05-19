import sys

def file_statistic():
    choice = "y"
    while choice.lower() == "y" or choice.lower() == "yes":
        path_to_a_file = input('Enter file name: ')
        while True:
            try:
                my_file = open(path_to_a_file, mode='r', encoding='latin_1')
                break
            except Exception:
                print(sys.exc_info()[1])
                path_to_a_file = input('Enter correct file name: ')
        letter_count = 0
        line_count = 0
        empty_line_count = 0
        lines_with_letter_count = 0
        lines_with_word_count = 0
        for num, line in enumerate(my_file,1):
            if 'z' in line:
                lines_with_letter_count += 1
                for word in line:
                    if word == 'z':
                        letter_count += 1
            line_count += 1
            if 'and' in line: lines_with_word_count += 1
            if not line.strip(): empty_line_count += 1
        print('total lines: {}'.format(line_count))
        print('empty lines: {}'.format(empty_line_count))
        print('lines with "z": {}'.format(lines_with_letter_count))
        print('"z" count: {}'.format(letter_count))
        print('lines with "and": {}'.format(lines_with_word_count))
        my_file.close()
        choice = input('Do you want to analyze another file? [Y/N]: ')

def main():
    file_statistic()

if __name__=='__main__':
    main()





















'''
import  sys
input_file = 'list_of_password.txt'
output_file = 'my_passwords.txt'

password_to_look_for = '123'

my_file1 = open(input_file, mode='r', encoding='latin_1')
my_file2 = open(output_file, mode='a', encoding='latin_1')

#print(my_file.read())
for num, line in enumerate(my_file1, 1):
    if password_to_look_for in line:
        print('Line №{} : {}'.format(num, line.strip()))
        my_file2.write("Found password: {}".format(line))
my_file1.close()
my_file2.close()


input_file = 'list_of_passwords.txt'
while True:
    try:
        print('Inside TRY')
        my_file = open(input_file, mode='r', encoding='latin_1')
    except Exception:
        print('Inside EXCEPT')
        print('Error Found')
        print(sys.exc_info()[1])
        input_file = input('Enter correct file name: ')
    else:
        print('Inside ELSE')
        print(my_file.read())
        sys.exit()
    finally:
        my_file.close()

print('------------EOF-------------')'''
