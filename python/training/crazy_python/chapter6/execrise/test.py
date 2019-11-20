class Foo(object):
    def __init__(self):
        print 'foo'
    def __new__(cls, *args, **kwargs):
        return object.__new__(Stranger, *args, **kwargs)
 
class Stranger(object):
    def __init__(self,*args,**kwargs):
        print 'stranger'
        self.name='name'
    def display(self):
        print self.name
foo = Foo()
st = Stranger('aaaa',a='ccc')