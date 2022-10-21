import string
def check_sublist(list1,a,b,c):
    lista=[alist_min for alist_min in list1 if alist_min < min(a,b,c)]
    listb=[blist_min for blist_min in list1 if blist_min < (a+b-c)]
    listc=[clist_min for clist_min in list1 if clist_min < (a or b or c)]
    return lista, listb, listc
