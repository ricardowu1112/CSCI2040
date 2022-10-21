import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp
#import wexpect

ok = 0

child = exp.spawn('python3 p1.py')

child.delaybeforesend = 0.5

# test 1 input is 210
child.sendline('210')
child.readline()
test1 = child.readline().rstrip()
if (test1 == 'Your input is not a palindrome number!' or test1.decode() == 'Your input is not a palindrome number!'):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

# test 2 input is 0210
child.sendline('01210')
child.readline()
test2 = child.readline().rstrip()
if (test2 == 'Your input is not a palindrome number!' or test2.decode() == 'Your input is not a palindrome number!'):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

# # test 3 input is -11
child.sendline('-11')
child.readline()
test3 = child.readline().rstrip()
if (test3 == 'Your input is not a palindrome number!' or test3.decode() == 'Your input is not a palindrome number!'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')


# # test 4 input is Nba A B n
child.sendline('Nba A B n')
child.readline()
test4 = child.readline().rstrip()
if (test4 == 'Your input is not a palindrome number!' or test4.decode() == 'Your input is not a palindrome number!'):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')

child.sendline('2112')
child.readline()
test5 = child.readline().rstrip()
if (test5 == '2112 is a palindrome number! Program ends.' or test5.decode() == '2112 is a palindrome number! Program ends.'):
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')

if ok == 5:
	print ('You pass all the tests!')
else:
	print("Some tests fail.")
