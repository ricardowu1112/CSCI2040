import os
if (os.name == 'posix'):
    import pexpect as exp
else:
    import wexpect as exp
#import wexpect

ok = 0

child = exp.spawn('python3 p4.py')
child.delaybeforesend = 0.5

child.sendline('3.7 3')
child.readline()
test1 = child.readline()
current_gpa = float(test1.split()[2])
if current_gpa == 3.7:
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('3.3 2')
child.readline()
test2 = child.readline()
current_gpa = float(test2.split()[2])
if current_gpa == 3.54:
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

child.sendline('-2.5 2')
child.readline()
test3 = child.readline().rstrip()
if(test3 == 'Wrong input!' or test3.decode() == 'Wrong input!'):
    print ('TEST 3 OK!')
    ok += 1
else:
    print ('TEST 3 FAIL.')

child.sendline('5.1 4')
child.readline()
test4 = child.readline().rstrip()
if(test4 == 'Wrong input!' or test4.decode() == 'Wrong input!'):
    print ('TEST 4 OK!')
    ok += 1
else:
    print ('TEST 4 FAIL.')

child.sendline('3.3 0')
child.readline()
test5 = child.readline()
current_gpa = float(test5.split()[2])
if current_gpa == 3.54:
	print ('TEST 5 OK!')
	ok += 1
else:
	print ('TEST 5 FAIL.')
	

child.sendline('exit')
child.readline()
test6 = child.readline().rstrip()
if (test6 == 'Program ends.' or test6.decode() == 'Program ends.'):
	print ('TEST 6 OK!')
	ok += 1
else:
	print ('TEST 6 FAIL.')

if ok == 6:
	print ('You pass all the tests!')
else:
	print("Some tests fail.")
