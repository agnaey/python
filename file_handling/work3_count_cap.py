##           find cap small letter and word

f=open('python/file_handling/create1.txt','r')
l=f.readlines()
f.seek(0)
letter=0
cap=0
word=0
for i in range(len(l)):
    a=f.readline().strip()
    s=a.split(' ')
    for i in s:
        if i!='':
            word+=1
    for i in a:
        if i !=' ':
            if i.isupper():
                cap+=1
            letter+=1

print(letter)
print('cap',cap)
print('small',letter-cap)
print('words',word)
print('no of line',len(l))
