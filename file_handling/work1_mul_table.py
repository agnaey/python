f=open('python/file_handling/create1.txt','w')
mul=int(input('enter a no:'))
for i in range(1,11):
    for j in range(1,mul+1):
        f.write(str(j)+'*'+str(i)+'='+str(j*i)+'\t')
    f.write('\n')

