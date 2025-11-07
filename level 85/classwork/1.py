def xo(s):
    s=s.lower()
    
    x1=0
    o1=0
    for i in s:
        if i == "x":
            x1+=1
        elif i == "o":
            o1+=1
    if x1==o1:
        return True
    return False