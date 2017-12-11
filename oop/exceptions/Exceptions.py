try:
    f = open('testfile2133', 'r')
    f.write("test write this")
except:
    print('There was a type error!')
finally:
    print('Always execute finally code blocks')


def askint():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Looks lke you di not enter an integer!')
            continue
        else:
            print('Correct that is an integer!')
            break
        finally:
            print('Finally block executed')
        print(val)



askint()
