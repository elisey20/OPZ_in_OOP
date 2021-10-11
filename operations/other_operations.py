# Для добавления новых операций
# В каждом классе операции должны быть
# два метода calc и get_symbol
# calc(float, float) -> float - задает логику операции
# get_symbol() -> str - задает единственный и уникальный символ операции

from operations.binary_operation_behavior import BOB


class Row(BOB):
    def calc(self, first: float, second: float) -> float:
        return first ** second

    def get_symbol(self) -> str:
        return 'm'
