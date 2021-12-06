def accum(s):
    res =""
    count=0
    for i in s:
        if count==0:
            res+=i.upper()
        else:
            res+="-"
            res+=i.upper()
            res+=i.lower()*count
        count+=1
    # print(res)
    return res
