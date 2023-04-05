import logging
import math

logging.basicConfig(filename='example.log', level=logging.INFO)

logger = logging.getLogger()

def sum_nums(*args):
    logger.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def sqrt_num(num):
    try:
        result = math.sqrt(float(num))
    except ValueError as e:
        logger.exception(f"Klaida: {e}")
    else:
        logger.info(f"{num} saknis lygi: {result}")
        return result

def count_chars(sentence):
    logger.info(f"Sakinio simboliu kiekis: {len(sentence)}")
    return len(sentence)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.exception(f"Klaida: {e}")
    else:
        logger.info(f"{x} padalinta is {y} lygu: {result}")
        return result

sum_nums(1, 2, 3, 4, 5)
sqrt_num('a')
count_chars("Labas, kaip sekasi?")
divide(10, 2)
divide(10, 0)