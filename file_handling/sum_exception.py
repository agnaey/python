l=[1,4,10.5,'ok']
sum=0
for i in l:
        if type(i)==int or type(i)==float:    ## do it if it is int or float
            sum=sum+i
print(sum)