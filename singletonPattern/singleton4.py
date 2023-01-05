class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance

class MyClass():
    __metaclass__ = Singleton
    a = 1


if __name__ == "__main__":
    orig = MyClass()
    new = MyClass()
    
    print(MyClass.__dict__)

    #assert orig == new

    print("orig.a is", orig.a)
    print("new.a is", new.a)
    print("orig.a add 1.")
    orig.a += 1
    print("orig.a is", orig.a)
    print("new.a is", new.a)
    # TODO: 目前这个方法不奏效