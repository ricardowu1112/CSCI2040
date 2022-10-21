def recursive_pow(x, n):
    if n == 0:
        return 1
    else:
        if n%2 == 0:
            return recursive_pow(x*x,n/2)
        else:
            return x * recursive_pow(x,n-1)