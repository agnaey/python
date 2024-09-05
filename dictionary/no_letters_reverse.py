num=int(input('enter a no:'))
no={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
s=' '
for i in range(num):
    if num<=0:
        break
    x=num%10
    s=no[x]+' '+s
    num=num//10
print(s)