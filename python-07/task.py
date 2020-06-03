# from python07.model import Filter, EndsWithDot, LessOneHundredChars, AtLeastFiveALetters, MoreThreeZLetters, EmptyLine, ConsistsNonLetterChars, Rule, Option
from python07.model import Option
import sys


if __name__ == '__main__':
    option = Option.get_option(sys.argv[1])
    option.filter_file(sys.argv[2])
























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
