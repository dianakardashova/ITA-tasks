import sys
def pairs_of_numbers(params: list) -> list:
    '''Function returns pairs of numbers that form the amount entered by the user.'''
    length = len(params)
    result = list()
    sum = int(input('Enter the sum of the pairs: '))
    i = 0
    while i < length:
        for j in range(i+1, length):
            if params[i] + params[j] == sum:
                result.append('{} + {}'.format(params[i], params[j]))
        i += 1
    return result

def command_line_arguments(*args: list) -> list:
    '''Function returns command line arguments'''
    while True:
        try:
            params = [int(item) for item in args]
            return params
        except ValueError:
            print('Oops!\nIntegers expected. \nTry it again!')
            sys.exit()
        except Exception:
            print('Oops!\nSomething went wrong. \nTry it again!')
            sys.exit()

def main():
    print(pairs_of_numbers(command_line_arguments(*sys.argv[1:])))

if __name__ == '__main__':
    main()


