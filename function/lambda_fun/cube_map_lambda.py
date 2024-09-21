'''                     cube in map'''
# l=[1,2,3,4,5,6,7,8]
# print(list(map(lambda x:x**3,l)))
'''
[1, 8, 27, 64, 125, 216, 343, 512]
'''


'''                    cube using user def in map'''
l=[1,2,3,4,5,6,7,8]
def fun(x):
    return x**3
print(list(map(fun,l)))

'''
[1, 8, 27, 64, 125, 216, 343, 512]
'''