
print('welcome')
a='hi'
b='21'
try:                                      ##'''   try is used when the prog may have error'''          
    print(a+b)
except:                                  ##''' if 'try' didnt work 'except' would work'''
    print('error')
else:                                    ##''' else is used to work if the code is correct only'''
    print('correct')
finally:                                 ##'''   finally is used to work even if the prog is correct or wrong'''
    print('prog ends')
