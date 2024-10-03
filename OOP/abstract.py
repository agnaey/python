from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print('python')
    def php(self):
        print('php')
class staff(syn):
    def reg(self):
        print('staff reg')
    def notes(self):
        print('notes')
class std(syn):
    def reg(self):
        print('std reg')
    def exam(self):
        print('exam')

amal=std()
amal.reg()