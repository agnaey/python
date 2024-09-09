'''                   local var'''

# def fun1():
#     a=20 ##local
#     print('inside a=',a)
# fun1()
# #print('outside a=',a)    


'''                     global var'''


def fun1():
    print('inside b=',b)
b=30 #global
fun1()
print('outside b=',b)