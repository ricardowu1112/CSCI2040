import os

if os.path.isfile('p3.py'):
    try:
        from p3 import word_count
        print('Successfully load p3.py')
        test_case = [
            (['python is boring',
            'pythom is a large heavy-bodied snake',
            'The python course is worse taking',
            'The python course is worth taking'], 'python', 20),
            (['python is boring',
              'pythom is a large heavy-bodied snake',
              'The python course is worse taking',
              'The python course is worth taking'], 'python', 10),
            (['aba', 'bca', 'baba', 'ab'], 'ab', 2)
                     ]
        expected = [2, 3, 2]
        try:
            print('Testing...')
            answer = [word_count(x, str, n) for (x, str, n) in test_case]
            print(answer)
            print(expected)
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing word_count, please check your code')
    except:
        print('Cannot load word_count, please check the function name or syntax')
else:
    print("Cannot find p3.py, please put p3.py and this test script in the same folder.")
