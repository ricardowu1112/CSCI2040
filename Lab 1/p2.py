def shiftCipher(n):
    n = input('Please input a string: ')
    result = ""
    for i in range(len(n)):
        char = n[i]
        if char.isupper():
            result += chr((ord(char) - 64) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 96) % 26 + 97)
        else:
            result += char
    print('The encrypted string is: {}'.format(result))
shiftCipher(1)