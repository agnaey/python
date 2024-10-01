# d={1:'one',2:'two',3:'three'}
# def num(d):
#     return{value:key for key,value in d.items()}
# print(num(d))

d={1:'one',2:'two',3:'three'}
def num(d):
    d1={}
    for i in d:
        d1[d[i]]=i
    return d1
print(num(d))
