##        it is to count hoe many letters are there

f=open('python/file_handling/create1.txt','r')
l=f.readlines()
f.seek(0)
letter=0
for i in range(len(l)):
    a=f.readline().strip()
    for i in a:
        if i !=' ':
            letter+=1
print(letter)
