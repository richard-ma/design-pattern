from packing import Packing


class Wrapper(Packing):
    def pack(self):
        return "Wrapper"


if __name__ == "__main__":
    wrapper = Wrapper()
    print(wrapper.pack())