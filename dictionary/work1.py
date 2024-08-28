d={}
limit=int(input('enter limit'))
for i in range(limit):
    key=str(input("input enter the key : "))
    value=str(input('input enter the value :'))
    d.update({key:value})
print(d)
