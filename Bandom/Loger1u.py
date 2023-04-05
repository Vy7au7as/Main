import math
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

def sum_all(*args):
    total = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {total}")
    return total

def square_root(num):
    result = math.sqrt(num)
    logging.info(f"{num} saknis lygi: {result}")
    return result

def count_symbols(sentence):
    count = len(sentence)
    logging.info(f"Sakinio simboliu kiekis: {count}")
    return count

def divide(x, y):
    result = x / y
    logging.info(f"{x} padalinta is {y} lygu: {result}")
    return result

sum_all(1, 2, 3, 4, 5)
square_root(16)
count_symbols("Labas pasauli!")
divide(10, 2)
