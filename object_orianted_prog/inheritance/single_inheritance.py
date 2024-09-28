                      ### '''parent and child class'''


# class parent:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
# class child(parent):
#     def bike(self):
#         print('bike')
# ##child
# agnaey=child()                 ###child can access parents things but parents cant
# agnaey.car
# agnaey.shop
# agnaey.bike

# ##parent                         ### parents can access only there thing not child
# parent.car
# parent.shop


###'''                          syf'''

class syn:
    def python(self):
        print('python')
    def php(self):
        print('php')
class novavi(syn):
    def dm(self):
        print('dem for work')
    def web_dev(self):
        print('web dev')

# #emp
amal=novavi()
amal.dm()                          ##emp can learn and work in syn and novavi but std cant
amal.php()
amal.python()

##std
agnaey=syn()
agnaey.php()                       ##std can only std in syn
agnaey.python()