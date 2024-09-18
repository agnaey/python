'''                               position argument    '''

# def detls(name,age):
#     print('name=',name)
#     print('age=',age)
# detls('agnaey',21)
# detls('ahana',20)

# detls(20,'gokul')  ##              this type of detls is wrong bec the output will be in opposite ways

'''
name= agnaey
age= 21
name= ahana
age= 20
name= 20
 age= gokul            #this is wrong
'''

'''                             function with keyword argument     '''

# def dtls(name,age):
#     print('name=',name)
#     print('age=',age)

# dtls(age=20,name='agnaey')   ###         o/p will come in name and age bec WE PRINT IT LIKE THAT if print change to age first o/p will be age
'''
name= agnaey
age= 20
'''

'''                       with default values'''

# def sample(name='abc',age=20):
#     print(name,age)
# sample()
# sample('agnaey')
# sample(age=25)
# sample('tutu',30)

'''
abc 20
agnaey 20
abc 25
tutu 30
'''


'''                            arbitrary arguments'''
# def sample(*a):
#     print(a)
# sample()
# sample(1,2,3)
# sample(1,2,3,4)
'''
()
(1, 2, 3)
(1, 2, 3, 4)
'''

'''---------------------------------------'''
# def sample(b,*a):
#     print(b,a)
# sample(1)
# sample(1,2,3,4)
'''
1 ()
1 (2, 3, 4)
'''

'''                            arbitrary keyword arguments'''
# def sample(**a):
#     print(a)
# sample(name='agnaey',age=20)
'''
{'name': 'agnaey', 'age': 20}
'''
