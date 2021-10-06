import operations


class OPZ:
    __vent = []
    __stack = []
    __flag_bracket = []

    def __go_to_stack(self, symbol):
        if symbol == '/':
            self.__stack.append('/')
        elif symbol == '*':
            while len(self.__stack) != 0 and self.__stack[-1] == '/':
                self.__vent.append(self.__stack.pop())
            self.__stack.append('*')
        else:
            while len(self.__stack) != 0 and (self.__stack[-1] == '/' or self.__stack[-1] == '*'):
                self.__vent.append(self.__stack.pop())
            self.__stack.append(symbol)

    def calculate(self, string):
        print("[INFO] Начался расчёт выражения с помощью ОПЗ...")

        flag = False
        for item in string:
            if item.isdigit():
                if flag:
                    self.__vent[-1] += item
                else:
                    self.__vent.append(item)
                    flag = True
            elif item == '/' or item == '*' or item == '-' or item == '+':
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

        print(self.__vent)
        for item in self.__vent:
            if item.isdigit():
                fstack.append(float(item))
            else:
                temp = fstack.pop()

                if item == '*':
                    fstack[-1] *= temp
                elif item == '+':
                    fstack[-1] += temp
                elif item == '-':
                    fstack[-1] -= temp
                elif item == '/':
                    fstack[-1] /= temp

        print("[INFO] Расчёт выражения с помощью ОПЗ окончен")
        return fstack[-1]
