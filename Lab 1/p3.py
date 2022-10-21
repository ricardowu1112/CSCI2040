def printString(num, string):
    happy = True
    while happy:
        num = int(input("Enter an integer: "))
        if num <= 0:
            happy = False
            print('Program ends.')
            break
        string = str(input("Enter a string: "))

        # string = "^_^"
        for i in range(1, num + 1):
            print(' ' * (num * len(string) - i * len(string)) + i * string)


printString(1, '^_^')
