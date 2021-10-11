from operations import Operations


class OPZ:
    __vent = []
    __stack = []
    __flag_bracket = []
    __operations = Operations()

    # получаем все символы операций, которые имеем, а также их приоритет
    __symbols = __operations.get_symbols()
    __symbols_priority = __operations.get_priority()

    def __go_to_stack(self, symbol):
        position = self.__symbols.index(symbol)
        priority = self.__symbols_priority[position]
        while len(self.__stack) != 0:
            if self.__symbols_priority[self.__symbols.index(self.__stack[-1])] > priority:
                self.__vent.append(self.__stack.pop())
            else:
                break
        self.__stack.append(symbol)

    # flag - вывод сообщений
    def calculate(self, string: str, messages=True) -> float:
        if messages:
            print("[INFO] Начался расчёт выражения с помощью ОПЗ...")

        flag = False
        for item in string:
            if item.isdigit():
                if flag:
                    self.__vent[-1] += item
                else:
                    self.__vent.append(item)
                    flag = True
            elif item in self.__symbols:
                self.__go_to_stack(item)
                flag = False
            elif item == '(':
                self.__flag_bracket.append(len(self.__stack))
                flag = False
            elif item == ')':
                while len(self.__stack) > self.__flag_bracket[-1]:
                    self.__vent.append(self.__stack.pop())
                self.__flag_bracket.pop()
                flag = False

        while len(self.__stack) != 0:
            self.__vent.append(self.__stack.pop())

        fstack = []
        operations = self.__operations.get_operations()

        for item in self.__vent:
            if item.isdigit():
                fstack.append(float(item))
            else:
                temp = fstack.pop()

                position = self.__symbols.index(item)
                fstack[-1] = operations[position].calc(fstack[-1], temp)

        if messages:
            print("[INFO] Расчёт выражения с помощью ОПЗ окончен")
        return round(fstack[-1], 4)
