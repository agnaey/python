'''                      even no'''
l=[1,2,3,4,5,6,7,8]
# data=filter(lambda x:x%2==0,l)
# print(list,data)

print(list(filter(lambda x:x%2==0,l)))

'''                print A letter word'''
# l=['apple','orange','kiwi']
# print(list(filter(lambda x:'a' in x,l)))

'''              user def  print A letter word '''
# l=['apple','orange','kiwi']
# def fun(x):
#     return 'a' in x
# print (list(filter(fun,l)))

# '''              user def fun  even no'''
# l=[1,2,3,4,5,6,7,8]
# def fun(x):
#     return 



'''                            odd no '''

l=[1,2,3,4,5,6,7,8]
print(list(filter(lambda x:x%2==1,l)))
