from opz import OPZ

if __name__ == "__main__":
    opz = OPZ()
    with open("input.txt") as file:
        string = file.read().strip()

    result = opz.calculate(string)

    print(round(result, 4))
