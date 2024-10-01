f=open('python/demo/16Q/exam.txt','r')
l=len(f.readlines())
f.seek(0)
word=' '
for i in range(l):
        a=f.readline().strip()
        s=a.split(' ')
        for j in s:
                if j!='':
                    if len(word)<len(j):
                           word=j
print('longest word is : ',word)