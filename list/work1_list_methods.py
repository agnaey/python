#                                              list methods


# append

# l=[]
# l.append(10)
# l.append(5)
# l.append(20)
# l.append("abc")
# l.append([1,2,3])
# print(l)

'''
[10, 5, 20, 'abc', [1, 2, 3]]
'''

# extend

# l=[10, 5, 20, 'abc', [1, 2, 3]]
# l.extend([8,9,4])
# print(l)

'''
[10, 5, 20, 'abc', [1, 2, 3], 8, 9, 4]
'''

# insert

l=[10, 5, 20, 'abc', [1, 2, 3], 8, 9, 4]
l.insert(0,"hi")
print(l)

'''
['hi', 10, 5, 20, 'abc', [1, 2, 3], 8, 9, 4]
'''
