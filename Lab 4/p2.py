a=range(1,12)
list1=list(map(lambda x:x**2,a))
list2=list(map(lambda x:x+2,a))
list3=[x for x in a if x <=8]
list4=[x**2 for x in a if x %2==0]