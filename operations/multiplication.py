from operations.binary_operation_behavior import BOB


class Multiplication(BOB):
    def calc(self, first: float, second: float):
        return first * second

    def get_symbol(self):
        return '*'
