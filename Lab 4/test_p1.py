import os

if os.path.isfile('p1.py'):
    try:
        from p1 import RPNCalculator
        print('Successfully load p1.py')
        calc = RPNCalculator()
        try:
            print('Testing...')
            answer = calc.eval("3 4 + 2 * 3 %")
            expected = 2
            print(answer)
            print(expected)
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing RPNCalculator, please check your code')
    except:
        print('Cannot load RPNCalculator, please check the function name or syntax')
else:
    print("Cannot find p1.py, please put p1.py and this test script in the same folder.")
