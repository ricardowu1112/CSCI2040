c=[0,0]
while True:
    a = input('')
    b = a.split(' ')
    if a == 'exit':
        print("Program ends.")
        break
    for index in range(len(b)):
        b[index]= float(b[index])
    if b[0] > 5.0 or b[1] < 0 or b[0]<0:
        print('Wrong input!')
        continue
    else:
        c[0]= (c[0]*c[1]+b[0]*b[1])/(c[1]+b[1])
        c[1]=c[1]+b[1]
        print('Current GPA: {0:.2f}'.format(c[0]))