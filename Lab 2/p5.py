from collections import Counter
import re
def count_alphabet(test_string):
    x=re.sub("[^a-zA-Z]","",test_string)
    count = Counter(x)
    return sum(count.values())

def hksar_capitalization(test_string):
    test_string=test_string.replace('h','H').replace('k','K').replace('s','S').replace('a','A').replace('r','R')
    return test_string

def concat(test_string, new_string):
    return test_string+new_string

def search(test_string, sub):
    reverse_test = sub[::-1]
    for x in range(len(test_string)-1,-1,-1):
        if test_string[x:x-len(reverse_test):-1] == reverse_test:
            return x-len(reverse_test)+1
    return -1