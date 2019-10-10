import turpleTest
class TestCase:
    def __init__(self,name,space):
        self.name = name
        self.space = space

    def __str__(self):
        return '%s,%s' % (self.name,self.space)

    def __abs__(self):
        pass
        return 'YOU'

R = TestCase('firstClass','M')
print(R)

