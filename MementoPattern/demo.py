from originator import Originator
from caretaker import CareTaker


if __name__ == "__main__":
    o = Originator()
    ct = CareTaker()

    o.set_state("State #1")
    o.set_state("State #2")
    ct.add(o.save_state_to_memento())
    o.set_state("State #3")
    ct.add(o.save_state_to_memento())
    o.set_state("State #4")

    print("Current State:", o.get_state())
    o.get_state_from_memento(ct.get(0))
    print("First saved State:", o.get_state())
    o.get_state_from_memento(ct.get(1))
    print("Second saved State:", o.get_state())