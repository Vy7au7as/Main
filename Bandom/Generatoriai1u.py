def even_generator():
    num = 2
    while True:
        yield num
        num += 2
gen = even_generator()
print(next(gen))  # išvestų 2
print(next(gen))  # išvestų 4
print(next(gen))  # išvestų 6
# ir taip toliau, grąžindamas sekantį porinį skaičių kiekvienoje iteracijoje
