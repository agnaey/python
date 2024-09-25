'''                                           read'''
# f=open('python/file_handling/create1.txt','r')
# a=f.read(3)  ##'''   we can only print the position no we added on read'(3)'      '''
# f.seek(0)    ##''' to start from any posi we want'''
# b=f.read()
# print(f.tell())  ##'''   to tell how many pos there is'''
# print(a)
# print(b)


'''                                           readline'''
f=open('python/file_handling/create1.txt','r')
a=f.readline()           
b=f.readline()       ##'''                   it will read only one line'''
c=f.readline()
print(a)
print(b)
print(c)
f.seek(0)
l=f.readline()
print(l)


'''                                           write'''
'''                                           w-mode'''
# f=open('python/file_handling/create1.txt','w')        ##''' (w) will overwrite everything and write its message'''
# f.write('good bye')
'''                                            a-mode'''
# f=open('python/file_handling/create1.txt','a')   ##'''(a) it will write below the content that is already present there'''
# f.write('\nok')                       ##''' (\n) is used to write on a new line or elese it will be writing in a old line'''