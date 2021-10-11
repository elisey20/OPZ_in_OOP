import unittest
from opz import OPZ


class OPZTestCase(unittest.TestCase):
    __opz = OPZ()

    def testing(self) -> None:
        self.assertEqual(self.__opz.calculate("1+2", messages=False), 3.0)
        self.assertEqual(self.__opz.calculate("3*6", messages=False), 18)
        self.assertEqual(self.__opz.calculate("5-20", messages=False), -15.0)
        self.assertEqual(self.__opz.calculate("20/5", messages=False), 4.0)
        self.assertEqual(self.__opz.calculate("4 + 5 - 2", messages=False), 7.0)
        self.assertEqual(self.__opz.calculate("12 + 8 /16", messages=False), 12.5)
        self.assertEqual(self.__opz.calculate("    (   1                    +                  15    )    /    4    ", messages=False), 4.0)
        self.assertEqual(self.__opz.calculate("(12-2)*((9/3+4560)/(156-4861*2))-((125/5)+45-81*(5846/51)+651*584-651+(18/8431))", messages=False), 379085.0522)
        self.assertEqual(self.__opz.calculate("((12+4)/2)*2", messages=False), 16.0)
        self.assertEqual(self.__opz.calculate("(12+4/2)*2", messages=False), 28.0)
        self.assertEqual(self.__opz.calculate("12*3/15+4/8", messages=False), 2.9)
        self.assertEqual(self.__opz.calculate("0100", messages=False), 100.0)
        self.assertEqual(self.__opz.calculate("2m10", messages=False), 1024.0)


if __name__ == "__main__":
    unittest.main()