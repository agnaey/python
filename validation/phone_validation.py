import re
a='8943819343'
if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit:
    print('valid')
else:
    print('not valid')

                                    ##"      valid      "   

