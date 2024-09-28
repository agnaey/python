##                           grandparent to parent, parent to child


class grandparent:
    def house(self):
        print('parent')
class parent(grandparent):
    def busness(self):
        print('busness')
class child(parent):
    def bike(self):
        print('bike')

#g parnet
g=grandparent()
g.house()
#par
father=parent()
father.house()
father.busness()

agnaey=child()
agnaey.busness()
agnaey.bike()
agnaey.house()




# class cu:
#     def exam(self):
#         print('exam')
# class clg(cu):
#     def ground(self):
#         print('ground')
# class std(clg):
#     def uniform(self):
#         print('uniform')

# ##clg
# ihrd=clg()
# ihrd.exam()
# ihrd.ground()
# ##std
# agnaey=std()
# agnaey.exam()
# agnaey.ground()
# agnaey.uniform