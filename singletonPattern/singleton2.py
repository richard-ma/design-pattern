class Signleton():
    _state = dict()
    def __new__(cls, *args, **kw):
        ob = super(Signleton, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state

        return ob

class MyClass(Signleton):
    a = 1


if __name__ == "__main__":
    orig = MyClass()
    new = MyClass()

    #assert orig == new #这是两个实例，所以id是不同的，只是共享了属性的字典_state

    print("orig.a is", orig.a)
    print("new.a is", new.a)
    print("orig.a add 1.")
    orig.a += 1
    print("orig.a is", orig.a)
    print("new.a is", new.a)