#                      index of duplicate no

l=[1,2,3,44,1,2,5,1]
no=int(input("enter a no : "))
c=l.count(no)
pos=0
while c>0:
    p=l.index(no,pos)
    print(p)
    pos=p+1
    c-=1