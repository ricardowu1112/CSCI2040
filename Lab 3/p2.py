import random
def quicksort(a):
    if len(a)<=1:
        return a
    left=[]
    right=[]
    pivot1=[]
    pivot=random.choice(a)
    for num in a:
        if num > pivot:
            left.append(num)
        elif num < pivot:
            right.append(num)
        elif num==pivot:
            pivot1.append(num)
    return quicksort(left) + pivot1 + quicksort(right)