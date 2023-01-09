from binaryobserver import BinaryObserver
from octalobserver import OctalObserver
from hexaobserver import HexaObserver
from subject import Subject


if __name__ == "__main__":
    subject = Subject()

    HexaObserver(subject)
    OctalObserver(subject)
    BinaryObserver(subject)

    print("First state change: 15")
    subject.set_state(15)
    print("Second state change: 10")
    subject.set_state(10)
    print("Third state change: 30")
    subject.set_state(30)