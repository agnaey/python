s={1,2,3,4,6,7}
s1={1,2,3,4,5}
# s.add(10)
'''{10, 1, 2, 3}'''

# s.difference({10,1,2,5,6})
# s.discard(3)
# s.clear()
# s.remove(1)
# s.pop()
# s.update({10,12,13})
# print(s.intersection(s1))
# print(s.union(s1))
# print(s.isdisjoint(s1))
# print(s.issubset(s1))
'''false'''
# print(s.issuperset(s1))
'''false'''
print(s1.difference(s))
'''{6,7}'''
# s.difference_update(s1)
'''{6,7}'''
# s.intersection_update(s1)
'''{1,2,3}'''
# s.symmetric_difference_update(s1)
'''{4,5,6,7}'''
# s.symmetric_difference(s1)
'''{1, 2, 3, 6, 7}'''
# print(s)