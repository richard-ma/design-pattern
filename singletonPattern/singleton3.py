def signleton(cls, *args, **kw):
    instances = dict()
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance


@signleton
class MyClass():
    a = 1


if __name__ == "__main__":
    orig = MyClass()
    new = MyClass()

    assert orig == new # 返回字典的同一个项，所以是同一个实例

    print("orig.a is", orig.a)
    print("new.a is", new.a)
    print("orig.a add 1.")
    orig.a += 1
    print("orig.a is", orig.a)
    print("new.a is", new.a)