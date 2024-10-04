import re
a='agnaey@gmail.com'
if re.search('^[a-z].*@gmail.com$',a):     ##''' ^ is used at starting letter    '''
                                            ##''' @ is used at end of the letter'''
    print('valid')
else:
    print('not valid')