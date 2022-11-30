import os

if os.path.isfile('p2.py'):
    try:
        import p2
        print('Successfully load p2.py')
        expected1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
        expected2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expected3 = [1, 2, 3, 4, 5, 6, 7, 8]
        expected4 = [4, 16, 36, 64, 100]
        try:
            print('Testing...')
            if expected1 == p2.list1 and expected2 == p2.list2 and expected3 == p2.list3 and expected4 == p2.list4 :            
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing p2, please check your code')
    except:
        print('Cannot load p2, please check the file')
else:
    print("Cannot find p2.py, please put p1.py and this test script in the same folder.")
