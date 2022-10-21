import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp
#import wexpect

ok = 0

child = exp.spawn('python3 p2.py')
child.delaybeforesend = 0.5

# test 1 input is ABcd
child.sendline('ABcd')
child.readline()
test1 = child.readline().rstrip()
if (test1 == 'The encrypted string is: BCde' or test1.decode() == 'The encrypted string is: BCde'):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child = exp.spawn('python3 p2.py')
child.delaybeforesend = 0.5

# test 2 input is csci2040
child.sendline('csci2040')
child.readline()
test2 = child.readline().rstrip()
if (test2 == 'The encrypted string is: dtdj2040' or test2.decode() == 'The encrypted string is: dtdj2040'):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

child = exp.spawn('python3 p2.py')
child.delaybeforesend = 0.5

# test 3 input is I love python!
child.sendline('I love python!')
child.readline()
test3 = child.readline().rstrip()
if (test3 == 'The encrypted string is: J mpwf qzuipo!' or test3.decode() == 'The encrypted string is: J mpwf qzuipo!'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')


child = exp.spawn('python3 p2.py')
child.delaybeforesend = 0.5

# test 3 input is I love python!
child.sendline('#4 Shift Cipher')
child.readline()
test4 = child.readline().rstrip()
if (test4 == 'The encrypted string is: #4 Tijgu Djqifs' or test4.decode() == 'The encrypted string is: #4 Tijgu Djqifs'):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')

if ok == 4:
	print ('You pass all the tests!')
else:
	print("Some tests fail.")