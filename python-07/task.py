from python07.model import Option, OptionError
import sys


def main(command_line_arguments):

    if len(command_line_arguments) == 3:
        try:
            option = Option.get_option(command_line_arguments[1])
        except OptionError as error:
            print(error)
        else:
            option.analyse_file(command_line_arguments[2])

    else:
        print('Wrong number of command line arguments passed.')


if __name__ == '__main__':
    main(sys.argv)














    # if Option.option_main(sys.argv):
    #     try:
    #         option = Option.get_option(sys.argv[1])
    #     except OptionError as error:
    #         print(error)
    #     else:
    #         option.analyse_file(sys.argv[2])


























# IMPORTANT
# def file_generator():
#     with open('file_test.txt', 'r') as file_stream:
#         for num, line in enumerate(file_stream, 1):
#             rules_for_line = list()
#             for rule in Rule:
#                 if rule.value.matches(line.strip()):
#                     rules_for_line.append(rule.value.name())
#             yield '{}: {}'.format(num, ' '.join(rules_for_line))
#
#
# if __name__ == '__main__':
#     my_iterator = file_generator()
#     for item in my_iterator:
#         print(item)
