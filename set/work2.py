php=set()
lmt=int(input('enter php the limit: '))
for i in range(lmt):
    std=input('enter the student: ')
    php.add(std)
print(f'php:{php}')

python=set()
lmt=int(input('enter python the limit: '))
for i in range(lmt):
    std=input('enter the student: ')
    python.add(std)
print(f'python:{python}')

java=set()
lmt=int(input('enter java the limit: '))
for i in range(lmt):
    std=input('enter the student: ')
    java.add(std)
print(f'java:{java}')

lmt=(php.intersection(python))
lmt.intersection(java)
print(f'common:{lmt}')

lmt=(python.difference(php))
lmt.difference(java)
print(f'in python unique:{lmt}')




    



