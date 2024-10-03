# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
        
# class teacher(syn):
#     def attendance(self):
#         print('attendance')
#     def notes(self):
#         print('notes')
# class non_teacher(syn):
#     def enquire(self):
#         print('enquire')
#     def accounts(self):
#         print('account')
# class std(teacher):
#     def classes(self):
#         print('classes')
#     def studing(self):
#         print('studing')

# agnaey=std()
# agnaey.attendance()
# agnaey.python()
# agnaey.studing()

# -------------------------------------------------------

class grandparent():
    def land(self):
        print('land')

class brother(grandparent):
    def shop(self):
        print('shop')
    def money(self):
        print('money')
class bro_child1(brother):
    def bike(self):
        print('bike')
class bro_child2(brother):
    def cycle(self):
        print('cycle')

class sister(grandparent):
    def car(self):
        print('car')
class sis_child(sister):
    def dress(self):
        print('dress')
    
rahul=bro_child1()
rahul.land()
rahul.shop()
rahul.bike()

rohan=bro_child2()
rohan.land()
rohan.shop()
rohan.cycle()

ammu=sis_child()
ammu.land()
ammu.car()
ammu.dress()


