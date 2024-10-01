def fact():
    a=int(input('enter a no:'))
    fact=1
    for i in range(1,a+1):
        fact*=i
    print(fact)
fact()    