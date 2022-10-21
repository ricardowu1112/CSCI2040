import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp
#import wexpect

ok = 0

child = exp.spawn('python3 p5.py')
child.delaybeforesend = 0.5

# test 1 
child.sendline('csci2040')
child.readline()
child.sendline('csci2040')
child.readline()
test1 = child.readline().rstrip()
if (test1 == 'Successfully set your password!' or test1.decode() == 'Successfully set your password!'):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

# test 2 
child = exp.spawn('python3 p5.py')
child.delaybeforesend = 0.5

child.sendline('123456')
child.readline()
test2 = child.readline().rstrip()
if (test2 == 'Invalid input.' or test2.decode() == 'Invalid input.'):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

child.sendline('abc123')
child.readline()
test2 = child.readline().rstrip()
if (test2 == 'Invalid input.' or test2.decode() == 'Invalid input.'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

child.sendline('python2040')
child.readline()
child.sendline('python2040')
child.readline()
test4 = child.readline().rstrip()
if (test4 == 'Successfully set your password!' or test4.decode() == 'Successfully set your password!'):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')

# test 5
child = exp.spawn('python3 p5.py')
child.delaybeforesend = 0.5

child.sendline('python')
child.readline()
test5 = child.readline().rstrip()
if (test5 == 'Invalid input.' or test5.decode() == 'Invalid input.'):
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')

child.sendline('csci2040')
child.readline()
child.sendline('csci1040')
child.readline()
test6 = child.readline().rstrip()
if (test6 == 'Those passwords did not match.' or test6.decode() == 'Those passwords did not match.'):
	print ('TEST 6 OK!')
	ok += 1
else:
	print ('TEST 6 FAIL.')

child.sendline('python2010')
child.readline()
test7 = child.readline().rstrip()
if (test7 == 'Those passwords did not match.' or test7.decode() == 'Those passwords did not match.'):
	print ('TEST 7 OK!')
	ok += 1
else:
	print ('TEST 7 FAIL.')

child.sendline('csci2040')
child.readline()
test8 = child.readline().rstrip()
if (test8 == 'Successfully set your password!' or test8.decode() == 'Successfully set your password!'):
	print ('TEST 8 OK!')
	ok += 1
else:
	print ('TEST 8 FAIL.')

# test 9
child = exp.spawn('python3 p5.py')
child.delaybeforesend = 0.5

child.sendline('csci2040')
child.readline()
child.sendline('csci204')
child.readline()
test9 = child.readline().rstrip()
if (test9 == 'Those passwords did not match.' or test9.decode() == 'Those passwords did not match.'):
	print ('TEST 9 OK!')
	ok += 1
else:
	print ('TEST 9 FAIL.')

child.sendline('csci1234')
child.readline()
test10 = child.readline().rstrip()
if (test10 == 'Those passwords did not match.' or test10.decode() == 'Those passwords did not match.'):
	print ('TEST 10 OK!')
	ok += 1
else:
	print ('TEST 10 FAIL.')

child.sendline('csci2440')
child.readline()
test11 = child.readline().rstrip()
if (test11 == 'Those passwords did not match. Please set your password next time. Program ends.' or test11.decode() == 'Those passwords did not match. Please set your password next time. Program ends.'):
	print ('TEST 11 OK!')
	ok += 1
else:
	print ('TEST 11 FAIL.')

if ok == 11:
	print ('You pass all the tests!')
else:
	print("Some tests fail.")
