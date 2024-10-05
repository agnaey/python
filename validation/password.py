import re
pas='agnaey12'
if len(pas)>=8 and re.search('[A-z0-9].*[!@#$%&0-9]',pas) and not(pas.isdigit()):
    print('valid')
else:
    print('invalid')