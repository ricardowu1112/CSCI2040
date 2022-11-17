def non_unique(list):
    from collections import Counter
    result=Counter(list)
    a={key:val for key,val in result.items() if val !=1}
    result1,result2 =[key for key in a.keys()],[val for val in a.values()]
    return [result1,result2] # `result' is a list.