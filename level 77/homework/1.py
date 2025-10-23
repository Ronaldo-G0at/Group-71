def a(num):
    res=[]
    for i in num:
        if i % 2 == 0:
            res.append(i)
    return sum(res)
print(a([1,2,3,4,5,6]))

def omg(txt,letter):
    return txt.count(letter)

print(omg("hello","l"))

def omd(l1, l2):
    res = []
    for x in l1:
        if x in l2:
            res.append(x)
    return res
print(omd([1,2,3,4], [3,4,5,6])) 