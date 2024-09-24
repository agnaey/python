f=open('python/file_handling/create1.txt','w')
mul=int(input('enter a no:'))

for i in range(1,11):

    f.write(str(i)+'*'+str(mul)+'='+str(i*mul)+'\n')

    ##''' the output will be on create1.txt file'''