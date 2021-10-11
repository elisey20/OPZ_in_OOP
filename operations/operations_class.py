from operations.multiplication import Multiplication
from operations.division import Division
from operations.addition import Addition
from operations.subtraction import Subtraction


class Operations:
    """ Здесь подключить новую операцию путем добавления нового объекта в список,
        а также задать ему приоритет относительно других операций(более большой
        приоритет задается более большим значением).
        По умолчанию / = 3, * = 2, + = - = 1 """
    __operations = [[Division(), 3], [Multiplication(), 2],
                    [Addition(), 1], [Subtraction(), 1]]

    def get_priority(self):
        result = []
        for item in self.__operations:
            result.append(item[1])
        return result

    def get_symbols(self) -> list:
        result = []
        for item in self.__operations:
            result.append(item[0].get_symbol())
        return result

    def get_operations(self) -> list:
        result = []
        for item in self.__operations:
            result.append(item[0])
        return result
