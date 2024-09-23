import numbers
import add as c
from sub import *
import mul
import div as d
from mod import *
while True:
    print(
        '''
1.add
2.sub
3.mul
4.div
5.mod
6.exit
'''
    )
    ch=int(input('enter your choise:'))
    if ch==1:
        a,b=numbers.num()
        c.add(a,b)
    elif ch==2:
        a,b=numbers.num()
        subs(a,b)
    elif ch==3:
        a,b=numbers.num()
        mul.mul(a,b)
    elif ch==4:
        a,b=numbers.num()
        d.div(a,b)
    elif ch==5:
        a,b= numbers.num()
        mod(a,b)
    else:break


