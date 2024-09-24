f=open('python/file_handling/create1.txt','r')
l=f.readlines()
f.seek(0)
for i in range(len(l)):
    a=f.readline().strip()
    print(a[::-1])