
class first:
    def __init__(self) -> None:
        print('first')

class second:
    def __init__(self) -> None:
        print('second')

class third():
    def __init__(self) -> None:
        super(first).__init__()
        print("third")


obj = third()