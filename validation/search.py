import re
a='abcd'


# print(re.search('a',a))          ##          <re.Match object; span=(0, 1), match='a'>

# print(re.search('abc',a))          ##          <re.Match object; span=(0, 3), match='abc'>

# print(re.search('a.',a))             #'''       "." dot is used to print next letter with it   '''
                                        ###       <re.Match object; span=(0, 2), match='ab'>

# print(re.search('b.',a))              ###      <re.Match object; span=(0, 2), match='bc'>

# print(re.search('a.*',a))               ###      ".*"  dot star is used to print full characters
                                        ###      <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('b.*',a))               ##      <re.Match object; span=(1, 4), match='abcd'>

# print(re.search('a.+',a))              ###         <re.Match object; span=(0, 4), match='abcd'>
# print(re.search('d.+',a))                ##     (o/p-none) because + only take one or more characters         

# print(re.search('a.?',a))                  ## o/p-  ab
# print(re.search('d.?',a))                     ## (o/p-d)  ? takes zero or more  

# print(re.search('[abcd]',a))                 ##  o/p - a   [] checks if there is any letter is there

# print(re.search('[a-z]',a))                     ## to check a to z



##'''            using if statement'''

# if re.search('a',a):
#     print('match')
# else:print('no match')            ###              match


# if re.search('s',a):
#     print('match')
# else:print('no match')              ###             no match



a='ABCD'
# print(re.search('[A-z]',a))           ## o/p- A

a='987261'
# print(re.search('[0-9]',a))         ## o/p - 9

'''                           phone no check'''

# print(re.search('[6-9]',a))            ## o/p - 9

'''        no and letter mix'''
a='abcd12434'
# print(re.search('[a-z][0-9]',a))         ## d/1
# print(re.search('[a-z0-9]',a))          ##  a
# print(re.search('[a-z].[0-9]',a))        ##cd1
#print(re.search('[a-z].*[0-9]',a))          ##abcd12434
# print(re.search('[a-z].?[0-9]',a))         ##cd1
# print(re.search('[a-z].?[0-9].*',a))         ##cd12434
# print(re.search('[a-z].?[0-9].+',a))         ##cd12434
print(re.search('[a-z].?[0-9].?',a))         ##cd12


