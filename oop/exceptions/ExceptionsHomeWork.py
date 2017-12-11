import sys

# First task - handle  TypeError exception
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Handled exception')

# Second task - devided by zero

try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError as detail:
    print(sys.exc_info()[0])
    print('Handling run-time error:', detail)
finally:
    print('All done the the end')


# Third task - write asks for an integer and prints the square of it
# Use while loop with a try except else block to account for incorrect inputs

def ask():
    while True:
        try:
            val = int(input('Please, enter an integer : '))
        except:
            print('Please try again')
            continue
        else:
            break
    print('Thank you, your number squared is : ' + str(val ** 2))


ask()
