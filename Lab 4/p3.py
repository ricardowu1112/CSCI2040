from functools import reduce
def recount(a,b):
    if type(a) == str:
        acount=a.count(string)
    else:
        acount=a
    if type(b) == str:
        bcount=b.count(string)
    else:
        bcount=b
    return bcount+acount

def word_count(x,str,n):
    global string
    string= str
    filtered = list(filter(lambda q: len(q)>n, x))
    concated = reduce(recount,filtered)
    return concated
