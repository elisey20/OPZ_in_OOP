from operations.binary_operation_behavior import BOB


class Division(BOB):
    def calc(self, first: float, second: float) -> float:
        return float(first) / second

    def get_symbol(self):
        return '/'

