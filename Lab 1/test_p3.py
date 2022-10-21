import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp
#import wexpect

ok = 0

child = exp.spawn('python3 p3.py')
child.delaybeforesend = 0.5

child.sendline('4')
child.readline()

child.sendline('1')
child.readline()

flag = True
for i in range(1, 5):
	line = child.readline().rstrip()
	if not (line == (4-i)*' '+'1'*i or line.decode() == (4-i)*' '+'1'*i):
		flag = False
if (flag == True):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')


child.sendline('2')
child.readline()

child.sendline('^_^')
child.readline()

flag = True
for i in [1,2]:
	line = child.readline().rstrip()
	if not (line == (2-i)*'   '+'^_^'*i or line.decode() == (2-i)*'   '+'^_^'*i):
		flag = False
if (flag == True):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')


child.sendline('-1')
child.readline()
test3 = child.readline().rstrip()
if (test3 == 'Program ends.' or test3.decode() == 'Program ends.'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

child = exp.spawn('python3 p3.py')
child.delaybeforesend = 0.5

child.sendline('0')
child.readline()
test4 = child.readline().rstrip()
if (test4 == 'Program ends.' or test4.decode() == 'Program ends.'):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')


if ok == 4:
	print ('You pass all the tests!')
else:
	print("Some tests fail.")
