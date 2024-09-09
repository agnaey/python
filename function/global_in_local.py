'''                 conerting local var to global var'''


def fun1():
    global a
    a=10
fun1()
print('a=',a)