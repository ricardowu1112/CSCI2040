def palindrome(n):
    while True:
        try:
            n = int(input("Please input a palindrome number: "))
        except:
            print("Your input is not a palindrome number!")
        else:
            a=str(n)
            if a[0]== '0':
                print("Your input is not a palindrome number!")
                break
            if a[:] == a[-1::-1]:
                print("{} is a palindrome number! Program ends.".format(n))
                break
            else:
                print("Your input is not a palindrome number!")
                continue
palindrome(1)
