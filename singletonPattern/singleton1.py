class Singleton():
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1


if __name__ == "__main__":
    orig = MyClass()
    new = MyClass()

    assert orig == new

    print("orig.a is", orig.a)
    print("new.a is", new.a)
    print("orig.a add 1.")
    orig.a += 1
    print("orig.a is", orig.a)
    print("new.a is", new.a)