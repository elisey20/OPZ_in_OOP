# OPZ_in_OOP

## Использование:

Класс OPZ использует несколько файлов с классами: `addition.py`, `division.py`, `multiplication.py`, `subtraction.py`, `other_operations.py`. Чтобы добавить новую операцию в программу нужно добвить новый уникальный класс в файл `other_operations.py` и создать объект класса в списке `__operations`, который находится в файле `operations_class.py`, а также задать приоритет операции относительно других. 

```python
""" Здесь подключить новую операцию путем добавления нового объекта в список,
    а также задать ему приоритет относительно других операций(более большой
    приоритет задается более большим значением).
    По умолчанию / = 3, * = 2, + = - = 1 """
__operations = [[Division(), 3], [Multiplication(), 2],
                [Addition(), 1], [Subtraction(), 1],
                [Row(), 4]]
```

В новом классе обязательно должны быть два метода calc и get_symbol.
- `calc(float, float) -> float` - задает логику операции
- `get_symbol() -> str` - задает единственный и уникальный символ операции

Добавления нового класса операции на примере степенной функции:
```python
class Row(BOB):
    def calc(self, first: float, second: float) -> float:
        return first ** second

    def get_symbol(self) -> str:
        return 'm'
```

## Ограничения:

1. Реализация позволяет добавлять только бинарные операции;
2. В программе нет проверок на ошибки, поэтому ответственность при создании новой операции и записи выражения полностью ложиться на пользователя;
3. Нельзя переопределять цифры;
4. Допустимо создание операции только с односимвольной записью;
5. Запрещено использовать вещественные числа при записи выражения;
6. Допустимо использовать только макет класса операции описанный выше.
