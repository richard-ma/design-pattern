from iterator import Iterator
from container import Container


class NameRepository(Container):
    NAMES = [
            "Robert",
            "John",
            "Julie",
            "Lora"
        ]

    class NameIterator(Iterator):
        INDEX = 0 
        
        def has_next(self):
            if NameRepository.NameIterator.INDEX < len(NameRepository.NAMES):
                return True
            else:
                return False

        def next(self):
            if self.has_next():
                ret = NameRepository.NAMES[NameRepository.NameIterator.INDEX]
                NameRepository.NameIterator.INDEX += 1
                return ret

            return None

    def get_iterator(self):
        return NameRepository.NameIterator()


if __name__ == "__main__":
    nr = NameRepository()

    iter = nr.get_iterator()
    while iter.has_next():
        print("Name:", iter.next())