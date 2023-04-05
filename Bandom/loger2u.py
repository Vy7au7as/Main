import math
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

def sum_all(*args):
    total = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {total}")
    return total

def square_root(num):
    try:
        result = math.sqrt(float(num))
    except ValueError as e:
        logging.exception(f"Klaida: {e} - {num} negalima paversti į skaičių")
    else:
        logging.info(f"{num} saknis lygi: {result}")
        return result

def count_symbols(sentence):
    count = len(sentence)
    logging.info(f"Sakinio simboliu kiekis: {count}")
    return count

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.exception(f"Klaida: {e} - negalima dalinti iš nulio")
    else:
        logging.info(f"{x} padalinta is {y} lygu: {result}")
        return result

sum_all(1, 2, 3, 4, 5)
square_root(16)
square_root("a")
count_symbols("Labas pasauli!")
divide(10, 2)
divide(10, 0)
