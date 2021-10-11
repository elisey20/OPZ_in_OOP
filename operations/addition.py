from operations.binary_operation_behavior import BOB


class Addition(BOB):
    def calc(self, first: float, second: float) -> float:
        return first + second

    def get_symbol(self):
        return '+'

