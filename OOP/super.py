# class school:
#     def notes(self):
#         print('notes')
# class std(school):
#     def notes(self):
#         print('notes in std')
#         super().notes()


# amal=std()
# amal.notes()


'''
notes in std
notes
'''

# class school:
#     def notes(self):
#         print('notes')
# class std(school):
#     def notes(self):
#         super().notes()
#         print('notes in std')


# amal=std()
# amal.notes()

'''
notes
notes in std
'''

# --------------------------------------------------------

# class school:
#     def notes(self,sub):
#         print('notes',sub)
# class std(school):
#     def notes(self):
#         print('notes in std')
#         super().notes('py')

# amal=std()
# amal.notes()

'''
notes in std
notes py
'''

# -----------------------------------------------

class school:
    def notes(self,sub):
        print('notes',sub)
class std(school):
    def notes(self,sub):
        print('notes in std')
        super().notes(sub)

amal=std()
amal.notes('py')