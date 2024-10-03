                                   ## you can add multiple parent

class parent1:
    def house(self):
        print('house')
class parent2:
    def car(self):
        print('car')
class child(parent1,parent2):
    def bike(self):
        print('bike')

agnaey=child()
agnaey.car()
agnaey.house()




# class school:
#     def class_room(self):
#         print('class room')
#     def ground(self):
#         print('ground')
# class tution:
#     def book(self):
#         print('book')
#     def work(self):
#         print('work')
# class std(school,tution):
#     def uniform(self):
#         print('uniform')

# agnaey=std()
# agnaey.book()
# agnaey.class_room()
# agnaey.uniform()

# akshay=tution()
# akshay.book()

# ahana=school()
# ahana.ground()