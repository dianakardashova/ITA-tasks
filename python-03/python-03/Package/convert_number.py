"""This script converts number into word."""
from num2words import num2words

def number_entered_by_user_to_word() -> str:
    """
    Ask the user for a number and convert to word.

    :return Text representation of a number.
    """
    number = input('What number would you like to convert?\nType it out: ')
    while True:
        try:
            float(number)
            return "Text representation of a number: {}".format(num2words(number))
        except ValueError:
            print('Oops! It must be a number. Try it again.')
            number = input('What number would you like to convert?\nType it out: ')

def main() -> None:
    """Program entry point."""
    print(number_entered_by_user_to_word())

if __name__ == '__main__':
    main()
