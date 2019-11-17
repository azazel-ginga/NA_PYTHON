#coding=utf-8
'''
对象动态添加方法，但是所添加的方法只是对当前对象有效，如果希望为所有实例都添加方法，则可通过类添加方法来实现。
'''

class Cat(object):
    def __init__(self,name):
        self.name = name

def walk_func(self):
    print("%s 慢慢地走过一片草地" % self.name)

d1 = Cat('Garfield')
d2 = Cat('Kitty')

#d1.walk()   因为类中没有这个方法,所以这里调用时会报错

#为Cat动态添加walk方法，该方法的第一个参数会自动绑定
Cat.walk = walk_func            #1

d1.walk()
d2.walk()

'''
程序中1号代码为为Cat动态添加了walk方法，为类动态添加方法时，不需要使用MethodType进行包装，该函数的第一个参数会自动绑定。
'''